from typing import List, Dict, Any

from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Items import PEItemData, item_data_table, item_table
from .Locations import PELoctData, location_data_table, location_table
from .Regions import PERegions
from .Options import PEOptions


class PEWeb(WebWorld):
    theme = "ice"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Parasite Eve Open-World Randomizer on your computer. This guide covers single-player and multiworld seeds.",
        "English",
        "pe_setup_en.md",
        "pe_setup/en",
        ["chrisaegrimm"]
    )
    tutorials = [setup_en]


class PEWorld(World):
    """
    One of them is a police officer. The other is possessed by an ancient evil threatening all life on Earth. The horrifying bond between them will continue until one of them dies.
    Join NYPD rookie Aya Brea as she tracks down the biological entity known as Eve. Upgrade your weapons and hidden mitochondrial powers to save the city.
    """
    game = "Parasite Eve"
    web = PEWeb()
    options: PEOptions
    options_dataclass = PEOptions
    location_id_to_name = PELoctData
    item_id_to_name = PEItemData

    def create_items(self, name: str) -> PEItemData:
        return PEItemData(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_item(self) -> None:
        item_pool: List[PEItemData] = []
            if item.code and item.can_create(self):
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        for region_name in PERegions.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in PERegions.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, PELoctData)
            region.add_exits(PERegions[region_name].connecting_regions)

from typing import List, Dict, Any

from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Items import PEItem, PEItemData, item_table
from .Locations import PELoctData, location_data_table, location_table
from .Regions import PERegions
from .Options import PEOptions, pe_option_groups


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


    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "schmoovement":                 self.options.schmoovement.value,
            "event_skip":                   self.options.event_skip.value,
            "randomizer_mode":              self.options.randomizer_mode.value,
            "end_goal":                     self.options.end_goal.value,
            "start_with_precinct":          self.options.start_with_precinct.value,
            "starting_unlocked_areas":      self.options.starting_unlocked_areas.value,
            "include_chrysler_bldg":        self.options.include_chrysler_bldg.value,
            "unreasonable_checks":          self.options.unreasonable_checks.value,
            "required_junk":                self.options.required_junk.value,
            "combat_difficulty":            self.options.combat_difficulty.value,
            "item_pool_difficulty":         self.options.item_pool_difficulty.value,
            "force_pe_staleness":           self.options.force_pe_staleness.value,
            "scavenger_mode":               self.options.scavenger_mode.value,
            "armor_attachments":            self.options.armor_attachments.value,
            "pesanity":                     self.options.pesanity.value,
            "statsanity":                   self.options.statsanity.value,
            "hidden_potential":             self.options.hidden_potential.value,
            "buff_nontraditional_weaponry": self.options.buff_nontraditional_weaponry.value,
            "equip_min_base_off":           self.options.equip_min_base_off.value,
            "equip_max_base_off":           self.options.equip_max_base_off.value,
            "equip_min_base_rng":           self.options.equip_min_base_rng.value,
            "equip_max_base_rng":           self.options.equip_max_base_rng.value,
            "equip_min_base_blt":           self.options.equip_min_base_blt.value,
            "equip_max_base_blt":           self.options.equip_max_base_blt.value,
            "equip_min_base_def":           self.options.equip_min_base_def.value,
            "equip_max_base_def":           self.options.equip_max_base_def.value,
            "equip_min_base_pen":           self.options.equip_min_base_pen.value,
            "equip_max_base_pen":           self.options.equip_max_base_pen.value,
            "equip_min_base_crt":           self.options.equip_min_base_crt.value,
            "equip_max_base_crt":           self.options.equip_max_base_crt.value,
            "equip_min_plus_off":           self.options.equip_min_plus_off.value,
            "equip_max_plus_off":           self.options.equip_max_plus_off.value,
            "equip_min_plus_rng":           self.options.equip_min_plus_rng.value,
            "equip_max_plus_rng":           self.options.equip_max_plus_rng.value,
            "equip_min_plus_blt":           self.options.equip_min_plus_blt.value,
            "equip_max_plus_blt":           self.options.equip_max_plus_blt.value,
            "equip_min_plus_def":           self.options.equip_min_plus_def.value,
            "equip_max_plus_def":           self.options.equip_max_plus_def.value,
            "equip_min_plus_pen":           self.options.equip_min_plus_pen.value,
            "equip_max_plus_pen":           self.options.equip_max_plus_pen.value,
            "equip_min_plus_crt":           self.options.equip_min_plus_crt.value,
            "equip_max_plus_crt":           self.options.equip_max_plus_crt.value,
            "equip_min_mod_slots":          self.options.equip_min_mod_slots.value,
            "equip_max_mod_slots":          self.options.equip_max_mod_slots.value,
            "death_link":                   self.options.death_link.value,
        }


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


    def create_items(self):
        itempool = []

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = PEItem(name, item_data.classification, item_data.code, self.player)
        return item

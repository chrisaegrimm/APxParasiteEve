from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Items import PEItemData
from .Locations import PELoctData
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

    def create_regions(self) -> None:
        self.multiworld.regions.append(Region("Menu", self.player, self.multiworld))

    def create_items(self) -> None:
        pass

    def create_item(self, name: str) -> "Item":
        item_class = self.get_item_classification(name)
        return TemplateItem(name, item_class, self.item_id_to_name.get(name, None), self.player)

    def get_item_classification(self, name: str) -> ItemClassification:
        return ItemClassification.progression


class TemplateItem(Item):
    game = "template"


class TemplateLocation(Location):
    game = "template"

from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld


class HelloWeb(WebWorld):
    setup_en = Tutorial(
        "setup",
        "description here",
        "en",
        "setup_en.md",
        "setup/en",
        ["your name here"]
    )
    tutorials = [setup_en]


class HelloWorld(World):
    game = "template"
    web = HelloWeb()
    location_id_to_name = {}
    item_id_to_name = {}

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

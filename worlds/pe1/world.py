from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
from . import items, locations, options, regions, rules, web_world




class PE1World(World):
    """
    One of them is a police officer. The other is possessed by an ancient evil threatening all life on Earth.
    The horrifying bond between them will continue until one of them dies.
    Join NYPD rookie Aya Brea as she tracks down the biological entity known as Eve.
    Upgrade your weapons and hidden mitochondrial powers to save the city.
    """

    game = "Parasite Eve"
    web = web_world.PE1WebWorld()

    options_dataclass = options.PE1Options
    options: options.PE1Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    origin_region_name = "Manhattan (World Map)"


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)


    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.PE1Item:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)


    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "schmoovement", "event_skip",
            "randomizer_mode", "end_goal", "starting_unlocked_areas",
            "include_chrysler_bldg", "unreasonable_checks", "required_junk",
            "combat_difficulty", "item_pool_difficulty", "include_took_kits",
            "include_traps", "include_boosts", "force_pe_staleness",
            "scavenger_mode", "starting_inventory_slots", "armor_attachments",
            "pesanity", "levelstatsanity",
            "hidden_potential", "shuffle_equipment_types",
            "accurate_equipment_type_icon", "buff_nontraditional_weaponry",
            "equip_min_base_off", "equip_max_base_off",
            "equip_min_base_rng", "equip_max_base_rng",
            "equip_min_base_blt", "equip_max_base_blt",
            "equip_min_base_def", "equip_max_base_def",
            "equip_min_base_pen", "equip_max_base_pen",
            "equip_min_base_crt", "equip_max_base_crt",
            "equip_min_plus_off", "equip_max_plus_off",
            "equip_min_plus_rng", "equip_max_plus_rng",
            "equip_min_plus_blt", "equip_max_plus_blt",
            "equip_min_plus_def", "equip_max_plus_def",
            "equip_min_plus_pen", "equip_max_plus_pen",
            "equip_min_plus_crt", "equip_max_plus_crt",
            "equip_min_mod_slots", "equip_max_mod_slots",
            "death_link"
        )
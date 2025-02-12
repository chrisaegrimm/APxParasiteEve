from copy import deepcopy
from typing import Dict, List

from BaseClasses import ItemClassification, Location, Region, Tutorial, CollectionState
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule
from .Items import PEItem, item_data_table, item_table
from .Locations import PELoct, location_data_table, location_table
from .Options import PEOptions, pe_option_groups
from . import Logic


class PEWebWorld(WebWorld):
    theme = "ice"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Parasite Eve in Archipelago.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["chrisaegrimm"]
    )

    tutorials = [setup_en]

    option_groups = pe_option_groups


class PEWorld(World):
    """It gud game."""

    game = "Parasite Eve"
    web = PEWebWorld()
    options_dataclass = PEOptions
    options: PEOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def create_item(self, name: str) -> PEItem:
        return PEItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[PEItem] = []

        location_count: int = 405

        item_pool += [self.create_item(name)
                      for name in item_data_table.keys()
                      if name not in self.options.start_inventory]

        self.multiworld.itempool += item_pool


    def create_regions(self) -> None:
        from .Regions import region_data_table

        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name
            }, PELoct)

            region.add_exits(region_data_table[region_name].connecting_regions)


    def get_filler_item_name(self) -> str:
        return "Junk"


    def set_rules(self) -> None:
        set_rule(self.multiworld.get_location("Chrysler BLDG. - 70F Queen Bee: Boss Drop", self.player),
                 lambda state: logic.mygame_has_key(state, self.player))
#       self.multiworld.completion_condition[self.player] = lambda state: state.has("Chrysler Key 7", self.player)

    def fill_slot_data(self):
        return {
            "schmoovement":                  self.options.schmoovement.value,
            "event_skip":                    self.options.event_skip.value,

            "randomizer_mode":               self.options.randomizer_mode.value,
            "end_goal":                      self.options.end_goal.value,
            "start_with_precinct":           self.options.start_with_precinct.value,
            "starting_unlocked_areas":       self.options.starting_unlocked_areas.value,
            "include_chrysler_bldg":         self.options.include_chrysler_bldg.value,
            "unreasonable_checks":           self.options.unreasonable_checks.value,
            "required_junk":                 self.options.required_junk.value,

            "combat_difficulty":             self.options.combat_difficulty.value,
            "item_pool_difficulty":          self.options.item_pool_difficulty.value,
            "include_traps":                 self.options.include_traps.value,
            "include_boosts":                self.options.include_boosts.value,
            "force_pe_staleness":            self.options.force_pe_staleness.value,
            "scavenger_mode":                self.options.scavenger_mode.value,
            "armor_attachments":             self.options.armor_attachments.value,
            "pesanity":                      self.options.pesanity.value,
            "levelstatsanity":               self.options.levelstatsanity.value,

            "hidden_potential":              self.options.hidden_potential.value,
            "shuffle_equipment_types":       self.options.shuffle_equipment_types.value,
            "accurate_equipment_type_icon":  self.options.accurate_equipment_type_icon.value,
            "buff_nontraditional_weaponry":  self.options.buff_nontraditional_weaponry.value,
            "equip_min_base_off":            self.options.equip_min_base_off.value,
            "equip_max_base_off":            self.options.equip_max_base_off.value,
            "equip_min_base_rng":            self.options.equip_min_base_rng.value,
            "equip_max_base_rng":            self.options.equip_max_base_rng.value,
            "equip_min_base_blt":            self.options.equip_min_base_blt.value,
            "equip_max_base_blt":            self.options.equip_max_base_blt.value,
            "equip_min_base_def":            self.options.equip_min_base_def.value,
            "equip_max_base_def":            self.options.equip_max_base_def.value,
            "equip_min_base_pen":            self.options.equip_min_base_pen.value,
            "equip_max_base_pen":            self.options.equip_max_base_pen.value,
            "equip_min_base_crt":            self.options.equip_min_base_crt.value,
            "equip_max_base_crt":            self.options.equip_max_base_crt.value,
            "equip_min_plus_off":            self.options.equip_min_plus_off.value,
            "equip_max_plus_off":            self.options.equip_max_plus_off.value,
            "equip_min_plus_rng":            self.options.equip_min_plus_rng.value,
            "equip_max_plus_rng":            self.options.equip_max_plus_rng.value,
            "equip_min_plus_blt":            self.options.equip_min_plus_blt.value,
            "equip_max_plus_blt":            self.options.equip_max_plus_blt.value,
            "equip_min_plus_def":            self.options.equip_min_plus_def.value,
            "equip_max_plus_def":            self.options.equip_max_plus_def.value,
            "equip_min_plus_pen":            self.options.equip_min_plus_pen.value,
            "equip_max_plus_pen":            self.options.equip_max_plus_pen.value,
            "equip_min_plus_crt":            self.options.equip_min_plus_crt.value,
            "equip_max_plus_crt":            self.options.equip_max_plus_crt.value,
            "equip_min_mod_slots":           self.options.equip_min_mod_slots.value,
            "equip_max_mod_slots":           self.options.equip_max_mod_slots.value,

            "death_link":                    self.options.death_link.value,
        }

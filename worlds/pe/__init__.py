from Typing import NamedTuple, List, Dict

from BaseClasses import Location, Region, Item, ItemClassification, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Options import PEOptions, pe_option_groups
from .Locations import PELoct, location_data_table, location_table
from .Regions import region_data_table
from .Items import PEItem, data_item_table, item_table


class PEWeb(WebWorld):
    theme = "ice"
    game = "Parasite Eve"
    option_groups = pe_option_groups

    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Parasite Eve Open-World Randomizer on your computer. This guide covers single-player and AP multiworld seeds.",
            language="English",
            file_name="pe_setup_en.md",
            link="pe_setup/en",
            authors=["chrisaegrimm"]
        )
    ]


class PEWorld(World):
    """
    One of them is a police officer. The other is possessed by an ancient evil threatening all life on Earth. The horrifying bond between them will continue until one of them dies.
    Join NYPD rookie Aya Brea as she tracks down the biological entity known as Eve. Upgrade your weapons and hidden mitochondrial powers to save the city.
    """
    game = "Parasite Eve"
    web = PEWeb()
    options: PEOptions
    options_dataclass = PEOptions
    location_name_to_id = location_table
    item_name_to_id = item_table


    def fill_slot_data(self):
        return {
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


    def create_item(self, name: str) -> PEItem:
        return PEItem(name, item_data_table[name].classification, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[PEItem] = []

        location_count: int = 615

    item_pool += [self.create_item(name)
                  for name in item_data_table.keys()
                  if name not in self.options.start_inventory]

    filler_item_count: int = location_count - len(item_pool)
    item_pool += [self.create_item("Junk") for _ in range(filler_item_count)]

    self.multiworld.itempool += item_pool


    def create_regions(self) -> None:
        from .Regions import region_data_table
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_table.items()
                if location_data.region == region_name
            }, PELoct)
        region.add_exits(region_data_table[region_name].connecting_regions)


    def get_filler_item_name(self) -> str:
        return "Junk"

    
    def set_rules(self) -> None:
        final_boss: str
        if self.options.end_goal.option_endeve4:
            final_boss = "Defeated Eve 4"
        elif self.options.end_goal.option_endubescape:
            final_boss = "Survived U.B."
        elif self.options.end_goal.option_endpurebred:
            final_boss = "Defeated The Purebred"
        elif self.options.end_goal.option_endallfinals:
            final_boss = "Cleared Both Final Sequences"
        else final_boss = "Final Boss String Failed On self.options.end_goal.option???"

        self.multiworld.completion_condition[self.player] = lambda state: state.has(final_boss, self.player)

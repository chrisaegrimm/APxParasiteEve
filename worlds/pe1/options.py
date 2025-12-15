from dataclasses import dataclass
from Options import Choice, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle


class Schmoovement(Choice):
    """
    Allows for quick movement outside of battle.
    """
    display_name = "Schmoovement"
    option_off = 0
    option_holdonly = 1
    option_on = 2
    default = 2

class EventSkip(DefaultOnToggle):
    """
    Allows in-game Event Skip feature while also allowing holding Square to skip past FMVs and dialogue when prompted.
    """
    display_name = "Event Skip"

class RandomizerMode(Choice):
    """
    Determine how you want the randomizer to be played.

    Open World: Start on the World Map and unlock locations in any order to progress.
    Dungeon Crawler: Gameplay is locked within the Chrysler Building, replacing its exit with the Cruiser as a hub.
    """
    display_name = "Randomizer Mode"
    option_openworld = 0
    option_dungeoncrawler = 1
    default = 0

class EndGoal(Choice):
    """
    Choose what sends Victory within your game. Note: All slimy staircases require Maeda's 3 good luck charms.

    Statue of Liberty: Clearing Museum and defeating Eve at the Statue of Liberty clears your game, skipping Ultimate Being.
    U.B.'s Escape: Clearing Museum, defeating Eve and U.B., then successfully blowing up the Cruiser clears your game.
    Secret Boss: Climbing the Chrysler Building and defeating the boss on the 77th Floor clears your game.
    Both Final Bosses: CB is locked after the 70th Floor. U.B.'s Escape leads you to the 71st Floor. Defeating the 77th Floor's boss clears your game.
    """
    display_name = "End Goal"
    option_endeve4 = 0
    option_endubescape = 1
    option_endpurebred = 2
    option_endallfinals = 3
    default = 1

class StartingUnlockedAreas(Range):
    """
    In Open World, choose how many areas , aside from the Precinct, are unlocked from the start (chosen at random).
    Note: This does not include the "Include Chrysler BLDG" option.
    """
    display_name = "Starting Unlocked Areas"
    range_start = 0
    range_end = 7
    default = 7

class IncludeChryslerBLDG(Choice):
    """
    Choose how the Chrysler Building is arranged to match your preferences:

    None: The Chrysler Building is not included in your seed and thus will never be unlocked.
    Boss: Only every 10th Floor is included, greatly reducing the checks included within.
    Quick: Includes two random floors and a boss floor per floor set. (18, 19, 20, 28, 29, 30, etc.)
    Full: All 77 floors of the Chrysler Building are present and contain checks that may be required.
    """
    display_name = "Include Chrysler BLDG"
    option_cbnone = 0
    option_cbboss = 1
    option_cbquick = 2
    option_cbfull = 3
    default = 0

class UnreasonableChecks(Toggle):
    """
    Toggle whether locations requiring rare trading cards, junk, or an absurd level of farming can have progression.
    """
    display_name = "Unreasonable Checks"

class RequiredJunk(Range):
    """
    If 'Unreasonable Checks' are enabled, set how many Junk are required for the 'Leave It to Wayne' location.

    Note: Junk can be affected by 'Scavenger Mode', requiring all Junk to be found instead of dropped.
    If the locations are available, the item pool may remove filler items to force Junk, lessening heals, cures, tools, etc.
    """
    display_name = "Required Junk"
    range_start = 0
    range_end = 300
    default = 0


class CombatDifficulty(Choice):
    """
    Choose how strict weapon/armor/PE/stat requirements can get for enemies and bosses.

    Note: 'Combat Difficulty' and 'Item Pool Difficulty' work separately.
    """
    display_name = "Combat Difficulty"
    option_generous = 0
    option_moderate = 1
    option_strict = 2
    option_masochistic = 3
    default = 0

class ItemPoolDifficulty(Choice):
    """
    Choose how generous the item pool can be for providing non-progression items to assist you.

    Generous/Moderate: Expect heals, tools, stats, and all PE to be present.
    Strict: Expect limited items to offer help and some PE abilities to be missing.
    Masochistic: Expect the bare minimum to aid you in your quest.

    Note: 'Combat Difficulty' and 'Item Pool Difficulty' work separately.
    """
    display_name = "Item Pool Difficulty"
    option_generous = 0
    option_moderate = 1
    option_strict = 2
    option_masochistic = 3
    default = 0

class IncludeToolKits(Choice):
    """
    Adds in Tool Kit and Super Tool Kit into the main item pool. These can be removed if you're seeking more of a challenge.
    """
    display_name = "Include Tool Kits"
    option_excludekits = 0
    option_include1kit = 1
    option_include2kit = 2
    default = 2

class IncludeTraps(Toggle):
    """
    Adds traps to the item pool based on your choice in Item Pool Difficulty. Traps aren't included in logic and can include
    traps like Darkness Trap and Confusion Trap, affecting you outside of combat as well.
    """
    display_name = "Include Traps"

class IncludeBoosts(Toggle):
    """
    Adds boosts to the item pool based on your choice in Item Pool Difficulty. Boosts aren't included in logic and can include
    boons like increasing your bonus points and replenishing your current HP / PE.
    """
    display_name = "Include Boosts"

class ForcePEStaleness(Toggle):
    """
    Regarded as a glitch and not a feature, this setting removes the ability to switch armors in combat,
    leaving access to PE limited as the fight goes on. Revives will still reset PE staleness.
    """
    display_name = "Force PE Staleness"

class ScavengerMode(Toggle):
    """
    Removes the ability to receive items from common enemies.

    Note: Bosses may still drop items and carry progression.
    """
    display_name = "Scavenger Mode"

class StartingInventorySlots(Range):
    """
    Sets your inventory slots available from the start. Vanilla starts you with 10 slots and, by default, the rando starts you
    with 14 slots, anticipating key items you can't discard. This option changes Aya's Item Capacity STAT rather than max slots,
    so lower starting items will increase faster as Aya levels early on.
    """
    display_name = "Starting Inventory Slots"
    range_start = 10
    range_end = 46
    default = 14

class ArmorAttachments(Toggle):
    """
    Adds the mechanic from Parasite Eve 2 where item slots are limited in combat. The amount available are
    determined from armor type and are always the first slots of your inventory. SORTING IS IMPORTANT NOW!
    """
    display_name = "Armor Attachments"

class PESanity(Choice):
    """
    Choose whether to randomize your learned PE spells and broaden their possible locations.

    Note: You may be without reliable healing from PE until the proper spell is found.
    """
    display_name = "PESanity"
    option_pevanilla = 0
    option_pelevels = 1
    option_pelocations = 2
    default = 0

class LevelStatSanity(Toggle):
    """
    Shuffle every stat gained from levels, as well as make every stat normally gained a check.

    Note: This greatly extends your amount of available locations at the cost of making combat a pain.
    If 'Unreasonable Checks' are turned on as well, you may be required to climb to Level 36 for progression.
    """
    display_name = "LevelStatSanity"


class HiddenPotential(Toggle):
    """
    This locks weapon and armor mods behind locked slots, starting every weapon and armor with minimum slots.
    As you upgrade with permits/tools, mods will be revealed as you expand the available slots.

    Note: This setting ignores 'Equipment Minimum Mod Slot Pool', but sets every weapon and armor's maximum
    slots to the chosen setting for 'Equipment Maximum Mod Slot Pool'.
    """
    display_name = "Hidden Potential"

class ShuffleEquipmentTypes(Toggle):
    """
    Allows weapon and armor types of weapons and armor to be shuffled.
    Rifles may become clubs and shotguns may become rocket launchers.
    """
    display_name = "Shuffle Equipment Types"

class AccurateEquipmentTypeIcon(Choice):
    """
    An extension of Shuffle Equipment Types, this settings changes the icons of the equipment affected by type shuffle
    to however you decide here: Accurate to the new type, shuffled and unmatched, or simply hidden entirely.
    This setting has no effect without Shuffle Equipment Types active.
    """
    display_name = "Accurate Equipment Type Icon"
    option_accurate = 0
    option_shuffled = 1
    option_hidden = 2
    default = 0

class ShuffleEquipmentStats(Toggle):
    """
    Allows shuffling of base and plus stats, as well as minimum and maximum mod slots, for all equipment based on the parameters you choose
    within this category. Setting this to false will keep vanilla stats and slots, ignoring all set stat ranges in this yaml.
    """
    display_name = "Shuffle Equipment Types"

class BuffNontraditionalWeaponry(Toggle):
    """
    This setting applies the value in Equipment Maximum Base stat settings and applies a 1.5x multiplier for
    Clubs/DNA Handguns and a 2x multiplier for Rocket Launchers, granting more use for less modular weapons.

    Note: Combined with Equipment Maximum Base stat settings, the cap remains 255 for a buffed weapon.
    """
    display_name = "Buff Nontraditional Weaponry"

class EquipmentMinimumBaseOffense(Range):
    """
    Set the lowest possible base Offense stat on a weapon.
    """
    display_name = "Equipment Minimum Base Offense"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseOffense(Range):
    """
    Set the highest possible base Offense stat on a weapon.
    """
    display_name = "Equipment Maximum Base Offense"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseRange(Range):
    """
    Set the lowest possible base Range stat on a weapon.
    """
    display_name = "Equipment Minimum Base Range"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseRange(Range):
    """
    Set the highest possible base Range stat on a weapon.
    """
    display_name = "Equipment Maximum Base Range"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseBullets(Range):
    """
    Set the lowest possible base Bullets stat on a weapon.
    """
    display_name = "Equipment Minimum Base Bullets"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseBullets(Range):
    """
    Set the highest possible base Bullets stat on a weapon.
    """
    display_name = "Equipment Maximum Base Bullets"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseDefense(Range):
    """
    Set the lowest possible base Defense stat on an armor.
    """
    display_name = "Equipment Minimum Base Defense"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseDefense(Range):
    """
    Set the highest possible base Defense stat on an armor.
    """
    display_name = "Equipment Maximum Base Defense"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBasePEnergy(Range):
    """
    Set the lowest possible base P.Energy stat on an armor.
    """
    display_name = "Equipment Minimum Base P.Energy"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBasePEnergy(Range):
    """
    Set the highest possible base P.Energy stat on an armor.
    """
    display_name = "Equipment Maximum Base P.Energy"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseCrEvade(Range):
    """
    Set the lowest possible base CrEvade stat on an armor.
    """
    display_name = "Equipment Minimum Base CrEvade"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseCrEvade(Range):
    """
    Set the highest possible base CrEvade stat on an armor.
    """
    display_name = "Equipment Maximum Base CrEvade"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumPlusOffense(Range):
    """
    Set the lowest possible plus Offense stat on a weapon.
    """
    display_name = "Equipment Minimum Plus Offense"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusOffense(Range):
    """
    Set the highest possible plus Offense stat on a weapon.
    """
    display_name = "Equipment Maximum Plus Offense"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusRange(Range):
    """
    Set the lowest possible plus Range stat on a weapon.
    """
    display_name = "Equipment Minimum Plus Range"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusRange(Range):
    """
    Set the highest possible plus Range stat on a weapon.
    """
    display_name = "Equipment Maximum Plus Range"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusBullets(Range):
    """
    Set the lowest possible plus Bullets stat on a weapon.
    """
    display_name = "Equipment Minimum Plus Bullets"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusBullets(Range):
    """
    Set the highest possible plus Bullets stat on a weapon.
    """
    display_name = "Equipment Maximum Plus Bullets"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusDefense(Range):
    """
    Set the lowest possible plus Defense stat on an armor.
    """
    display_name = "Equipment Minimum Plus Defense"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusDefense(Range):
    """
    Set the highest possible plus Defense stat on an armor.
    """
    display_name = "Equipment Maximum Plus Defense"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusPEnergy(Range):
    """
    Set the lowest possible plus P.Energy stat on an armor.
    """
    display_name = "Equipment Minimum Plus P.Energy"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusPEnergy(Range):
    """
    Set the highest possible plus P.Energy stat on an armor.
    """
    display_name = "Equipment Maximum Plus P.Energy"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusCrEvade(Range):
    """
    Set the lowest possible plus CrEvade stat on an armor.
    """
    display_name = "Equipment Minimum Plus CrEvade"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusCrEvade(Range):
    """
    Set the highest possible plus CrEvade stat on an armor.
    """
    display_name = "Equipment Maximum Plus CrEvade"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumModSlots(Range):
    """
    Set the lowest possible mod slots any weapon or armor can start with.
    """
    display_name = "Equipment Minimum Mod Slots"
    range_start = 0
    range_end = 10
    default = 1

class EquipmentMaximumModSlots(Range):
    """
    Set the highest possible mod slots any weapon or armor can be upgraded to.
    """
    display_name = "Equipment Maximum Mod Slots"
    range_start = 0
    range_end = 10
    default = 10




@dataclass
class PE1Options(PerGameCommonOptions):

    schmoovement:                  Schmoovement
    event_skip:                    EventSkip
    randomizer_mode:               RandomizerMode
    end_goal:                      EndGoal
    starting_unlocked_areas:       StartingUnlockedAreas
    include_chrysler_bldg:         IncludeChryslerBLDG
    unreasonable_checks:           UnreasonableChecks
    required_junk:                 RequiredJunk
    combat_difficulty:             CombatDifficulty
    item_pool_difficulty:          ItemPoolDifficulty
    include_tool_kits:             IncludeToolKits
    include_traps:                 IncludeTraps
    include_boosts:                IncludeBoosts
    force_pe_staleness:            ForcePEStaleness
    scavenger_mode:                ScavengerMode
    starting_inventory_slots:      StartingInventorySlots
    armor_attachments:             ArmorAttachments
    pesanity:                      PESanity
    levelstatsanity:               LevelStatSanity
    hidden_potential:              HiddenPotential
    shuffle_equipment_types:       ShuffleEquipmentTypes
    accurate_equipment_type_icon:  AccurateEquipmentTypeIcon
    buff_nontraditional_weaponry:  BuffNontraditionalWeaponry
    equip_min_base_off:            EquipmentMinimumBaseOffense
    equip_max_base_off:            EquipmentMaximumBaseOffense
    equip_min_base_rng:            EquipmentMinimumBaseRange
    equip_max_base_rng:            EquipmentMaximumBaseRange
    equip_min_base_blt:            EquipmentMinimumBaseBullets
    equip_max_base_blt:            EquipmentMaximumBaseBullets
    equip_min_base_def:            EquipmentMinimumBaseDefense
    equip_max_base_def:            EquipmentMaximumBaseDefense
    equip_min_base_pen:            EquipmentMinimumBasePEnergy
    equip_max_base_pen:            EquipmentMaximumBasePEnergy
    equip_min_base_crt:            EquipmentMinimumBaseCrEvade
    equip_max_base_crt:            EquipmentMaximumBaseCrEvade
    equip_min_plus_off:            EquipmentMinimumPlusOffense
    equip_max_plus_off:            EquipmentMaximumPlusOffense
    equip_min_plus_rng:            EquipmentMinimumPlusRange
    equip_max_plus_rng:            EquipmentMaximumPlusRange
    equip_min_plus_blt:            EquipmentMinimumPlusBullets
    equip_max_plus_blt:            EquipmentMaximumPlusBullets
    equip_min_plus_def:            EquipmentMinimumPlusDefense
    equip_max_plus_def:            EquipmentMaximumPlusDefense
    equip_min_plus_pen:            EquipmentMinimumPlusPEnergy
    equip_max_plus_pen:            EquipmentMaximumPlusPEnergy
    equip_min_plus_crt:            EquipmentMinimumPlusCrEvade
    equip_max_plus_crt:            EquipmentMaximumPlusCrEvade
    equip_min_mod_slots:           EquipmentMinimumModSlots
    equip_max_mod_slots:           EquipmentMaximumModSlots
    death_link:                    DeathLink




option_groups = [

    OptionGroup(
        "World Options",
        [
        RandomizerMode,
        EndGoal,
        StartingUnlockedAreas,
        IncludeChryslerBLDG,
        UnreasonableChecks,
        RequiredJunk
        ]
    ),

    OptionGroup(
        "Item Options",
        [
        CombatDifficulty,
        ItemPoolDifficulty,
        IncludeToolKits,
        IncludeTraps,
        IncludeBoosts,
        ForcePEStaleness,
        ScavengerMode,
        StartingInventorySlots,
        ArmorAttachments,
        PESanity,
        LevelStatSanity
        ],
    ),

    OptionGroup(
        "Stat Options",
        [
        HiddenPotential,
        ShuffleEquipmentTypes,
        AccurateEquipmentTypeIcon,
        ShuffleEquipmentStats,
        BuffNontraditionalWeaponry,
        EquipmentMinimumBaseOffense,
        EquipmentMaximumBaseOffense,
        EquipmentMinimumBaseRange,
        EquipmentMaximumBaseRange,
        EquipmentMinimumBaseBullets,
        EquipmentMaximumBaseBullets,
        EquipmentMinimumBaseDefense,
        EquipmentMaximumBaseDefense,
        EquipmentMinimumBasePEnergy,
        EquipmentMaximumBasePEnergy,
        EquipmentMinimumBaseCrEvade,
        EquipmentMaximumBaseCrEvade,
        EquipmentMinimumPlusOffense,
        EquipmentMaximumPlusOffense,
        EquipmentMinimumPlusRange,
        EquipmentMaximumPlusRange,
        EquipmentMinimumPlusBullets,
        EquipmentMaximumPlusBullets,
        EquipmentMinimumPlusDefense,
        EquipmentMaximumPlusDefense,
        EquipmentMinimumPlusPEnergy,
        EquipmentMaximumPlusPEnergy,
        EquipmentMinimumPlusCrEvade,
        EquipmentMaximumPlusCrEvade,
        EquipmentMinimumModSlots,
        EquipmentMaximumModSlots,
        ],
    ),
]


#Can return to add option presets if I choose, probably make one for each rando mode from the lua-based rando.
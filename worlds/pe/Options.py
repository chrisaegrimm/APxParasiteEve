from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, DeathLink, OptionGroup, PerGameCommonOptions


class Schmoovement(Choice)
    """
    Allows for quick movement outside of battle.
    """
    display_name = "Schmoovement"
    option_off = 0
    option_holdonly = 1
    option_on = 2
    default = 2

class EventSkip(DefaultOnToggle)
    """
    Allows in-game Event Skip feature while also allowing holding Square to skip past FMVs and dialogue when prompted.
    """
    display_name = "Event Skip"


class RandomizerMode(Choice)
    """
    Determine how you want the randomizer to be played.

    Open World: Start on the World Map and unlock locations in any order to progress.
    Dungeon Crawler: Gameplay is locked within the Chrysler Building, replacing its exit with the Cruiser as a hub.
    """
    display_name = "Randomizer Mode"
    option_openworld = 0
    option_dungeoncrawler = 1
    default = 0

class EndGoal(Choice)
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

class StartWithPrecinct(DefaultOnToggle)
    """
    In Open World, start with access to the Precinct for inventory management and starting checks.
    """
    display_name = "Start with Precinct"

class StartingUnlockedAreas(Range)
    """
    In Open World, choose how many areas are unlocked from the start (chosen at random).
    Note: This does not include the 'Starting with Precinct' option, as well as the Chrysler Building.
    """
    display_name = "Starting Unlocked Areas"
    range_start = 0
    range_end = 8
    default = 8

class IncludeChryslerBuilding(Choice)
    """
    Choose how the Chrysler Building is arranged to match your preferences:

    None: The Chrysler Building is not included in your seed and thus will never be unlocked.
    Boss: Only every 10th Floor is included, greatly reducing the checks included within.
    Quick: Includes two random floors and a boss floor per floor set. (18, 19, 20, 28, 29, 30, etc.)
    Full: All 77 floors of the Chrysler Building are present and contain checks that may be required.
    """
    display_name = "Include Chrysler Building"
    option_cbnone = 0
    option_cbboss = 1
    option_cbquick = 2
    option_cbfull = 3
    default = 0

class UnreasonableChecks(Toggle)
    """
    Toggle whether locations requiring rare trading cards, junk, or an absurd level of farming can have progression.
    """
    display_name = "Unreasonable Checks"

class RequiredJunk(Range)
    """
    If 'Unreasonable Checks' are enabled, set how many Junk are required for the 'Leave It to Wayne' location.

    Note: Junk can be affected by 'Scavenger Mode', requiring all Junk to be found instead of dropped.
    If the locations are available, the item pool may remove filler items to force Junk, lessening heals, cures, tools, etc.
    """
    display_name = "Required Junk"
    range_start = 0
    range_end = 300
    default = 0


class CombatDifficulty(Choice)
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

class ItemPoolDifficulty(Choice)
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

class ForcePEStaleness
    """
    Regarded as a glitch and not a feature, this setting removes the ability to switch armors in combat,
    leaving access to PE limited as the fight goes on. Revives will still reset PE staleness.
    """
    display_name = "Force PE Staleness"

class ScavengerMode(Toggle)
    """
    Removes the ability to receive items from common enemies.

    Note: Bosses may still drop items and carry progression.
    """
    display_name = "Scavenger Mode"

class ArmorAttachments(Toggle)
    """
    Adds the mechanic from Parasite Eve 2 where item slots are limited in combat. The amount available are
    determined from armor type and are always the first slots of your inventory. SORTING IS IMPORTANT NOW!
    """
    display_name = "Armor Attachments"

class PESanity(Choice)
    """
    Choose whether to randomize your learned PE spells and broaden their possible locations.

    Note: You may be without reliable healing from PE until the proper spell is found.
    """
    display_name = "PESanity"
    option_pevanilla = 0
    option_pelevels = 1
    option_pelocations = 2
    default = 0

class StatSanity(Toggle)
    """
    Shuffle every stat gained from levels, as well as make every stat normally gained a check.

    Note: This greatly extends your amount of available locations at the cost of making combat a pain.
    If 'Unreasonable Checks' are turned on as well, you may required to climb to Level 36 for progression.
    """
    display_name = "StatSanity"


class HiddenPotential(Toggle)
    """
    This locks weapon and armor mods behind locked slots, starting every weapon and armor with minimum slots.
    As you upgrade with permits/tools, mods will be revealed as you expand the available slots.

    Note: This setting ignores 'Equipment Minimum Mod Slot Pool', but sets every weapon and armor's maximum
    slots to the chosen setting for 'Equipment Maximum Mod Slot Pool'.
    """
    display_name = "Hidden Potential"

class BuffNontraditionalWeaponry(Toggle)
    """
    This setting applies the value in Equipment Maximum Base stat settings and applies a 1.5x multiplier for
    Clubs/DNA Handguns and a 2x multiplier for Rocket Launchers, granting more use for less modular weapons.

    Note: Combined with Equipment Maximum Base stat settings, the cap remains 255 for a buffed weapon.
    """
    display_name = "Buff Nontraditional Weaponry"

class EquipmentMinimumBaseOffense(Range)
    """
    Set the lowest possible base Offense stat on a weapon.
    """
    display_name = "Equipment Minimum Base Offense"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseOffense(Range)
    """
    Set the highest possible base Offense stat on a weapon.
    """
    display_name = "Equipment Maximum Base Offense"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseRange(Range)
    """
    Set the lowest possible base Range stat on a weapon.
    """
    display_name = "Equipment Minimum Base Range"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseRange(Range)
    """
    Set the highest possible base Range stat on a weapon.
    """
    display_name = "Equipment Maximum Base Range"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseBullets(Range)
    """
    Set the lowest possible base Bullets stat on a weapon.
    """
    display_name = "Equipment Minimum Base Bullets"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseBullets(Range)
    """
    Set the highest possible base Bullets stat on a weapon.
    """
    display_name = "Equipment Maximum Base Bullets"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseDefense(Range)
    """
    Set the lowest possible base Defense stat on an armor.
    """
    display_name = "Equipment Minimum Base Defense"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseDefense(Range)
    """
    Set the highest possible base Defense stat on an armor.
    """
    display_name = "Equipment Maximum Base Defense"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBasePEnergy(Range)
    """
    Set the lowest possible base P.Energy stat on an armor.
    """
    display_name = "Equipment Minimum Base P.Energy"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBasePEnergy(Range)
    """
    Set the highest possible base P.Energy stat on an armor.
    """
    display_name = "Equipment Maximum Base P.Energy"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumBaseCrEvade(Range)
    """
    Set the lowest possible base CrEvade stat on an armor.
    """
    display_name = "Equipment Minimum Base CrEvade"
    range_start = 0
    range_end = 255
    default = 15

class EquipmentMaximumBaseCrEvade(Range)
    """
    Set the highest possible base CrEvade stat on an armor.
    """
    display_name = "Equipment Maximum Base CrEvade"
    range_start = 0
    range_end = 255
    default = 100

class EquipmentMinimumPlusOffense(Range)
    """
    Set the lowest possible plus Offense stat on a weapon.
    """
    display_name = "Equipment Minimum Plus Offense"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusOffense(Range)
    """
    Set the highest possible plus Offense stat on a weapon.
    """
    display_name = "Equipment Maximum Plus Offense"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusRange(Range)
    """
    Set the lowest possible plus Range stat on a weapon.
    """
    display_name = "Equipment Minimum Plus Range"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusRange(Range)
    """
    Set the highest possible plus Range stat on a weapon.
    """
    display_name = "Equipment Maximum Plus Range"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusBullets(Range)
    """
    Set the lowest possible plus Bullets stat on a weapon.
    """
    display_name = "Equipment Minimum Plus Bullets"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusBullets(Range)
    """
    Set the highest possible plus Bullets stat on a weapon.
    """
    display_name = "Equipment Maximum Plus Bullets"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusDefense(Range)
    """
    Set the lowest possible plus Defense stat on an armor.
    """
    display_name = "Equipment Minimum Plus Defense"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusDefense(Range)
    """
    Set the highest possible plus Defense stat on an armor.
    """
    display_name = "Equipment Maximum Plus Defense"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusPEnergy(Range)
    """
    Set the lowest possible plus P.Energy stat on an armor.
    """
    display_name = "Equipment Minimum Plus P.Energy"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusPEnergy(Range)
    """
    Set the highest possible plus P.Energy stat on an armor.
    """
    display_name = "Equipment Maximum Plus P.Energy"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumPlusCrEvade(Range)
    """
    Set the lowest possible plus CrEvade stat on an armor.
    """
    display_name = "Equipment Minimum Plus CrEvade"
    range_start = 0
    range_end = 255
    default = 0

class EquipmentMaximumPlusCrEvade(Range)
    """
    Set the highest possible plus CrEvade stat on an armor.
    """
    display_name = "Equipment Maximum Plus CrEvade"
    range_start = 0
    range_end = 255
    default = 4

class EquipmentMinimumModSlots(Range)
    """
    Set the lowest possible mod slots any weapon or armor can start with.
    """
    display_name = "Equipment Minimum Mod Slots"
    range_start = 0
    range_end = 10
    default = 1

class EquipmentMaximumModSlots(Range)
    """
    Set the highest possible mod slots any weapon or armor can be upgraded to.
    """
    display_name = "Equipment Maximum Mod Slots"
    range_start = 0
    range_end = 10
    default = 10



pe_option_groups = [
    OptionGroup("World Options", [
        RandomizerMode,
        EndGoal,
        StartWithPrecinct,
        StartingUnlockedAreas,
        IncludeChryslerBuilding,
        UnreasonableChecks,
        RequiredJunk,
    ]),
    OptionGroup("Item Options", [
        CombatDifficulty,
        ItemPoolDifficulty,
        ForcePEStaleness,
        ScavengerMode,
        ArmorAttachments,
        PESanity,
        StatSanity,
    ]),
    OptionGroup("Stat Options", [
        HiddenPotential,
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
    ]),
]
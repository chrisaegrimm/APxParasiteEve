from BaseClasses import Item, ItemClassification
import typing


class ParasiteEveItemData(Item):
    game: str = "Parasite Eve"


class ItemData(typing.NamedTuple):
    code: int
    category: str
    classification: any


item_table: Dict[str, PEItemData] = {
    "Ammo +6":        PEItemData(624001, "AutoDist",     ItemClassification.filler),
    "Ammo +15":       PEItemData(624002, "AutoDist",     ItemClassification.useful),
    "Ammo +30":       PEItemData(624003, "AutoDist",     ItemClassification.useful),
    "DNA Bullets":    PEItemData(624004, "AutoDist",     ItemClassification.useful),
    "Rocket":         PEItemData(624005, "AutoDist",     ItemClassification.useful),
    "Medicine 1":     PEItemData(624006, "Consumable",  ItemClassification.filler),
    "Medicine 2":     PEItemData(624007, "Consumable",  ItemClassification.useful),
    "Medicine 3":     PEItemData(624008, "Consumable",  ItemClassification.useful),
    "Medicine 4":     PEItemData(624009, "Consumable",  ItemClassification.useful),
    "Full Recovery":  PEItemData(624010, "Consumable",  ItemClassification.useful),
    "Super Junk":     PEItemData(624011, "KeyItem",     ItemClassification.progression),
    "Duper Junk":     PEItemData(624012, "Junk",        ItemClassification.filler),
    "Cure-P":         PEItemData(624013, "Consumable",  ItemClassification.useful),
    "Cure-D":         PEItemData(624014, "Consumable",  ItemClassification.useful),
    "Cure-C":         PEItemData(624015, "Consumable",  ItemClassification.filler),
    "Cure-M":         PEItemData(624016, "Consumable",  ItemClassification.useful),
    "FullCure":       PEItemData(624017, "Consumable",  ItemClassification.useful),
    "Revive":         PEItemData(624018, "Consumable",  ItemClassification.useful),
    #Defense +1":     PEItemData(624019, "Unused duplicate Defense 1, unable to be used.")
    "Junk":           PEItemData(624020, "Junk",        ItemClassification.filler),
    "Trading Card":   PEItemData(624021, "CommonTCard", ItemClassification.useful),
    "Tool":           PEItemData(624022, "ToolType",    ItemClassification.useful),
    "Super Tool":     PEItemData(624023, "ToolType",    ItemClassification.useful),
    #Item24":         PEItemData(624024, "Unused item. Consumable, but has no effect.")
    #Item25":         PEItemData(624025, "Unused item. Consumable, but has no effect.")
    #Ammo Crate":     PEItemData(624026, "Crate is automatically given upon receiving its ammo.")
    #Rocket Crate":   PEItemData(624027, "Crate is automatically given upon receiving its ammo.")
    #Maeda Crate":    PEItemData(624028, "Crate is automatically given upon receiving its ammo.")
    "Offense +1":     PEItemData(624029, "Consumable",  ItemClassification.filler),
    "Offense +2":     PEItemData(624030, "Consumable",  ItemClassification.useful),
    "Offense +3":     PEItemData(624031, "Consumable",  ItemClassification.useful),
    "Offense +4":     PEItemData(624032, "Consumable",  ItemClassification.useful),
    "Range +1":       PEItemData(624033, "Consumable",  ItemClassification.filler),
    "Range +2":       PEItemData(624034, "Consumable",  ItemClassification.useful),
    "Range +3":       PEItemData(624035, "Consumable",  ItemClassification.useful),
    "Range +4":       PEItemData(624036, "Consumable",  ItemClassification.useful),
    "Bullet Cap +1":  PEItemData(624037, "Consumable",  ItemClassification.filler),
    "Bullet Cap +2":  PEItemData(624038, "Consumable",  ItemClassification.useful),
    "Bullet Cap +3":  PEItemData(624039, "Consumable",  ItemClassification.useful),
    "Bullet Cap +4":  PEItemData(624040, "Consumable",  ItemClassification.useful),
    "Defense +1":     PEItemData(624041, "Consumable",  ItemClassification.filler),
    "Defense +2":     PEItemData(624042, "Consumable",  ItemClassification.useful),
    "Defense +3":     PEItemData(624043, "Consumable",  ItemClassification.useful),
    "Defense +4":     PEItemData(624044, "Consumable",  ItemClassification.useful),
    "Cr Evade +1":    PEItemData(624045, "Consumable",  ItemClassification.filler),
    "Cr Evade +2":    PEItemData(624046, "Consumable",  ItemClassification.useful),
    "Cr Evade +3":    PEItemData(624047, "Consumable",  ItemClassification.useful),
    "Cr Evade +4":    PEItemData(624048, "Consumable",  ItemClassification.useful),
    "PE +1":          PEItemData(624049, "Consumable",  ItemClassification.filler),
    "PE +2":          PEItemData(624050, "Consumable",  ItemClassification.useful),
    "PE +3":          PEItemData(624051, "Consumable",  ItemClassification.useful),
    "PE +4":          PEItemData(624052, "Consumable",  ItemClassification.useful),
    

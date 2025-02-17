from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class PELoct(Location):
    game = "Parasite Eve"

class PELoctData(NamedTuple):
    address: Optional[int] = None
    region: str


location_data_table: Dict[str, PELoctData] = {

    "PE - Heal 1: Awakening":                                          PELoctData("Carnegie Hall: NoReqs", 625001),
    "PE - Scan: Level 4":                                              PELoctData("PE", 625002),
    "PE - Slow: Level 7":                                              PELoctData("PE", 625003),
    "PE - Detox: Level 9":                                             PELoctData("PE", 625004),
    "PE - Heal 2: Level 11":                                           PELoctData("PE", 625005),
    "PE - Barrier: Level 13":                                          PELoctData("PE", 625006),
    "PE - Energy Shot: Level 15":                                      PELoctData("PE", 625007),
    "PE - Confuse: Level 17":                                          PELoctData("PE", 625008),
    "PE - Haste: Level 20":                                            PELoctData("PE", 625009),
    "PE - Heal 3: Level 22":                                           PELoctData("PE", 625010),
    "PE - Gene Heal: Level 25":                                        PELoctData("PE", 625011),
    "PE - Medic: Level 28":                                            PELoctData("PE", 625012),
    "PE - Preraise: Level 30":                                         PELoctData("PE", 625013),
    "PE - Full Recover: Level 32":                                     PELoctData("PE", 625014),
    "PE - Liberate: Level 33":                                         PELoctData("PE", 625015),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}

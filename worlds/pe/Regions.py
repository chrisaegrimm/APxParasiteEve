from typing import NamedTuple, List, Dict


class PERegions(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, PERegions] = {

    "Menu":                                          PERegions(["Carnegie Hall: NoReqs"]),
    "Menu":                                          PERegions(["N.Y.P.D. #17: NoReqs"]),
    "Menu":                                          PERegions(["Central Park: NoReqs"]),
    "Menu":                                          PERegions(["Soho: NoReqs"]),
    "Menu":                                          PERegions(["Hospital: NoReqs"]),
    "Menu":                                          PERegions(["Chinatown: NoReqs|Combat+GK"]),
    "Menu":                                          PERegions(["Subway: Combat+PK|GK"]),
    "Menu":                                          PERegions(["Warehouse: NoReqs"]),
    "Menu":                                          PERegions(["Museum: NoReqs"]),
    "Menu":                                          PERegions(["Chrysler BLDG.: Key 1"]),

    "Carnegie Hall: NoReqs":                         PERegions(["Carnegie Hall: Combat"]),
    "Carnegie Hall: Combat":                         PERegions(["Carnegie Hall: Combat+TK"]),
    "Carnegie Hall: Combat+TK":                      PERegions(),
    "Carnegie Hall: Combat":                         PERegions(["Carnegie Hall: Combat+RK"]),
    "Carnegie Hall: Combat+RK":                      PERegions(["Carnegie Hall: Combat+RK+Boss"]),
    "Carnegie Hall: Combat+RK+Boss":                 PERegions(),

    "N.Y.P.D. #17: NoReqs":                          PERegions(["N.Y.P.D. #17: LK"]),
    "N.Y.P.D. #17: LK":                              PERegions(),
    "N.Y.P.D. #17: NoReqs":                          PERegions(["N.Y.P.D. #17: SK"]),
    "N.Y.P.D. #17: SK":                              PERegions(),
    "N.Y.P.D. #17: NoReqs":                          PERegions(["N.Y.P.D. #17: SJ"]),
    "N.Y.P.D. #17: SJ":                              PERegions(["N.Y.P.D. #17: Combat+SJ"]),
    "N.Y.P.D. #17: Combat+SJ":                       PERegions(["N.Y.P.D. #17: Combat+SJ+Boss"]),
    "N.Y.P.D. #17: Combat+SJ+Boss":                  PERegions(["N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+JunkReq"]),
    "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+JunkReq":  PERegions(),
    "N.Y.P.D. #17: Combat+SJ+Boss":                  PERegions(["N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC"]),
    "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC":    PERegions(["N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+14RTC"]),
    "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+14RTC":    PERegions(),

    "Central Park: NoReqs":                          PERegions(["Central Park: Combat"]),
    "Central Park: Combat":                          PERegions(["Central Park: Combat+ZK"]),
    "Central Park: Combat+ZK":                       PERegions(["Central Park: Combat+ZK+Boss"]),
    "Central Park: Combat+ZK+Boss":                  PERegions(),

    "Soho: NoReqs":                                  PERegions(["Soho: WM"]),
    "Soho: WM":                                      PERegions(),

    "Hospital: NoReqs":                              PERegions(["Hospital: Combat"]),
    "Hospital: Combat":                              PERegions(["Hospital: Combat+AK"]),
    "Hospital: Combat+AK":                           PERegions(),
    "Hospital: Combat":                              PERegions(["Hospital: Combat+GC"]),
    "Hospital: Combat+GC":                           PERegions(),
    "Hospital: Combat":                              PERegions(["Hospital: Combat+BC"]),
    "Hospital: Combat+BC":                           PERegions(["Hospital: Combat+BC+Fuses"]),
    "Hospital: Combat+BC+Fuses":                     PERegions(["Hospital: Combat+BC+Fuses+EK+Boss"]),
    "Hospital: Combat+BC+Fuses+EK+Boss":             PERegions(),

    "Chinatown: NoReqs|Combat+GK":                   PERegions(["Chinatown: Combat|Combat+GK"]),
    "Chinatown: Combat|Combat+GK":                   PERegions(["Chinatown: Combat+Boss|Combat+GK+Boss"]),
    "Chinatown: Combat+Boss|Combat+GK+Boss":         PERegions(),
    "Chinatown: Combat|Combat+GK":                   PERegions(["Chinatown: Combat|GK"]),
    "Chinatown: Combat|GK":                          PERegions(["Subway: Combat+PK|GK"]),

    "Subway: Combat+PK|GK":                          PERegions(["Subway: Combat+PK|Combat+GK"]),
    "Subway: Combat+PK|Combat+GK":                   PERegions(["Subway: Combat+PK+Boss|Combat+GK+Boss"]),
    "Subway: Combat+PK+Boss|Combat+GK+Boss":         PERegions(),

    "Warehouse: NoReqs":                             PERegions(["Warehouse: Combat"]),
    "Warehouse: Combat":                             PERegions(["Warehouse: Combat+WK"]),
    "Warehouse: Combat+WK":                          PERegions(["Warehouse: Combat+WK+Boss"]),
    "Warehouse: Combat+WK+Boss":                     PERegions(),

    "Museum: NoReqs":                                PERegions(["Museum: Combat"]),
    "Museum: Combat":                                PERegions(["Museum: Combat+KK"]),
    "Museum: Combat+KK":                             PERegions(["Museum: Combat+KK+Boss"]),
    "Museum: Combat+KK+Boss":                        PERegions(["PE"]),
    "PE":                                            PERegions(),
    "Museum: Combat+KK+Boss":                        PERegions(["LevelStat"]),
    "LevelStat":                                     PERegions(["LevelStat+UnrChks"]),
    "LevelStat+UnrChks":                             PERegions(),
    "Museum: Combat+KK+Boss":                        PERegions(["Cruiser"]),
    "Cruiser":                                       PERegions(),

    "Chrysler BLDG.: Key 1":                         PERegions(["Chrysler BLDG.: Key 2"]),
    "Chrysler BLDG.: Key 2":                         PERegions(["Chrysler BLDG.: Key 3"]),
    "Chrysler BLDG.: Key 3":                         PERegions(["Chrysler BLDG.: Key 4"]),
    "Chrysler BLDG.: Key 4":                         PERegions(["Chrysler BLDG.: Key 5"]),
    "Chrysler BLDG.: Key 5":                         PERegions(["Chrysler BLDG.: Key 6"]),
    "Chrysler BLDG.: Key 6":                         PERegions(["Chrysler BLDG.: Key 7"]),
    "Chrysler BLDG.: Key 7":                         PERegions(),
}

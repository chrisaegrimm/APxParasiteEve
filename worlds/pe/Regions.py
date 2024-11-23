from typing import NamedTuple, List, Dict


class PERegions(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, PERegions] = {

    "Title Screen":                               PERegions(["New York City"]),

    "New York City":                              PERegions(["Carnegie Hall: NoReqs"]),
    "New York City":                              PERegions(["N.Y.P.D. #17: NoReqs"]),
    "New York City":                              PERegions(["Central Park: NoReqs"]),
    "New York City":                              PERegions(["Soho: NoReqs"]),
    "New York City":                              PERegions(["Hospital: NoReqs"]),
    "New York City":                              PERegions(["Chinatown: NoReqs|Combat+GK"]),
    "New York City":                              PERegions(["Subway: Combat+PK|GK"]),
    "New York City":                              PERegions(["Warehouse: NoReqs"]),
    "New York City":                              PERegions(["Museum: NoReqs"]),
    "New York City":                              PERegions(["Chrysler BLDG.: Key 1"]),

    "Carnegie Hall: NoReqs":                      PERegions(["Carnegie Hall: Combat"]),
    "Carnegie Hall: Combat":                      PERegions(["Carnegie Hall: Combat+TK"]),
    "Carnegie Hall: Combat":                      PERegions(["Carnegie Hall: Combat+RK"]),
    "Carnegie Hall: Combat+RK":                   PERegions(["Carnegie Hall: Combat+RK+Boss"]),

    "N.Y.P.D. #17: NoReqs":                       PERegions(["N.Y.P.D. #17: LK"]),
    "N.Y.P.D. #17: NoReqs":                       PERegions(["N.Y.P.D. #17: SK"]),
    "N.Y.P.D. #17: NoReqs":                       PERegions(["N.Y.P.D. #17: SJ"]),
    "N.Y.P.D. #17: SJ":                           PERegions(["N.Y.P.D. #17: Combat+SJ"]),
    "N.Y.P.D. #17: Combat+SJ":                    PERegions(["N.Y.P.D. #17: Combat+SJ+Boss"]),
    "N.Y.P.D. #17: Combat+SJ+Boss":               PERegions(["N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+JunkReq"]),
    "N.Y.P.D. #17: Combat+SJ+Boss":               PERegions(["N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC"]),
    "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC": PERegions(["N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+14RTC"]),

    "Central Park: NoReqs":                       PERegions(["Central Park: Combat"]),
    "Central Park: Combat":                       PERegions(["Central Park: Combat+ZK"]),
    "Central Park: Combat+ZK":                    PERegions(["Central Park: Combat+ZK+Boss"]),

    "Soho: NoReqs":                               PERegions(["Soho: WM"]),

    "Hospital: NoReqs":                           PERegions(["Hospital: Combat"]),
    "Hospital: Combat":                           PERegions(["Hospital: Combat+AK"]),
    "Hospital: Combat":                           PERegions(["Hospital: Combat+GC"]),
    "Hospital: Combat":                           PERegions(["Hospital: Combat+BC"]),
    "Hospital: Combat+BC":                        PERegions(["Hospital: Combat+BC+Fuses"]),
    "Hospital: Combat+BC+Fuses":                  PERegions(["Hospital: Combat+BC+Fuses+EK+Boss"]),

    "Chinatown: NoReqs|Combat+GK":                PERegions(["Chinatown: Combat|Combat+GK"]),
    "Chinatown: Combat|Combat+GK":                PERegions(["Chinatown: Combat+Boss|Combat+GK+Boss"]),
    "Chinatown: Combat|Combat+GK":                PERegions(["Chinatown: Combat|GK"]),
    "Chinatown: Combat|GK":                       PERegions(["Subway: Combat+PK|GK"]),

    "Subway: Combat+PK|GK":                       PERegions(["Subway: Combat+PK|Combat+GK"]),
    "Subway: Combat+PK|Combat+GK":                PERegions(["Subway: Combat+PK+Boss|Combat+GK+Boss"]),

    "Warehouse: NoReqs":                          PERegions(["Warehouse: Combat"]),
    "Warehouse: Combat":                          PERegions(["Warehouse: Combat+WK"]),
    "Warehouse: Combat+WK":                       PERegions(["Warehouse: Combat+WK+Boss"]),

    "Museum: NoReqs":                             PERegions(["Museum: Combat"]),
    "Museum: Combat":                             PERegions(["Museum: Combat+KK"]),
    "Museum: Combat+KK":                          PERegions(["Museum: Combat+KK+Boss"]),
    "Museum: Combat+KK+Boss":                     PERegions(["Cruiser"]),

    "Chrysler BLDG.: Key 1":                      PERegions(["Chrysler BLDG.: Key 2"]),
    "Chrysler BLDG.: Key 2":                      PERegions(["Chrysler BLDG.: Key 3"]),
    "Chrysler BLDG.: Key 3":                      PERegions(["Chrysler BLDG.: Key 4"]),
    "Chrysler BLDG.: Key 4":                      PERegions(["Chrysler BLDG.: Key 5"]),
    "Chrysler BLDG.: Key 5":                      PERegions(["Chrysler BLDG.: Key 6"]),
    "Chrysler BLDG.: Key 6":                      PERegions(["Chrysler BLDG.: Key 7"]),
}

from typing import Dict, List, NamedTuple


class PERegnData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, PERegnData] = {

    "Menu":                                          PERegnData(["Carnegie Hall: NoReqs", "N.Y.P.D. #17: NoReqs",
                                                                 "Central Park: NoReqs", "Soho: NoReqs",
                                                                 "Hospital: NoReqs", "Chinatown: NoReqs|Combat+GK",
                                                                 "Subway: Combat+PK|GK", "Warehouse: NoReqs",
                                                                 "Museum: NoReqs", "Chrysler BLDG.: Key 1"]),

    "Carnegie Hall: NoReqs":                         PERegnData(["Carnegie Hall: Combat"]),
    "Carnegie Hall: Combat":                         PERegnData(["Carnegie Hall: Combat+TK", "Carnegie Hall: Combat+RK"]),
    "Carnegie Hall: Combat+TK":                      PERegnData(),
    "Carnegie Hall: Combat+RK":                      PERegnData(["Carnegie Hall: Combat+RK+Boss"]),
    "Carnegie Hall: Combat+RK+Boss":                 PERegnData(),

    "N.Y.P.D. #17: NoReqs":                          PERegnData(["N.Y.P.D. #17: LK", "N.Y.P.D. #17: SK", "N.Y.P.D. #17: SJ"]),
    "N.Y.P.D. #17: LK":                              PERegnData(),
    "N.Y.P.D. #17: SK":                              PERegnData(),
    "N.Y.P.D. #17: SJ":                              PERegnData(["N.Y.P.D. #17: Combat+SJ"]),
    "N.Y.P.D. #17: Combat+SJ":                       PERegnData(["N.Y.P.D. #17: Combat+SJ+Boss"]),
    "N.Y.P.D. #17: Combat+SJ+Boss":                  PERegnData(["N.Y.P.D. #17: Combat+SJ+Boss+UC+JunkReq",
                                                                 "N.Y.P.D. #17: Combat+SJ+Boss+UC+12RTC"]),
    "N.Y.P.D. #17: Combat+SJ+Boss+UC+JunkReq":       PERegnData(),
    "N.Y.P.D. #17: Combat+SJ+Boss+UC+12RTC":         PERegnData(["N.Y.P.D. #17: Combat+SJ+Boss+UC+14RTC"]),
    "N.Y.P.D. #17: Combat+SJ+Boss+UC+14RTC":         PERegnData(),

    "Central Park: NoReqs":                          PERegnData(["Central Park: Combat"]),
    "Central Park: Combat":                          PERegnData(["Central Park: Combat+ZK"]),
    "Central Park: Combat+ZK":                       PERegnData(["Central Park: Combat+ZK+Boss"]),
    "Central Park: Combat+ZK+Boss":                  PERegnData(),

    "Soho: NoReqs":                                  PERegnData(["Soho: WM"]),
    "Soho: WM":                                      PERegnData(),

    "Hospital: NoReqs":                              PERegnData(["Hospital: Combat"]),
    "Hospital: Combat":                              PERegnData(["Hospital: Combat+AK", "Hospital: Combat+GC", "Hospital: Combat+BC"]),
    "Hospital: Combat+AK":                           PERegnData(),
    "Hospital: Combat+GC":                           PERegnData(),
    "Hospital: Combat+BC":                           PERegnData(["Hospital: Combat+BC+Fuses"]),
    "Hospital: Combat+BC+Fuses":                     PERegnData(["Hospital: Combat+BC+Fuses+EK+Boss"]),
    "Hospital: Combat+BC+Fuses+EK+Boss":             PERegnData(),

    "Chinatown: NoReqs|Combat+GK":                   PERegnData(["Chinatown: Combat|Combat+GK"]),
    "Chinatown: Combat|Combat+GK":                   PERegnData(["Chinatown: Combat+Boss|Combat+GK+Boss", "Chinatown: Combat|GK"]),
    "Chinatown: Combat+Boss|Combat+GK+Boss":         PERegnData(),
    "Chinatown: Combat|GK":                          PERegnData(["Subway: Combat+PK|GK"]),

    "Subway: Combat+PK|GK":                          PERegnData(["Subway: Combat+PK|Combat+GK"]),
    "Subway: Combat+PK|Combat+GK":                   PERegnData(["Subway: Combat+PK+Boss|Combat+GK+Boss"]),
    "Subway: Combat+PK+Boss|Combat+GK+Boss":         PERegnData(),

    "Warehouse: NoReqs":                             PERegnData(["Warehouse: Combat"]),
    "Warehouse: Combat":                             PERegnData(["Warehouse: Combat+WK"]),
    "Warehouse: Combat+WK":                          PERegnData(["Warehouse: Combat+WK+Boss"]),
    "Warehouse: Combat+WK+Boss":                     PERegnData(),

    "Museum: NoReqs":                                PERegnData(["Museum: Combat"]),
    "Museum: Combat":                                PERegnData(["Museum: Combat+KK"]),
    "Museum: Combat+KK":                             PERegnData(["Museum: Combat+KK+Boss"]),
    "Museum: Combat+KK+Boss":                        PERegnData(["Cruiser"]),
    "Cruiser":                                       PERegnData(),

    "Chrysler BLDG.: Key 1":                         PERegnData(["Chrysler BLDG.: Key 2"]),
    "Chrysler BLDG.: Key 2":                         PERegnData(["Chrysler BLDG.: Key 3"]),
    "Chrysler BLDG.: Key 3":                         PERegnData(["Chrysler BLDG.: Key 4"]),
    "Chrysler BLDG.: Key 4":                         PERegnData(["Chrysler BLDG.: Key 5"]),
    "Chrysler BLDG.: Key 5":                         PERegnData(["Chrysler BLDG.: Key 6"]),
    "Chrysler BLDG.: Key 6":                         PERegnData(["Chrysler BLDG.: Key 7"]),
    "Chrysler BLDG.: Key 7":                         PERegnData(),
}

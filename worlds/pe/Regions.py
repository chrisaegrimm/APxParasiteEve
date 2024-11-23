from typing import Dict

PERegions: Dict[str, str] = {

    "Title Screen":                               "New York City",

    "New York City":                              "Carnegie Hall: NoReqs",
    "New York City":                              "N.Y.P.D. #17: NoReqs",
    "New York City":                              "Central Park: NoReqs",
    "New York City":                              "Soho: NoReqs",
    "New York City":                              "Hospital: NoReqs",
    "New York City":                              "Chinatown: NoReqs|Combat+GK",
    "New York City":                              "Subway: Combat+PK|GK",
    "New York City":                              "Warehouse: NoReqs",
    "New York City":                              "Museum: NoReqs",
    "New York City":                              "Chrysler BLDG.: Key 1",

    "Carnegie Hall: NoReqs":                      "Carnegie Hall: Combat",
    "Carnegie Hall: Combat":                      "Carnegie Hall: Combat+TK",
    "Carnegie Hall: Combat":                      "Carnegie Hall: Combat+RK",
    "Carnegie Hall: Combat+RK":                   "Carnegie Hall: Combat+RK+Boss",

    "N.Y.P.D. #17: NoReqs":                       "N.Y.P.D. #17: LK",
    "N.Y.P.D. #17: NoReqs":                       "N.Y.P.D. #17: SK",
    "N.Y.P.D. #17: NoReqs":                       "N.Y.P.D. #17: SJ",
    "N.Y.P.D. #17: SJ":                           "N.Y.P.D. #17: Combat+SJ",
    "N.Y.P.D. #17: Combat+SJ":                    "N.Y.P.D. #17: Combat+SJ+Boss",
    "N.Y.P.D. #17: Combat+SJ+Boss":               "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+JunkReq",
    "N.Y.P.D. #17: Combat+SJ+Boss":               "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC",
    "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC": "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+14RTC",

    "Central Park: NoReqs":                       "Central Park: Combat",
    "Central Park: Combat":                       "Central Park: Combat+ZK",
    "Central Park: Combat+ZK":                    "Central Park: Combat+ZK+Boss",

    "Soho: NoReqs":                               "Soho: WM",

    "Hospital: NoReqs":                           "Hospital: Combat",
    "Hospital: Combat":                           "Hospital: Combat+AK",
    "Hospital: Combat":                           "Hospital: Combat+GC",
    "Hospital: Combat":                           "Hospital: Combat+BC",
    "Hospital: Combat+BC":                        "Hospital: Combat+BC+Fuses",
    "Hospital: Combat+BC+Fuses":                  "Hospital: Combat+BC+Fuses+EK+Boss",

    "Chinatown: NoReqs|Combat+GK":                "Chinatown: Combat|Combat+GK",
    "Chinatown: Combat|Combat+GK":                "Chinatown: Combat+Boss|Combat+GK+Boss",
    "Chinatown: Combat|Combat+GK":                "Chinatown: Combat|GK",
    "Chinatown: Combat|GK":                       "Subway: Combat+PK|GK",

    "Subway: Combat+PK|GK":                       "Subway: Combat+PK|Combat+GK",
    "Subway: Combat+PK|Combat+GK":                "Subway: Combat+PK+Boss|Combat+GK+Boss",

    "Warehouse: NoReqs":                          "Warehouse: Combat",
    "Warehouse: Combat":                          "Warehouse: Combat+WK",
    "Warehouse: Combat+WK":                       "Warehouse: Combat+WK+Boss",

    "Museum: NoReqs":                             "Museum: Combat",
    "Museum: Combat":                             "Museum: Combat+KK",
    "Museum: Combat+KK":                          "Museum: Combat+KK+Boss",
    "Museum: Combat+KK+Boss":                     "Cruiser",

    "Chrysler BLDG.: Key 1":                      "Chrysler BLDG.: Key 2",
    "Chrysler BLDG.: Key 2":                      "Chrysler BLDG.: Key 3",
    "Chrysler BLDG.: Key 3":                      "Chrysler BLDG.: Key 4",
    "Chrysler BLDG.: Key 4":                      "Chrysler BLDG.: Key 5",
    "Chrysler BLDG.: Key 5":                      "Chrysler BLDG.: Key 6",
    "Chrysler BLDG.: Key 6":                      "Chrysler BLDG.: Key 7"

}

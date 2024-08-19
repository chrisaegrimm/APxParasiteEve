from typing import Dict

pe_regions: Dict[str, str] = {

    "Title Screen": "World Map",

    "World Map": "Carnegie Hall: NoReqs",
    "World Map": "N.Y.P.D. #17: NoReqs",
    "World Map": "Central Park: NoReqs",
    "World Map": "Soho: NoReqs",
    "World Map": "Hospital: NoReqs",
    "World Map": "Chinatown: NoReqs|Combat+GK",
    "World Map": "Subway: Combat+PK|GK",
    "World Map": "Warehouse: NoReqs",
    "World Map": "Museum: NoReqs",
    "World Map": "Chrysler BLDG.: Key 1",

    "Carnegie Hall: NoReqs": "Carnegie Hall: Combat",
    "Carnegie Hall: Combat": "Carnegie Hall: Combat+TK",
    "Carnegie Hall: Combat": "Carnegie Hall: Combat+RK",
    "Carnegie Hall: Combat+RK": "Carnegie Hall: Combat+RK+Boss",

    "N.Y.P.D. #17: NoReqs": "N.Y.P.D. #17: LK",
    "N.Y.P.D. #17: NoReqs": "N.Y.P.D. #17: SK",
    "N.Y.P.D. #17: NoReqs": "N.Y.P.D. #17: SJ",
    "N.Y.P.D. #17: SJ": "N.Y.P.D. #17: Combat+SJ",
    "N.Y.P.D. #17: Combat+SJ": "N.Y.P.D. #17: Combat+SJ+Boss",
    "N.Y.P.D. #17: Combat+SJ+Boss": "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+JunkReq",
    "N.Y.P.D. #17: Combat+SJ+Boss": "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC",
    "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+12RTC": "N.Y.P.D. #17: Combat+SJ+Boss+UnrChks+14RTC",

    "Central Park: NoReqs": "Central Park: Combat",
    "Central Park: Combat": "Central Park: Combat+ZK",
    "Central Park: Combat+ZK": "Central Park: Combat+ZK+Boss",

    "Soho: NoReqs": "Soho: WM",

    "Hospital: NoReqs": "Hospital: Combat",
    "Hospital: Combat": "Hospital: Combat+AK",
    "Hospital: Combat": "Hospital: Combat+GC",
    "Hospital: Combat": "Hospital: Combat+BC",
    "Hospital: Combat+BC": "Hospital: Combat+BC+Fuses",
    "Hospital: Combat+BC+Fuses": "Hospital: Combat+BC+Fuses+EK+Boss",

    "Chinatown: NoReqs|Combat+GK": "Chinatown: Combat|Combat+GK",
    "Chinatown: Combat|Combat+GK": "Chinatown: Combat+Boss|Combat+GK+Boss",
    "Chinatown: Combat|Combat+GK": "Chinatown: Combat|GK",
    "Chinatown: Combat|GK": "Subway: Combat+PK|GK",

    "Subway: Combat+PK|GK": "Subway: Combat+PK|Combat+GK",
    "Subway: Combat+PK|Combat+GK": "Subway: Combat+PK+Boss|Combat+GK+Boss",

    "Warehouse: NoReqs": "Warehouse: Combat",
    "Warehouse: Combat": "Warehouse: Combat+WK",
    "Warehouse: Combat+WK": "Warehouse: Combat+WK+Boss",

    "Museum: NoReqs": "Museum: Combat",
    "Museum: Combat": "Museum: Combat+KK",
    "Museum: Combat+KK": "Museum: Combat+KK+Boss",
    "Museum: Combat+KK+Boss": "Cruiser",

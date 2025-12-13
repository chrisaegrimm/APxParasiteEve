from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items
if TYPE_CHECKING:
    from .world import PE1World




LOCATION_NAME_TO_ID = {
    "Carnegie Hall - F1 Backstage: Chest": 1,
    "Carnegie Hall - B1 Save Room: Chest": 2,
    "Carnegie Hall - B1 Save Room: Theater Corpse": 3,
    "Carnegie Hall - B1 Diary Room: Diary Key": 4,
    "Carnegie Hall - B1 Diary Room: Closet": 5,
    "Carnegie Hall - B1 Parrot Room: Closet": 6,
    "Carnegie Hall - B1 Clown Locker Room: Locker": 7,
    "Carnegie Hall - B1 Burned Pair Locker Room: Locker": 8,
    "Carnegie Hall - B1 Prop Room: Front Chest": 9,
    "Carnegie Hall - B1 Prop Room: Hidden Chest": 10,
    "Carnegie Hall - B1 Prop Room: Rat Cabinet": 11,
    "Carnegie Hall - B1 Backstage Storage: Chest": 12,
    "Carnegie Hall - Sewers Stairway: Chest": 13,
    "Carnegie Hall - Sewers Ghost Girl: Back Left Chest": 14,
    "Carnegie Hall - Sewers Ghost Girl: Back Right Chest": 15,
    "Carnegie Hall - Sewers Ghost Girl: Front Left Chest": 16,
    "Carnegie Hall - Sewers Hidden Chest Room: Left Chest": 17,
    "Carnegie Hall - Sewers Hidden Chest Room: Center Chest": 18,
    "Carnegie Hall - Sewers Hidden Chest Room: Right Chest": 19,
    "Carnegie Hall - Sewers Hidden Chest Room: Valve Chest": 20,
    "Carnegie Hall - Sewers Alligator: Boss Drop": 21,

    "N.Y.P.D. #17 - D2 1F Baker's Office: Baker Permit 1": 22,
    "N.Y.P.D. #17 - D2 1F Locker Room: Right Locker": 23,
    "N.Y.P.D. #17 - D2 1F Locker Room: Center Locker": 24,
    "N.Y.P.D. #17 - D2 1F Conference Room: Baker Permit 2": 25,
    "N.Y.P.D. #17 - D2 B1 Weapons Department: M16A1": 26,
    "N.Y.P.D. #17 - D3 1F Entrance: Maeda's Hamaya": 27,
    "N.Y.P.D. #17 - D3 1F Main Hall: Cop's Ammo": 28,
    "N.Y.P.D. #17 - D3 1F Main Hall: Nix's Ammo": 29,
    "N.Y.P.D. #17 - D3 1F Save Room: Warner's Ammo": 30,
    "N.Y.P.D. #17 - D3 1F Locker Room: Right Locker": 31,
    "N.Y.P.D. #17 - D3 1F Locker Room: Cop's Ammo": 32,
    "N.Y.P.D. #17 - D2 1F Locker Room: Locked Locker": 33,
    "N.Y.P.D. #17 - D3 B1 Weapons Department: Torres's Gun": 34,
    "N.Y.P.D. #17 - D3 B1 Kennel: Cathy's Ammo": 35,
    "N.Y.P.D. #17 - D3 1F Conference Room: Spider Chest": 36,
    "N.Y.P.D. #17 - D3 2F Barred Staircase: Cop's Ammo": 37,
    "N.Y.P.D. #17 - D3 2F Holding Cells: Left Chest": 38,
    "N.Y.P.D. #17 - D3 2F Holding Cells: Right Chest": 39,
    "N.Y.P.D. #17 - D3 2F Interrogation Room: Chest": 40,
    "N.Y.P.D. #17 - D3 2F Interrogation Room: Table Sparkle": 41,
    "N.Y.P.D. #17 - D3 2F Save Office: Desk Chest": 42,
    "N.Y.P.D. #17 - D3 2F Save Office: Floor Chest": 43,
    "N.Y.P.D. #17 - D3 3F Ambush Hall: Cop's Locker Key": 44,
    "N.Y.P.D. #17 - D4 3F Medical Office: Daniel's Ammo": 45,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Boss Drop": 46,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Chest": 47,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Cop's Ammo": 48,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf's Backroom: Chest": 49,
    "N.Y.P.D. #17 - D2 B1 Weapons Storage: Left Chest": 50,
    "N.Y.P.D. #17 - D2 B1 Weapons Storage: Center Chest": 51,
    "N.Y.P.D. #17 - D2 B1 Weapons Storage: Right Chest": 52,
    "N.Y.P.D. #17 - D3 3F Kerberos: Boss Drop": 53,
    "N.Y.P.D. #17 - D4 B1 Weapons Department: Leave It to Wayne": 54,
    "N.Y.P.D. #17 - D4 B1 Weapons Department: Tool Kit": 55,
    "N.Y.P.D. #17 - D4 B1 Weapons Department: Super Tool Kit": 56,

    "Central Park - Entrance: Car Chest": 57,
    "Central Park - Entrance: Snake Chest": 58,
    "Central Park - Front Gate: Left Chest": 59,
    "Central Park - Front Gate: Right Chest": 60,
    "Central Park - Courtyard: Left Gun Chest": 61,
    "Central Park - Courtyard: Right Tool Chest": 62,
    "Central Park - Office: Key Drawer": 63,
    "Central Park - Office: Cabinet": 64,
    "Central Park - Office: Locked Cupboard": 65,
    "Central Park - Snake Exhibit: Upper Right Chest": 66,
    "Central Park - Snake Exhibit: Lower Left Chest": 67,
    "Central Park - Snake Exhibit: Lower Right Chest": 68,
    "Central Park - Back Courtyard: Ammo Chest": 69,
    "Central Park - Figure 8: Right Chest": 70,
    "Central Park - Figure 8: Left Chest": 71,
    "Central Park - Gazebo: Left Chest": 72,
    "Central Park - Gazebo: Right Chest": 73,
    "Central Park - Behind Gazebo (Save): Chest": 74,
    "Central Park - Forest Maze West: Mythical Tool Chest": 75,
    "Central Park - Forest Maze Bridge: Chest": 76,
    "Central Park - Forest Maze Dock: Chest": 77,
    "Central Park - Forest Maze East: Backup Tool Chest": 78,
    "Central Park - Under Bush Bridge: Left Stat Chest": 79,
    "Central Park - Under Bush Bridge: Right YOLO Tool Chest": 80,
    "Central Park - Carriage Eve: Boss Drop": 81,

    "Soho - Apartment Interior: Chest": 82,
    "Soho - Apartment Exterior: Trash Card": 83,
    "Soho - Pharmacy: Aisle 3 Medicine Chest": 84,
    "Soho - Pharmacy: Aisle 5 Revive Chest": 85,
    "Soho - Pharmacy: Backroom Left Chest": 86,
    "Soho - Pharmacy: Backroom Right Chest": 87,
    "Soho - Pharmacy: Aisle 1 Left Shelf": 88,
    "Soho - Pharmacy: Aisle 3 Far Back Shelf": 89,
    "Soho - Pharmacy: Behind Phone Counter": 90,
    "Soho - Pharmacy: Aisle 4 Right Shelf": 91,
    "Soho - Sam's Gun Shop: Upper Left Chest": 92,
    "Soho - Sam's Gun Shop: Upper Right Chest": 93,
    "Soho - Sam's Gun Shop: Behind Counter Chest": 94,
    "Soho - Sam's Gun Shop: Lower Right Chest": 95,
    "Soho - Sam's Gun Shop: Green Box": 96,
    "Soho - Sam's Gun Shop: Red Box": 97,
    "Soho - Sam's Gun Shop: Shotgun Rack": 98,
    "Soho - Sam's Gun Shop: Rifle Rack": 99,

    "Hospital - 1F Outside: Maeda's Mayoke": 100,
    "Hospital - 1F Lobby: Corner Ammo Chest": 101,
    "Hospital - 1F Lobby: Closet Chest": 102,
    "Hospital - 1F Emergency Room: Chest": 103,
    "Hospital - 1F Flashback Room: Chest": 104,
    "Hospital - 1F Flashback Room: Nurse": 105,
    "Hospital - 1F Green Hallway: Chest": 106,
    "Hospital - 1F Nitrogen Storage: King Bacterium Drop": 107,
    "Hospital - 1F Nitrogen Storage: Chest": 108,
    "Hospital - B1 Storage: Upper Chest": 109,
    "Hospital - B1 Storage: Lower Chest": 110,
    "Hospital - B1 Storage: Shelf Fuse Sparkle": 111,
    "Hospital - B1 Save Office: Chest": 112,
    "Hospital - B1 Save Office: Key Drawer": 113,
    "Hospital - B1 Morgue: Chest": 114,
    "Hospital - B1 Autopsy: Lower Chest": 115,
    "Hospital - B1 Autopsy: Upper Chest": 116,
    "Hospital - B1 Crematory: Corner Chest": 117,
    "Hospital - B1 Crematory: Fuse Sparkle": 118,
    "Hospital - B1 Crematory: Cardkey Corpse": 119,
    "Hospital - B1 Blue Hallway: 50/50 Chest": 120,
    "Hospital - B1 Collapsed Back Stairway: Sparkle": 121,
    "Hospital - B1 Sterilization Room: Left Chest": 122,
    "Hospital - B1 Sterilization Room: Right Chest": 123,
    "Hospital - B1 Sterilization Room: Fuse Sparkle": 124,
    "Hospital - 13F Research Lab: Chest": 125,
    "Hospital - 13F Research Lab: Counter": 126,
    "Hospital - 13F Research Lab: Shelf": 127,
    "Hospital - 13F Kennel: Chest": 128,
    "Hospital - 13F Roof Elevator Access: Lower Chest": 129,
    "Hospital - 13F Roof Elevator Access: Upper Chest": 130,
    "Hospital - 13F Roof Elevator Access: Upper Sparkle": 131,
    "Hospital - 13F Roof Elevator Access: Lower Sparkle": 132,
    "Hospital - Roof Spiderwoman: Boss Drop": 133,

    "Chinatown - Near Entrance: Left Chest": 134,
    "Chinatown - Near Entrance: Right Chest": 135,
    "Chinatown - Antique Shop Exterior (Save): Lower Chest": 136,
    "Chinatown - Antique Shop Exterior (Save): Upper Chest": 137,
    "Chinatown - Antique Shop Interior: Chest": 138,
    "Chinatown - Antique Shop Interior: Shelf": 139,
    "Chinatown - End of the Street: Maeda's Narita": 140,
    "Chinatown - End of the Street: Chest": 141,
    "Chinatown - Sewers Labyrinth A-04: Super Tool Sparkle": 142,
    "Chinatown - Sewers Labyrinth B-01: Medicine 4 Chest": 143,
    "Chinatown - Sewers Labyrinth B-03: Cure-D Sparkle": 144,
    "Chinatown - Sewers Labyrinth B-06: Ammo Chest": 145,
    "Chinatown - Sewers Labyrinth C-02: Cr Protector Chest": 146,
    "Chinatown - Sewers Labyrinth C-06: Range Sparkle": 147,
    "Chinatown - Sewers Labyrinth D-03: M203-3 Chest": 148,
    "Chinatown - Sewers Labyrinth D-08: M870 Chest": 149,
    "Chinatown - Sewers Labyrinth D-11: Off or Def Chest": 150,
    "Chinatown - Sewers Labyrinth E-04: Medicine 3 Chest": 151,
    "Chinatown - Sewers Labyrinth E-10: Tool Sparkle": 152,
    "Chinatown - Sewers Labyrinth F-09: Offense Chest": 153,
    "Chinatown - Sewers Exit Catwalk: Club 3 Chest": 154,
    "Chinatown - Pump Station Exterior: Alligator Chest": 155,
    "Chinatown - Pump Station Exterior: Catwalk Chest": 156,
    "Chinatown - Pump Station Control Room: Chest": 157,

    "Subway - Platform (Save): Bench Chest": 158,
    "Subway - Platform (Save): Phone Chest": 159,
    "Subway - Exit Stairway: Chest": 160,
    "Subway - Left Mole Tunnel: Chest": 161,
    "Subway - Centipede: Boss Drop": 162,
    "Subway - Parked Passenger Car: Right Chest": 163,
    "Subway - Parked Passenger Car: Left Chest": 164,
    "Subway - Parked Passenger Car: Lower Chest": 165,
    "Subway - Bridge: Cop's Gate Key": 166,

    "Warehouse - Outside: Left Chest (Hidden)": 167,
    "Warehouse - Outside: Right Chest": 168,
    "Warehouse - Entrance: Forklift Chest": 169,
    "Warehouse - Tom and Jerry: Chest": 170,
    "Warehouse - Tom and Jerry: Key Sparkle": 171,
    "Warehouse - Save Room: Ladder Chest": 172,
    "Warehouse - Save Room: Upper Ground Chest": 173,
    "Warehouse - Save Room: Lower Ground Chest": 174,
    "Warehouse - Before Descent: Lower Left Chest": 175,
    "Warehouse - Before Descent: Upper Left Chest": 176,
    "Warehouse - Before Descent: Upper Right Chest": 177,
    "Warehouse - Giant Enemy Crab: Boss Drop": 178,
    "Warehouse - Giant Enemy Crab: Steamed Tool": 179,

    "Museum - 1F Klamp Pursuit East Exhibit: Chest": 180,
    "Museum - 1F Klamp Pursuit West Exhibit: Chest": 181,
    "Museum - 1F Klamp Pursuit Troodon Hall: Right Chest": 182,
    "Museum - 1F Klamp Pursuit Troodon Hall: Left Chest": 183,
    "Museum - 1F Rainforest Exhibit: Quiz": 184,
    "Museum - 1F Rainforest Employee Hallway: Quiz": 185,
    "Museum - 1F Rainforest Employee Hallway: Chest": 186,
    "Museum - 1F Rainforest Storage Room: Lower Right Chest": 187,
    "Museum - 1F Rainforest Storage Room: Lower Center Chest": 188,
    "Museum - 1F Rainforest Storage Room: Upper Chest": 189,
    "Museum - 1F Rainforest Storage Room: Hidden Closet Right Chest": 190,
    "Museum - 1F Rainforest Storage Room: Hidden Closet Left Chest": 191,
    "Museum - 1F Stingy Scorpion Hall: Quiz": 192,
    "Museum - 1F Tribal Staircase: Chest": 193,
    "Museum - 1F Stone Head Room: Ladder Access Chest": 194,
    "Museum - 1F Fire Escape: Stat Chest": 195,
    "Museum - 2F Gemstone Staircase: Quiz": 196,
    "Museum - 2F Gemstone Staircase: Right Chest": 197,
    "Museum - 2F Gemstone Staircase: Left Chest": 198,
    "Museum - 3F Fire Escape: Rocket Chest": 199,
    "Museum - 3F Hall of Evolution: Quiz": 200,
    "Museum - 2F Festive Lobby: Revive Chest": 201,
    "Museum - 3F Pterodactyl Ambush Hall: Chest": 202,
    "Museum - 3F Stegosaurus Room: Chest": 203,
    "Museum - 2F Museum Shop Tents: Upper Chest": 204,
    "Museum - 2F Museum Shop Tents: Lower Chest": 205,
    "Museum - 2F Security Office: Chest": 206,
    "Museum - 4F Security Storage: Lower Right Chest": 207,
    "Museum - 4F Security Storage: Lower Left Chest": 208,
    "Museum - 4F Security Storage: Upper Left Chest": 209,
    "Museum - 4F Security Storage: Center Chest": 210,
    "Museum - 2F Klamp's Office: Maeda's Gun": 211,
    "Museum - 2F Klamp's Office: Klamp's Key": 212,
    "Museum - 4F Forgotten Landing: Full Recover Chest": 213,
    "Museum - 3F Triceratops: Boss Drop": 214,
    "Museum - 1F T-Rex: Left Chest": 215,
    "Museum - 1F T-Rex: Right Chest": 216,
    "Museum - 1F T-Rex: Boss Drop": 217,
    "Museum - 2F Glass Exhibit Near Chocobo: Quiz": 218,
    "Museum - 2F Glass Exhibit Near Chocobo: Left Chest Behind Glass": 219,
    "Museum - 2F Glass Exhibit Near Chocobo: Right Chest Behind Glass": 220,
    "Museum - 3F Final Approach: Quiz": 221,
    "Museum - 3F Final Approach: Right Chest Behind Glass": 222,
    "Museum - 3F Final Approach: Left Chest Behind Glass": 223,

    "Cruiser - Deck: Daniel's Sacrifice": 224,

    "Chrysler BLDG. - Treasurebox Set 1-01: Offense": 301,
    "Chrysler BLDG. - Treasurebox Set 1-01: Cr Evade": 302,
    "Chrysler BLDG. - Treasurebox Set 1-01: Tool": 303,
    "Chrysler BLDG. - Treasurebox Set 1-01: USP-2": 304,
    "Chrysler BLDG. - Treasurebox Set 1-02: Tool A": 305,
    "Chrysler BLDG. - Treasurebox Set 1-02: M1911A4": 306,
    "Chrysler BLDG. - Treasurebox Set 1-02: Tool B": 307,
    "Chrysler BLDG. - Treasurebox Set 1-02: Sp Vest 2": 308,
    "Chrysler BLDG. - Treasurebox Set 1-03: M16A2": 309,
    "Chrysler BLDG. - Treasurebox Set 1-03: Tool": 310,
    "Chrysler BLDG. - Treasurebox Set 1-03: Cr Evade": 311,
    "Chrysler BLDG. - Treasurebox Set 1-04: PE": 312,
    "Chrysler BLDG. - Treasurebox Set 1-04: Kv Jacket": 313,
    "Chrysler BLDG. - Treasurebox Set 1-04: M79-4": 314,
    "Chrysler BLDG. - Treasurebox Set 1-05: P38 T Card": 315,
    "Chrysler BLDG. - Treasurebox Set 1-05: P228": 316,
    "Chrysler BLDG. - Treasurebox Set 1-05: PE": 317,
    "Chrysler BLDG. - Treasurebox Set 1-05: Cr Evade": 318,
    "Chrysler BLDG. - Treasurebox Set 1-06: Sv Jacket": 319,
    "Chrysler BLDG. - Treasurebox Set 1-06: Cr Evade": 320,
    "Chrysler BLDG. - Treasurebox Set 1-07: PE": 321,
    "Chrysler BLDG. - Treasurebox Set 1-07: P226": 322,
    "Chrysler BLDG. - Treasurebox Set 1-07: Defense": 323,
    "Chrysler BLDG. - Treasurebox Set 1-08: Range": 324,
    "Chrysler BLDG. - Treasurebox Set 1-08: Bullet Cap": 325,
    "Chrysler BLDG. - Treasurebox Set 1-08: Rocket": 326,
    "Chrysler BLDG. - Treasurebox Set 1-08: Tool": 327,
    "Chrysler BLDG. - Treasurebox Set 1-09: Bullet Cap": 328,
    "Chrysler BLDG. - Treasurebox Set 1-09: Offense A": 329,
    "Chrysler BLDG. - Treasurebox Set 1-09: Offense B": 330,
    "Chrysler BLDG. - 10F Spiderwoman EX: Boss Drop": 331,
    "Chrysler BLDG. - Treasurebox Set 2-01: Cr Jacket": 332,
    "Chrysler BLDG. - Treasurebox Set 2-01: Defense": 333,
    "Chrysler BLDG. - Treasurebox Set 2-02: Tool": 334,
    "Chrysler BLDG. - Treasurebox Set 2-03: Tool A": 335,
    "Chrysler BLDG. - Treasurebox Set 2-03: Tool B": 336,
    "Chrysler BLDG. - Treasurebox Set 2-03: M203-5": 337,
    "Chrysler BLDG. - Treasurebox Set 2-04: Tool": 338,
    "Chrysler BLDG. - Treasurebox Set 2-04: M96": 339,
    "Chrysler BLDG. - Treasurebox Set 2-04: Bullet Cap": 340,
    "Chrysler BLDG. - Treasurebox Set 2-05: Kasul T Card": 341,
    "Chrysler BLDG. - Treasurebox Set 2-05: Offense": 342,
    "Chrysler BLDG. - Treasurebox Set 2-05: Rocket": 343,
    "Chrysler BLDG. - Treasurebox Set 2-06: Super Tool": 344,
    "Chrysler BLDG. - Treasurebox Set 2-06: Club 4": 345,
    "Chrysler BLDG. - Treasurebox Set 2-06: Defense": 346,
    "Chrysler BLDG. - Treasurebox Set 2-07: AM44": 347,
    "Chrysler BLDG. - Treasurebox Set 2-07: P229": 348,
    "Chrysler BLDG. - Treasurebox Set 2-08: PE": 349,
    "Chrysler BLDG. - Treasurebox Set 2-08: Sp Suit 1": 350,
    "Chrysler BLDG. - Treasurebox Set 2-09: Full UZ": 351,
    "Chrysler BLDG. - Treasurebox Set 2-09: Range": 352,
    "Chrysler BLDG. - Treasurebox Set 2-09: Bhawk T Card": 353,
    "Chrysler BLDG. - Treasurebox Set 2-10: Kv Suit 1": 354,
    "Chrysler BLDG. - Treasurebox Set 2-10: Tool": 355,
    "Chrysler BLDG. - 20F Alligators EX: Boss Drops": 356,
    "Chrysler BLDG. - Treasurebox Set 3-01: Tool": 357,
    "Chrysler BLDG. - Treasurebox Set 3-02: Tool A": 358,
    "Chrysler BLDG. - Treasurebox Set 3-02: PPKS T Card": 359,
    "Chrysler BLDG. - Treasurebox Set 3-02: Tool B": 360,
    "Chrysler BLDG. - Treasurebox Set 3-03: Bullet Cap": 361,
    "Chrysler BLDG. - Treasurebox Set 3-03: Tool": 362,
    "Chrysler BLDG. - Treasurebox Set 3-03: Super Tool": 363,
    "Chrysler BLDG. - Treasurebox Set 3-04: Super Tool": 364,
    "Chrysler BLDG. - Treasurebox Set 3-04: Cr Evade": 365,
    "Chrysler BLDG. - Treasurebox Set 3-04: Mark 23": 366,
    "Chrysler BLDG. - Treasurebox Set 3-05: Offense": 367,
    "Chrysler BLDG. - Treasurebox Set 3-05: Tool": 368,
    "Chrysler BLDG. - Treasurebox Set 3-05: M870-2": 369,
    "Chrysler BLDG. - Treasurebox Set 3-06: Type64": 370,
    "Chrysler BLDG. - Treasurebox Set 3-06: Defense": 371,
    "Chrysler BLDG. - Treasurebox Set 3-07: Cm Jacket": 372,
    "Chrysler BLDG. - Treasurebox Set 3-08: B Jacket 2": 373,
    "Chrysler BLDG. - Treasurebox Set 3-08: M1 T Card": 374,
    "Chrysler BLDG. - Treasurebox Set 3-08: Offense": 375,
    "Chrysler BLDG. - Treasurebox Set 3-09: Range": 376,
    "Chrysler BLDG. - Treasurebox Set 3-09: Cr Evade": 377,
    "Chrysler BLDG. - Treasurebox Set 3-10: Tool": 378,
    "Chrysler BLDG. - Treasurebox Set 3-10: Sv Suit 1": 379,
    "Chrysler BLDG. - Treasurebox Set 3-10: M79-5": 380,
    "Chrysler BLDG. - 30F Centipede EX: Boss Drop": 381,
    "Chrysler BLDG. - Treasurebox Set 4-01: PSG-1": 382,
    "Chrysler BLDG. - Treasurebox Set 4-01: Tool": 383,
    "Chrysler BLDG. - Treasurebox Set 4-01: Full Cure": 384,
    "Chrysler BLDG. - Treasurebox Set 4-01: Bullet Cap": 385,
    "Chrysler BLDG. - Treasurebox Set 4-02: Cm Suit 1": 386,
    "Chrysler BLDG. - Treasurebox Set 4-02: Tool": 387,
    "Chrysler BLDG. - Treasurebox Set 4-02: Full Recover": 388,
    "Chrysler BLDG. - Treasurebox Set 4-03: Tool": 389,
    "Chrysler BLDG. - Treasurebox Set 4-03: Rocket": 390,
    "Chrysler BLDG. - Treasurebox Set 4-03: Defense": 391,
    "Chrysler BLDG. - Treasurebox Set 4-03: Sv Suit 2": 392,
    "Chrysler BLDG. - Treasurebox Set 4-04: MP5A5": 393,
    "Chrysler BLDG. - Treasurebox Set 4-04: MK5 T Card": 394,
    "Chrysler BLDG. - Treasurebox Set 4-04: Sp Armor 1": 395,
    "Chrysler BLDG. - Treasurebox Set 4-04: BAR T Card": 396,
    "Chrysler BLDG. - Treasurebox Set 4-05: Tool": 397,
    "Chrysler BLDG. - Treasurebox Set 4-06: MP44 T Card": 398,
    "Chrysler BLDG. - Treasurebox Set 4-07: MG42 T Card": 399,
    "Chrysler BLDG. - Treasurebox Set 4-07: Cr Evade": 400,
    "Chrysler BLDG. - Treasurebox Set 4-07: M1911A5": 401,
    "Chrysler BLDG. - Treasurebox Set 4-07: Defense": 402,
    "Chrysler BLDG. - Treasurebox Set 4-08: Maverick": 403,
    "Chrysler BLDG. - Treasurebox Set 4-08: Range": 404,
    "Chrysler BLDG. - Treasurebox Set 4-09: Kv Armor 1": 405,
    "Chrysler BLDG. - Treasurebox Set 4-10: Tool": 406,
    "Chrysler BLDG. - 40F Triceratops EX: Boss Drop": 407,
    "Chrysler BLDG. - Treasurebox Set 5-01: SAR": 408,
    "Chrysler BLDG. - Treasurebox Set 5-01: Tool": 409,
    "Chrysler BLDG. - Treasurebox Set 5-01: M29 T Card": 410,
    "Chrysler BLDG. - Treasurebox Set 5-02: M73 T Card": 411,
    "Chrysler BLDG. - Treasurebox Set 5-02: PE": 412,
    "Chrysler BLDG. - Treasurebox Set 5-02: Super Tool": 413,
    "Chrysler BLDG. - Treasurebox Set 5-02: AT4-1": 414,
    "Chrysler BLDG. - Treasurebox Set 5-03: Tool": 415,
    "Chrysler BLDG. - Treasurebox Set 5-03: Bullet Cap": 416,
    "Chrysler BLDG. - Treasurebox Set 5-04: Cr Suit 1": 417,
    "Chrysler BLDG. - Treasurebox Set 5-05: USP-3": 418,
    "Chrysler BLDG. - Treasurebox Set 5-06: Offense": 419,
    "Chrysler BLDG. - Treasurebox Set 5-06: Rocket": 420,
    "Chrysler BLDG. - Treasurebox Set 5-06: Cm Armor 1": 421,
    "Chrysler BLDG. - Treasurebox Set 5-06: Tool": 422,
    "Chrysler BLDG. - Treasurebox Set 5-06: Range": 423,
    "Chrysler BLDG. - Treasurebox Set 5-07: Tool": 424,
    "Chrysler BLDG. - Treasurebox Set 5-08: B Suit 1": 425,
    "Chrysler BLDG. - Treasurebox Set 5-09: G20": 426,
    "Chrysler BLDG. - Treasurebox Set 5-09: Tool": 427,
    "Chrysler BLDG. - Treasurebox Set 5-09: Offense": 428,
    "Chrysler BLDG. - Treasurebox Set 5-09: Sv Armor 1": 429,
    "Chrysler BLDG. - 50F Cockroach: Boss Drop": 430,
    "Chrysler BLDG. - Treasurebox Set 6-01: Type38 T Card": 431,
    "Chrysler BLDG. - Treasurebox Set 6-01: Cr Evade": 432,
    "Chrysler BLDG. - Treasurebox Set 6-01: Sp Armor 2": 433,
    "Chrysler BLDG. - Treasurebox Set 6-02: Rocket": 434,
    "Chrysler BLDG. - Treasurebox Set 6-02: MP5SD6": 435,
    "Chrysler BLDG. - Treasurebox Set 6-03: B Suit 2": 436,
    "Chrysler BLDG. - Treasurebox Set 6-04: M712": 437,
    "Chrysler BLDG. - Treasurebox Set 6-05: S12": 438,
    "Chrysler BLDG. - Treasurebox Set 6-05: PE": 439,
    "Chrysler BLDG. - Treasurebox Set 6-05: Full Recover": 440,
    "Chrysler BLDG. - Treasurebox Set 6-05: Cr Armor 1": 441,
    "Chrysler BLDG. - Treasurebox Set 6-06: Full Cure": 442,
    "Chrysler BLDG. - Treasurebox Set 6-07: FA-MAS": 443,
    "Chrysler BLDG. - Treasurebox Set 6-08: Range": 444,
    "Chrysler BLDG. - Treasurebox Set 6-09: Tool A": 445,
    "Chrysler BLDG. - Treasurebox Set 6-09: Tool B": 446,
    "Chrysler BLDG. - Treasurebox Set 6-09: Tool C": 447,
    "Chrysler BLDG. - 60F Giant Enemy Crab EX: Boss Drop": 448,
    "Chrysler BLDG. - Treasurebox Set 7-01: PE": 449,
    "Chrysler BLDG. - Treasurebox Set 7-01: M500-2": 450,
    "Chrysler BLDG. - Treasurebox Set 7-01: Full Recover": 451,
    "Chrysler BLDG. - Treasurebox Set 7-01: M500": 452,
    "Chrysler BLDG. - Treasurebox Set 7-02: Defense": 453,
    "Chrysler BLDG. - Treasurebox Set 7-03: XM177E2": 454,
    "Chrysler BLDG. - Treasurebox Set 7-03: Tool": 455,
    "Chrysler BLDG. - Treasurebox Set 7-03: Range": 456,
    "Chrysler BLDG. - Treasurebox Set 7-03: Full Cure": 457,
    "Chrysler BLDG. - Treasurebox Set 7-04: Super Tool": 458,
    "Chrysler BLDG. - Treasurebox Set 7-04: Cm Armor 2": 459,
    "Chrysler BLDG. - Treasurebox Set 7-04: Bullet Cap": 460,
    "Chrysler BLDG. - Treasurebox Set 7-05: B Armor": 461,
    "Chrysler BLDG. - Treasurebox Set 7-05: M96R": 462,
    "Chrysler BLDG. - Treasurebox Set 7-05: Super Tool": 463,
    "Chrysler BLDG. - Treasurebox Set 7-05: Tool": 464,
    "Chrysler BLDG. - Treasurebox Set 7-06: Type3 T Card": 465,
    "Chrysler BLDG. - Treasurebox Set 7-07: M203-6": 466,
    "Chrysler BLDG. - Treasurebox Set 7-07: Offense": 467,
    "Chrysler BLDG. - Treasurebox Set 7-07: Sv Armor 2": 468,
    "Chrysler BLDG. - Treasurebox Set 7-08: Eagle T Card": 469,
    "Chrysler BLDG. - Treasurebox Set 7-08: PE": 470,
    "Chrysler BLDG. - Treasurebox Set 7-08: Club 5": 471,
    "Chrysler BLDG. - Treasurebox Set 7-08: Cr Armor 2": 472,
    "Chrysler BLDG. - 70F Queen Bee: Boss Drop": 473,
    "Chrysler BLDG. - 77F Spire: Maya": 474
}


class PE1Location(Location):
    game = "Parasite Eve"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: PE1World) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: PE1World) -> None:

    manhattan = world.get_region("Manhattan (World Map)")

    ch_norq = world.get_region("Carnegie Hall: NoRq")
    ch_cmbt = world.get_region("Carnegie Hall: Cmbt")
    ch_cmbt_tk = world.get_region("Carnegie Hall: Cmbt+TK")
    ch_cmbt_rk = world.get_region("Carnegie Hall: Cmbt+RK")
    ch_boss_rk = world.get_region("Carnegie Hall: Boss+RK")

    pd_norq = world.get_region("N.Y.P.D. #17: NoRq")
    pd_lk = world.get_region("N.Y.P.D. #17: LK")
    pd_sk = world.get_region("N.Y.P.D. #17: SK")
    pd_sj = world.get_region("N.Y.P.D. #17: SJ")
    pd_cmbt_sj = world.get_region("N.Y.P.D. #17: Cmbt+SJ")
    pd_boss_sj = world.get_region("N.Y.P.D. #17: Boss+SJ")
    pd_boss_sj_junk = world.get_region("N.Y.P.D. #17: Boss+SJ+Junk")
    pd_boss_sj_12rt = world.get_region("N.Y.P.D. #17: Boss+SJ+12RT")
    pd_boss_sj_14rt = world.get_region("N.Y.P.D. #17: Boss+SJ+14RT")

    cp_norq = world.get_region("Central Park: NoRq")
    cp_cmbt = world.get_region("Central Park: Cmbt")
    cp_cmbt_zk = world.get_region("Central Park: Cmbt+ZK")
    cp_boss_zk = world.get_region("Central Park: Boss+ZK")

    sh_norq = world.get_region("Soho: NoRq")
    sh_wm = world.get_region("Soho: WM")

    hs_norq = world.get_region("Hospital: NoRq")
    hs_gc = world.get_region("Hospital: GC")
    hs_bc = world.get_region("Hospital: BC")
    hs_cmbt = world.get_region("Hospital: Cmbt")
    hs_cmbt_gc = world.get_region("Hospital: Cmbt+GC")
    hs_cmbt_ak = world.get_region("Hospital: Cmbt+AK")
    hs_cmbt_bc = world.get_region("Hospital: Cmbt+BC")
    hs_cmbt_bc_3f = world.get_region("Hospital: Cmbt+BC+3F")
    hs_boss_bc_3f_ek = world.get_region("Hospital: Boss+BC+3F+EK")

    ct_norq_or_cmbt_gk = world.get_region("Chinatown: NoRq|Cmbt+GK")
    ct_cmbt_or_cmbt_gk = world.get_region("Chinatown: Cmbt|Cmbt+GK")
    ct_boss_or_boss_gk = world.get_region("Chinatown: Boss|Boss+GK")
    ct_cmbt_or_gk = world.get_region("Chinatown: Cmbt|GK")

    sw_cmbt_pk_or_gk = world.get_region("Subway: Cmbt+PK|GK")
    sw_cmbt_pk_or_cmbt_gk = world.get_region("Subway: Cmbt+PK|Cmbt+GK")
    sw_boss_pk_or_boss_gk = world.get_region("Subway: Boss+PK|Boss+GK")

    wh_norq = world.get_region("Warehouse: NoRq")
    wh_cmbt = world.get_region("Warehouse: Cmbt")
    wh_cmbt_wk = world.get_region("Warehouse: Cmbt+WK")
    wh_boss_wk = world.get_region("Warehouse: Boss+WK")

    mu_norq = world.get_region("Museum: NoRq")
    mu_cmbt = world.get_region("Museum: Cmbt")
    mu_cmbt_kk = world.get_region("Museum: Cmbt+KK")
    mu_boss_kk = world.get_region("Museum: Boss+KK")

    liberty = world.get_region("Statue of Liberty: Boss")
    cruiser = world.get_region("Cruiser: Boss")

    cb_k1 = world.get_region("Chrysler BLDG.: Key 1")
    cb_k2 = world.get_region("Chrysler BLDG.: Key 2")
    cb_k3 = world.get_region("Chrysler BLDG.: Key 3")
    cb_k4 = world.get_region("Chrysler BLDG.: Key 4")
    cb_k5 = world.get_region("Chrysler BLDG.: Key 5")
    cb_k6 = world.get_region("Chrysler BLDG.: Key 6")
    cb_k7 = world.get_region("Chrysler BLDG.: Key 7")
    cb_spire = world.get_region("Chrysler BLDG.: Spire")




    ch_norq_locations = get_location_names_with_ids(
        [
        "Carnegie Hall - F1 Backstage: Chest"
        ]
    )
    ch_norq.add_locations(ch_norq_locations, PE1Location)

    ch_cmbt_locations = get_location_names_with_ids(
        [
        "Carnegie Hall - B1 Save Room: Chest",
        "Carnegie Hall - B1 Save Room: Theater Corpse",
        "Carnegie Hall - B1 Clown Locker Room: Locker",
        "Carnegie Hall - B1 Burned Pair Locker Room: Locker"
        ]
    )
    ch_cmbt.add_locations(ch_cmbt_locations, PE1Location)

    ch_cmbt_tk_locations = get_location_names_with_ids(
        [
        "Carnegie Hall - B1 Diary Room: Diary Key",
        "Carnegie Hall - B1 Diary Room: Closet",
        "Carnegie Hall - B1 Parrot Room: Closet",
        "Carnegie Hall - B1 Prop Room: Front Chest",
        "Carnegie Hall - B1 Prop Room: Hidden Chest",
        "Carnegie Hall - B1 Prop Room: Rat Cabinet",
        "Carnegie Hall - B1 Backstage Storage: Chest"
        ]
    )
    ch_cmbt_tk.add_locations(ch_cmbt_tk_locations, PE1Location)

    ch_cmbt_rk_locations = get_location_names_with_ids(
        [
        "Carnegie Hall - Sewers Stairway: Chest",
        "Carnegie Hall - Sewers Ghost Girl: Back Left Chest",
        "Carnegie Hall - Sewers Ghost Girl: Back Right Chest",
        "Carnegie Hall - Sewers Ghost Girl: Front Left Chest",
        "Carnegie Hall - Sewers Hidden Chest Room: Left Chest",
        "Carnegie Hall - Sewers Hidden Chest Room: Center Chest",
        "Carnegie Hall - Sewers Hidden Chest Room: Right Chest",
        "Carnegie Hall - Sewers Hidden Chest Room: Valve Chest"
        ]
    )
    ch_cmbt_rk.add_locations(ch_cmbt_rk_locations, PE1Location)

    ch_boss_rk_locations = get_location_names_with_ids(
        [
        "Carnegie Hall - Sewers Alligator: Boss Drop"
        ]
    )
    ch_boss_rk.add_locations(ch_boss_rk_locations, PE1Location)

    pd_norq_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D2 1F Baker's Office: Baker Permit 1",
        "N.Y.P.D. #17 - D2 1F Locker Room: Right Locker",
        "N.Y.P.D. #17 - D2 1F Locker Room: Center Locker",
        "N.Y.P.D. #17 - D2 1F Conference Room: Baker Permit 2",
        "N.Y.P.D. #17 - D2 B1 Weapons Department: M16A1"
        ]
    )
    pd_norq.add_locations(pd_norq_locations, PE1Location)

    pd_lk_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D2 1F Locker Room: Locked Locker"
        ]
    )
    pd_lk.add_locations(pd_lk_locations, PE1Location)

    pd_sk_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D2 B1 Weapons Storage: Left Chest",
        "N.Y.P.D. #17 - D2 B1 Weapons Storage: Center Chest",
        "N.Y.P.D. #17 - D2 B1 Weapons Storage: Right Chest"
        ]
    )
    pd_sk.add_locations(pd_sk_locations, PE1Location)

    pd_sj_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D3 1F Entrance: Maeda's Hamaya",
        "N.Y.P.D. #17 - D3 1F Main Hall: Cop's Ammo",
        "N.Y.P.D. #17 - D3 1F Locker Room: Right Locker",
        "N.Y.P.D. #17 - D3 1F Locker Room: Cop's Ammo",
        "N.Y.P.D. #17 - D3 B1 Weapons Department: Torres's Gun",
        "N.Y.P.D. #17 - D3 B1 Kennel: Cathy's Ammo"
        ]
    )
    pd_sj.add_locations(pd_sj_locations, PE1Location)

    pd_cmbt_sj_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D3 1F Main Hall: Nix's Ammo",
        "N.Y.P.D. #17 - D3 1F Save Room: Warner's Ammo",
        "N.Y.P.D. #17 - D3 1F Conference Room: Spider Chest",
        "N.Y.P.D. #17 - D3 2F Barred Staircase: Cop's Ammo",
        "N.Y.P.D. #17 - D3 2F Holding Cells: Left Chest",
        "N.Y.P.D. #17 - D3 2F Holding Cells: Right Chest",
        "N.Y.P.D. #17 - D3 2F Interrogation Room: Chest",
        "N.Y.P.D. #17 - D3 2F Interrogation Room: Table Sparkle",
        "N.Y.P.D. #17 - D3 2F Save Office: Desk Chest",
        "N.Y.P.D. #17 - D3 2F Save Office: Floor Chest"
        ]
    )
    pd_cmbt_sj.add_locations(pd_cmbt_sj_locations, PE1Location)

    pd_boss_sj_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D3 3F Ambush Hall: Cop's Locker Key",
        "N.Y.P.D. #17 - D4 3F Medical Office: Daniel's Ammo",
        "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Boss Drop",
        "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Chest",
        "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Cop's Ammo",
        "N.Y.P.D. #17 - D3 3F Big Bad Wolf's Backroom: Chest",
        "N.Y.P.D. #17 - D3 3F Kerberos: Boss Drop"
        ]
    )
    pd_boss_sj.add_locations(pd_boss_sj_locations, PE1Location)

    pd_boss_sj_junk_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D4 B1 Weapons Department: Leave It to Wayne"
        ]
    )
    pd_boss_sj_junk.add_locations(pd_boss_sj_junk_locations, PE1Location)

    pd_boss_sj_12rt_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D4 B1 Weapons Department: Tool Kit"
        ]
    )
    pd_boss_sj_12rt.add_locations(pd_boss_sj_12rt_locations, PE1Location)

    pd_boss_sj_14rt_locations = get_location_names_with_ids(
        [
        "N.Y.P.D. #17 - D4 B1 Weapons Department: Super Tool Kit"
        ]
    )
    pd_boss_sj_14rt.add_locations(pd_boss_sj_14rt_locations, PE1Location)


    cp_norq_locations = get_location_names_with_ids(
        [
        "Central Park - Entrance: Car Chest",
        "Central Park - Entrance: Snake Chest"
        ]
    )
    cp_norq.add_locations(cp_norq_locations, PE1Location)

    cp_cmbt_locations = get_location_names_with_ids(
        [
        "Central Park - Front Gate: Left Chest",
        "Central Park - Front Gate: Right Chest",
        "Central Park - Courtyard: Left Gun Chest",
        "Central Park - Courtyard: Right Tool Chest",
        "Central Park - Office: Key Drawer",
        "Central Park - Office: Cabinet",
        "Central Park - Back Courtyard: Ammo Chest",
        "Central Park - Figure 8: Right Chest",
        "Central Park - Figure 8: Left Chest"
        ]
    )
    cp_cmbt.add_locations(cp_cmbt_locations, PE1Location)

    cp_cmbt_zk_locations = get_location_names_with_ids(
        [
        "Central Park - Office: Locked Cupboard",
        "Central Park - Snake Exhibit: Upper Right Chest",
        "Central Park - Snake Exhibit: Lower Left Chest",
        "Central Park - Snake Exhibit: Lower Right Chest",
        "Central Park - Gazebo: Left Chest",
        "Central Park - Gazebo: Right Chest",
        "Central Park - Behind Gazebo (Save): Chest",
        "Central Park - Forest Maze West: Mythical Tool Chest",
        "Central Park - Forest Maze Bridge: Chest",
        "Central Park - Forest Maze Dock: Chest",
        "Central Park - Forest Maze East: Backup Tool Chest",
        "Central Park - Under Bush Bridge: Left Stat Chest",
        "Central Park - Under Bush Bridge: Right YOLO Tool Chest"
        ]
    )
    cp_cmbt_zk.add_locations(cp_cmbt_zk_locations, PE1Location)

    cp_boss_zk_locations = get_location_names_with_ids(
        [
        "Central Park - Carriage Eve: Boss Drop"
        ]
    )
    cp_boss_zk.add_locations(cp_boss_zk_locations, PE1Location)


    sh_norq_locations = get_location_names_with_ids(
        [
        "Soho - Apartment Interior: Chest",
        "Soho - Apartment Exterior: Trash Card",
        "Soho - Pharmacy: Aisle 3 Medicine Chest",
        "Soho - Pharmacy: Aisle 5 Revive Chest",
        "Soho - Pharmacy: Backroom Left Chest",
        "Soho - Pharmacy: Backroom Right Chest",
        "Soho - Pharmacy: Aisle 1 Left Shelf",
        "Soho - Pharmacy: Aisle 3 Far Back Shelf",
        "Soho - Pharmacy: Behind Phone Counter",
        "Soho - Pharmacy: Aisle 4 Right Shelf"
        ]
    )
    sh_norq.add_locations(sh_norq_locations, PE1Location)

    sh_wm_locations = get_location_names_with_ids(
        [
        "Soho - Sam's Gun Shop: Upper Left Chest",
        "Soho - Sam's Gun Shop: Upper Right Chest",
        "Soho - Sam's Gun Shop: Behind Counter Chest",
        "Soho - Sam's Gun Shop: Lower Right Chest",
        "Soho - Sam's Gun Shop: Green Box",
        "Soho - Sam's Gun Shop: Red Box",
        "Soho - Sam's Gun Shop: Shotgun Rack",
        "Soho - Sam's Gun Shop: Rifle Rack"
        ]
    )
    sh_wm.add_locations(sh_wm_locations, PE1Location)


    hs_norq_locations = get_location_names_with_ids(
        [
        "Hospital - 1F Outside: Maeda's Mayoke",
        "Hospital - 1F Lobby: Corner Ammo Chest",
        "Hospital - 1F Lobby: Closet Chest",
        "Hospital - B1 Storage: Upper Chest",
        "Hospital - B1 Storage: Lower Chest",
        "Hospital - B1 Storage: Shelf Fuse Sparkle",
        "Hospital - B1 Save Office: Chest",
        "Hospital - B1 Save Office: Key Drawer",
        "Hospital - B1 Morgue: Chest"
        ]
    )
    hs_norq.add_locations(hs_norq_locations, PE1Location)

    hs_gc_locations = get_location_names_with_ids(
        [
        "Hospital - 1F Green Hallway: Chest"
        ]
    )
    hs_gc.add_locations(hs_gc_locations, PE1Location)

    hs_bc_locations = get_location_names_with_ids(
        [
        "Hospital - B1 Blue Hallway: 50/50 Chest",
        "Hospital - B1 Collapsed Back Stairway: Sparkle",
        "Hospital - B1 Sterilization Room: Left Chest"
        ]
    )
    hs_bc.add_locations(hs_bc_locations, PE1Location)

    hs_cmbt_locations = get_location_names_with_ids(
        [
        "Hospital - 1F Emergency Room: Chest",
        "Hospital - 1F Flashback Room: Chest",
        "Hospital - 1F Flashback Room: Nurse"
        ]
    )
    hs_cmbt.add_locations(hs_cmbt_locations, PE1Location)

    hs_cmbt_gc_locations = get_location_names_with_ids(
        [
        "Hospital - 1F Nitrogen Storage: Chest",
        "Hospital - 1F Nitrogen Storage: King Bacterium Drop"
        ]
    )
    hs_cmbt_gc.add_locations(hs_cmbt_gc_locations, PE1Location)

    hs_cmbt_ak_locations = get_location_names_with_ids(
        [
        "Hospital - B1 Autopsy: Lower Chest",
        "Hospital - B1 Autopsy: Upper Chest",
        "Hospital - B1 Crematory: Corner Chest",
        "Hospital - B1 Crematory: Fuse Sparkle",
        "Hospital - B1 Crematory: Cardkey Corpse"
        ]
    )
    hs_cmbt_ak.add_locations(hs_cmbt_ak_locations, PE1Location)

    hs_cmbt_bc_locations = get_location_names_with_ids(
        [
        "Hospital - B1 Sterilization Room: Right Chest",
        "Hospital - B1 Sterilization Room: Fuse Sparkle"
        ]
    )
    hs_cmbt_bc.add_locations(hs_cmbt_bc_locations, PE1Location)

    hs_cmbt_bc_3f_locations = get_location_names_with_ids(
        [
        "Hospital - 13F Research Lab: Chest",
        "Hospital - 13F Research Lab: Counter",
        "Hospital - 13F Research Lab: Shelf",
        "Hospital - 13F Kennel: Chest",
        "Hospital - 13F Roof Elevator Access: Lower Chest",
        "Hospital - 13F Roof Elevator Access: Upper Chest",
        "Hospital - 13F Roof Elevator Access: Upper Sparkle",
        "Hospital - 13F Roof Elevator Access: Lower Sparkle"
        ]
    )
    hs_cmbt_bc_3f.add_locations(hs_cmbt_bc_3f_locations, PE1Location)

    hs_boss_bc_3f_ek_locations = get_location_names_with_ids(
        [
        "Hospital - Roof Spiderwoman: Boss Drop"
        ]
    )
    hs_boss_bc_3f_ek.add_locations(hs_boss_bc_3f_ek_locations, PE1Location)


    ct_norq_or_cmbt_gk_locations = get_location_names_with_ids(
        [
        "Chinatown - Near Entrance: Left Chest",
        "Chinatown - Near Entrance: Right Chest"
        ]
    )
    ct_norq_or_cmbt_gk.add_locations(ct_norq_or_cmbt_gk_locations, PE1Location)

    ct_cmbt_or_cmbt_gk_locations = get_location_names_with_ids(
        [
        "Chinatown - Antique Shop Exterior (Save): Lower Chest",
        "Chinatown - Antique Shop Exterior (Save): Upper Chest",
        "Chinatown - Antique Shop Interior: Chest",
        "Chinatown - Antique Shop Interior: Shelf",
        "Chinatown - End of the Street: Maeda's Narita",
        "Chinatown - End of the Street: Chest",
        "Chinatown - Sewers Labyrinth A-04: Super Tool Sparkle",
        "Chinatown - Sewers Labyrinth B-01: Medicine 4 Chest",
        "Chinatown - Sewers Labyrinth B-03: Cure-D Sparkle",
        "Chinatown - Sewers Labyrinth B-06: Ammo Chest",
        "Chinatown - Sewers Labyrinth C-02: Cr Protector Chest",
        "Chinatown - Sewers Labyrinth C-06: Range Sparkle",
        "Chinatown - Sewers Labyrinth D-03: M203-3 Chest",
        "Chinatown - Sewers Labyrinth D-08: M870 Chest",
        "Chinatown - Sewers Labyrinth D-11: Off or Def Chest",
        "Chinatown - Sewers Labyrinth E-04: Medicine 3 Chest",
        "Chinatown - Sewers Labyrinth E-10: Tool Sparkle",
        "Chinatown - Sewers Labyrinth F-09: Offense Chest",
        "Chinatown - Sewers Exit Catwalk: Club 3 Chest"
        ]
    )
    ct_cmbt_or_cmbt_gk.add_locations(ct_cmbt_or_cmbt_gk_locations, PE1Location)

    ct_boss_or_boss_gk_locations = get_location_names_with_ids(
        [
        "Chinatown - Pump Station Exterior: Alligator Chest"
        ]
    )
    ct_boss_or_boss_gk.add_locations(ct_boss_or_boss_gk_locations, PE1Location)

    ct_cmbt_or_gk_locations = get_location_names_with_ids(
        [
        "Chinatown - Pump Station Exterior: Catwalk Chest",
        "Chinatown - Pump Station Control Room: Chest"
        ]
    )
    ct_cmbt_or_gk.add_locations(ct_cmbt_or_gk_locations, PE1Location)


    sw_cmbt_pk_or_gk_locations = get_location_names_with_ids(
        [
        "Subway - Platform (Save): Bench Chest",
        "Subway - Platform (Save): Phone Chest",
        "Subway - Exit Stairway: Chest"
        ]
    )
    sw_cmbt_pk_or_gk.add_locations(sw_cmbt_pk_or_gk_locations, PE1Location)

    sw_cmbt_pk_or_cmbt_gk_locations = get_location_names_with_ids(
        [
        "Subway - Left Mole Tunnel: Chest"
        ]
    )
    sw_cmbt_pk_or_cmbt_gk.add_locations(sw_cmbt_pk_or_cmbt_gk_locations, PE1Location)

    sw_boss_pk_or_boss_gk_locations = get_location_names_with_ids(
        [
        "Subway - Centipede: Boss Drop",
        "Subway - Parked Passenger Car: Right Chest",
        "Subway - Parked Passenger Car: Left Chest",
        "Subway - Parked Passenger Car: Lower Chest",
        "Subway - Bridge: Cop's Gate Key"
        ]
    )
    sw_boss_pk_or_boss_gk.add_locations(sw_boss_pk_or_boss_gk_locations, PE1Location)


    wh_norq_locations = get_location_names_with_ids(
        [
        "Warehouse - Outside: Left Chest (Hidden)",
        "Warehouse - Outside: Right Chest",
        "Warehouse - Entrance: Forklift Chest"
        ]
    )
    wh_norq.add_locations(wh_norq_locations, PE1Location)

    wh_cmbt_locations = get_location_names_with_ids(
        [
        "Warehouse - Tom and Jerry: Chest",
        "Warehouse - Tom and Jerry: Key Sparkle",
        "Warehouse - Save Room: Ladder Chest",
        "Warehouse - Save Room: Upper Ground Chest",
        "Warehouse - Save Room: Lower Ground Chest"
        ]
    )
    wh_cmbt.add_locations(wh_cmbt_locations, PE1Location)

    wh_cmbt_wk_locations = get_location_names_with_ids(
        [
        "Warehouse - Before Descent: Lower Left Chest",
        "Warehouse - Before Descent: Upper Left Chest",
        "Warehouse - Before Descent: Upper Right Chest"
        ]
    )
    wh_cmbt_wk.add_locations(wh_cmbt_wk_locations, PE1Location)

    wh_boss_wk_locations = get_location_names_with_ids(
        [
        "Warehouse - Giant Enemy Crab: Boss Drop",
        "Warehouse - Giant Enemy Crab: Steamed Tool"
        ]
    )
    wh_boss_wk.add_locations(wh_boss_wk_locations, PE1Location)


    mu_norq_locations = get_location_names_with_ids(
        [
        "Museum - 1F Klamp Pursuit East Exhibit: Chest",
        "Museum - 1F Klamp Pursuit West Exhibit: Chest",
        "Museum - 1F Rainforest Exhibit: Quiz",
        "Museum - 1F Rainforest Employee Hallway: Quiz",
        "Museum - 1F Rainforest Employee Hallway: Chest",
        "Museum - 1F Stingy Scorpion Hall: Quiz",
        "Museum - 1F T-Rex: Left Chest",
        "Museum - 1F T-Rex: Right Chest"
        ]
    )
    mu_norq.add_locations(mu_norq_locations, PE1Location)

    mu_cmbt_locations = get_location_names_with_ids(
        [
        "Museum - 1F Klamp Pursuit Troodon Hall: Right Chest",
        "Museum - 1F Klamp Pursuit Troodon Hall: Left Chest",
        "Museum - 1F Rainforest Storage Room: Lower Right Chest",
        "Museum - 1F Rainforest Storage Room: Lower Center Chest",
        "Museum - 1F Rainforest Storage Room: Upper Chest",
        "Museum - 1F Rainforest Storage Room: Hidden Closet Right Chest",
        "Museum - 1F Rainforest Storage Room: Hidden Closet Left Chest",
        "Museum - 1F Tribal Staircase: Chest",
        "Museum - 1F Stone Head Room: Ladder Access Chest",
        "Museum - 1F Fire Escape: Stat Chest",
        "Museum - 2F Gemstone Staircase: Quiz",
        "Museum - 2F Gemstone Staircase: Right Chest",
        "Museum - 2F Gemstone Staircase: Left Chest",
        "Museum - 3F Fire Escape: Rocket Chest",
        "Museum - 3F Hall of Evolution: Quiz",
        "Museum - 2F Festive Lobby: Revive Chest",
        "Museum - 3F Pterodactyl Ambush Hall: Chest",
        "Museum - 3F Stegosaurus Room: Chest",
        "Museum - 2F Museum Shop Tents: Upper Chest",
        "Museum - 2F Museum Shop Tents: Lower Chest",
        "Museum - 2F Security Office: Chest",
        "Museum - 4F Security Storage: Lower Right Chest",
        "Museum - 4F Security Storage: Lower Left Chest",
        "Museum - 4F Security Storage: Upper Left Chest",
        "Museum - 4F Security Storage: Center Chest",
        "Museum - 2F Klamp's Office: Maeda's Gun",
        "Museum - 2F Klamp's Office: Klamp's Key",
        "Museum - 4F Forgotten Landing: Full Recover Chest"
        ]
    )
    mu_cmbt.add_locations(mu_cmbt_locations, PE1Location)

    mu_cmbt_kk_locations = get_location_names_with_ids(
        [
        "Museum - 2F Glass Exhibit Near Chocobo: Quiz"
        ]
    )
    mu_cmbt_kk.add_locations(mu_cmbt_kk_locations, PE1Location)

    mu_boss_kk_locations = get_location_names_with_ids(
        [
        "Museum - 3F Triceratops: Boss Drop",
        "Museum - 1F T-Rex: Boss Drop",
        "Museum - 2F Glass Exhibit Near Chocobo: Left Chest Behind Glass",
        "Museum - 2F Glass Exhibit Near Chocobo: Right Chest Behind Glass",
        "Museum - 3F Final Approach: Quiz",
        "Museum - 3F Final Approach: Right Chest Behind Glass",
        "Museum - 3F Final Approach: Left Chest Behind Glass"
        ]
    )
    mu_boss_kk.add_locations(mu_boss_kk_locations, PE1Location)


    cruiser_locations = get_location_names_with_ids(
        [
        "Cruiser - Deck: Daniel's Sacrifice"
        ]
    )
    cruiser.add_locations(cruiser_locations, PE1Location)


    cb_k1_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 1-01: Offense",
        "Chrysler BLDG. - Treasurebox Set 1-01: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 1-01: Tool",
        "Chrysler BLDG. - Treasurebox Set 1-01: USP-2",
        "Chrysler BLDG. - Treasurebox Set 1-02: Tool A",
        "Chrysler BLDG. - Treasurebox Set 1-02: M1911A4",
        "Chrysler BLDG. - Treasurebox Set 1-02: Tool B",
        "Chrysler BLDG. - Treasurebox Set 1-02: Sp Vest 2",
        "Chrysler BLDG. - Treasurebox Set 1-03: M16A2",
        "Chrysler BLDG. - Treasurebox Set 1-03: Tool",
        "Chrysler BLDG. - Treasurebox Set 1-03: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 1-04: PE",
        "Chrysler BLDG. - Treasurebox Set 1-04: Kv Jacket",
        "Chrysler BLDG. - Treasurebox Set 1-04: M79-4",
        "Chrysler BLDG. - Treasurebox Set 1-05: P38 T Card",
        "Chrysler BLDG. - Treasurebox Set 1-05: P228",
        "Chrysler BLDG. - Treasurebox Set 1-05: PE",
        "Chrysler BLDG. - Treasurebox Set 1-05: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 1-06: Sv Jacket",
        "Chrysler BLDG. - Treasurebox Set 1-06: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 1-07: PE",
        "Chrysler BLDG. - Treasurebox Set 1-07: P226",
        "Chrysler BLDG. - Treasurebox Set 1-07: Defense",
        "Chrysler BLDG. - Treasurebox Set 1-08: Range",
        "Chrysler BLDG. - Treasurebox Set 1-08: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 1-08: Rocket",
        "Chrysler BLDG. - Treasurebox Set 1-08: Tool",
        "Chrysler BLDG. - Treasurebox Set 1-09: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 1-09: Offense A",
        "Chrysler BLDG. - Treasurebox Set 1-09: Offense B",
        "Chrysler BLDG. - 10F Spiderwoman EX: Boss Drop"
        ]
    )
    cb_k1.add_locations(cb_k1_locations, PE1Location)

    cb_k2_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 2-01: Cr Jacket",
        "Chrysler BLDG. - Treasurebox Set 2-01: Defense",
        "Chrysler BLDG. - Treasurebox Set 2-02: Tool",
        "Chrysler BLDG. - Treasurebox Set 2-03: Tool A",
        "Chrysler BLDG. - Treasurebox Set 2-03: Tool B",
        "Chrysler BLDG. - Treasurebox Set 2-03: M203-5",
        "Chrysler BLDG. - Treasurebox Set 2-04: Tool",
        "Chrysler BLDG. - Treasurebox Set 2-04: M96",
        "Chrysler BLDG. - Treasurebox Set 2-04: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 2-05: Kasul T Card",
        "Chrysler BLDG. - Treasurebox Set 2-05: Offense",
        "Chrysler BLDG. - Treasurebox Set 2-05: Rocket",
        "Chrysler BLDG. - Treasurebox Set 2-06: Super Tool",
        "Chrysler BLDG. - Treasurebox Set 2-06: Club 4",
        "Chrysler BLDG. - Treasurebox Set 2-06: Defense",
        "Chrysler BLDG. - Treasurebox Set 2-07: AM44",
        "Chrysler BLDG. - Treasurebox Set 2-07: P229",
        "Chrysler BLDG. - Treasurebox Set 2-08: PE",
        "Chrysler BLDG. - Treasurebox Set 2-08: Sp Suit 1",
        "Chrysler BLDG. - Treasurebox Set 2-09: Full UZ",
        "Chrysler BLDG. - Treasurebox Set 2-09: Range",
        "Chrysler BLDG. - Treasurebox Set 2-09: Bhawk T Card",
        "Chrysler BLDG. - Treasurebox Set 2-10: Kv Suit 1",
        "Chrysler BLDG. - Treasurebox Set 2-10: Tool",
        "Chrysler BLDG. - 20F Alligators EX: Boss Drops"
        ]
    )
    cb_k2.add_locations(cb_k2_locations, PE1Location)

    cb_k3_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 3-01: Tool",
        "Chrysler BLDG. - Treasurebox Set 3-02: Tool A",
        "Chrysler BLDG. - Treasurebox Set 3-02: PPKS T Card",
        "Chrysler BLDG. - Treasurebox Set 3-02: Tool B",
        "Chrysler BLDG. - Treasurebox Set 3-03: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 3-03: Tool",
        "Chrysler BLDG. - Treasurebox Set 3-03: Super Tool",
        "Chrysler BLDG. - Treasurebox Set 3-04: Super Tool",
        "Chrysler BLDG. - Treasurebox Set 3-04: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 3-04: Mark 23",
        "Chrysler BLDG. - Treasurebox Set 3-05: Offense",
        "Chrysler BLDG. - Treasurebox Set 3-05: Tool",
        "Chrysler BLDG. - Treasurebox Set 3-05: M870-2",
        "Chrysler BLDG. - Treasurebox Set 3-06: Type64",
        "Chrysler BLDG. - Treasurebox Set 3-06: Defense",
        "Chrysler BLDG. - Treasurebox Set 3-07: Cm Jacket",
        "Chrysler BLDG. - Treasurebox Set 3-08: B Jacket 2",
        "Chrysler BLDG. - Treasurebox Set 3-08: M1 T Card",
        "Chrysler BLDG. - Treasurebox Set 3-08: Offense",
        "Chrysler BLDG. - Treasurebox Set 3-09: Range",
        "Chrysler BLDG. - Treasurebox Set 3-09: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 3-10: Tool",
        "Chrysler BLDG. - Treasurebox Set 3-10: Sv Suit 1",
        "Chrysler BLDG. - Treasurebox Set 3-10: M79-5",
        "Chrysler BLDG. - 30F Centipede EX: Boss Drop"
        ]
    )
    cb_k3.add_locations(cb_k3_locations, PE1Location)

    cb_k4_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 4-01: PSG-1",
        "Chrysler BLDG. - Treasurebox Set 4-01: Tool",
        "Chrysler BLDG. - Treasurebox Set 4-01: Full Cure",
        "Chrysler BLDG. - Treasurebox Set 4-01: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 4-02: Cm Suit 1",
        "Chrysler BLDG. - Treasurebox Set 4-02: Tool",
        "Chrysler BLDG. - Treasurebox Set 4-02: Full Recover",
        "Chrysler BLDG. - Treasurebox Set 4-03: Tool",
        "Chrysler BLDG. - Treasurebox Set 4-03: Rocket",
        "Chrysler BLDG. - Treasurebox Set 4-03: Defense",
        "Chrysler BLDG. - Treasurebox Set 4-03: Sv Suit 2",
        "Chrysler BLDG. - Treasurebox Set 4-04: MP5A5",
        "Chrysler BLDG. - Treasurebox Set 4-04: MK5 T Card",
        "Chrysler BLDG. - Treasurebox Set 4-04: Sp Armor 1",
        "Chrysler BLDG. - Treasurebox Set 4-04: BAR T Card",
        "Chrysler BLDG. - Treasurebox Set 4-05: Tool",
        "Chrysler BLDG. - Treasurebox Set 4-06: MP44 T Card",
        "Chrysler BLDG. - Treasurebox Set 4-07: MG42 T Card",
        "Chrysler BLDG. - Treasurebox Set 4-07: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 4-07: M1911A5",
        "Chrysler BLDG. - Treasurebox Set 4-07: Defense",
        "Chrysler BLDG. - Treasurebox Set 4-08: Maverick",
        "Chrysler BLDG. - Treasurebox Set 4-08: Range",
        "Chrysler BLDG. - Treasurebox Set 4-09: Kv Armor 1",
        "Chrysler BLDG. - Treasurebox Set 4-10: Tool",
        "Chrysler BLDG. - 40F Triceratops EX: Boss Drop"
        ]
    )
    cb_k4.add_locations(cb_k4_locations, PE1Location)

    cb_k5_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 5-01: SAR",
        "Chrysler BLDG. - Treasurebox Set 5-01: Tool",
        "Chrysler BLDG. - Treasurebox Set 5-01: M29 T Card",
        "Chrysler BLDG. - Treasurebox Set 5-02: M73 T Card",
        "Chrysler BLDG. - Treasurebox Set 5-02: PE",
        "Chrysler BLDG. - Treasurebox Set 5-02: Super Tool",
        "Chrysler BLDG. - Treasurebox Set 5-02: AT4-1",
        "Chrysler BLDG. - Treasurebox Set 5-03: Tool",
        "Chrysler BLDG. - Treasurebox Set 5-03: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 5-04: Cr Suit 1",
        "Chrysler BLDG. - Treasurebox Set 5-05: USP-3",
        "Chrysler BLDG. - Treasurebox Set 5-06: Offense",
        "Chrysler BLDG. - Treasurebox Set 5-06: Rocket",
        "Chrysler BLDG. - Treasurebox Set 5-06: Cm Armor 1",
        "Chrysler BLDG. - Treasurebox Set 5-06: Tool",
        "Chrysler BLDG. - Treasurebox Set 5-06: Range",
        "Chrysler BLDG. - Treasurebox Set 5-07: Tool",
        "Chrysler BLDG. - Treasurebox Set 5-08: B Suit 1",
        "Chrysler BLDG. - Treasurebox Set 5-09: G20",
        "Chrysler BLDG. - Treasurebox Set 5-09: Tool",
        "Chrysler BLDG. - Treasurebox Set 5-09: Offense",
        "Chrysler BLDG. - Treasurebox Set 5-09: Sv Armor 1",
        "Chrysler BLDG. - 50F Cockroach: Boss Drop"
        ]
    )
    cb_k5.add_locations(cb_k5_locations, PE1Location)

    cb_k6_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 6-01: Type38 T Card",
        "Chrysler BLDG. - Treasurebox Set 6-01: Cr Evade",
        "Chrysler BLDG. - Treasurebox Set 6-01: Sp Armor 2",
        "Chrysler BLDG. - Treasurebox Set 6-02: Rocket",
        "Chrysler BLDG. - Treasurebox Set 6-02: MP5SD6",
        "Chrysler BLDG. - Treasurebox Set 6-03: B Suit 2",
        "Chrysler BLDG. - Treasurebox Set 6-04: M712",
        "Chrysler BLDG. - Treasurebox Set 6-05: S12",
        "Chrysler BLDG. - Treasurebox Set 6-05: PE",
        "Chrysler BLDG. - Treasurebox Set 6-05: Full Recover",
        "Chrysler BLDG. - Treasurebox Set 6-05: Cr Armor 1",
        "Chrysler BLDG. - Treasurebox Set 6-06: Full Cure",
        "Chrysler BLDG. - Treasurebox Set 6-07: FA-MAS",
        "Chrysler BLDG. - Treasurebox Set 6-08: Range",
        "Chrysler BLDG. - Treasurebox Set 6-09: Tool A",
        "Chrysler BLDG. - Treasurebox Set 6-09: Tool B",
        "Chrysler BLDG. - Treasurebox Set 6-09: Tool C",
        "Chrysler BLDG. - 60F Giant Enemy Crab EX: Boss Drop"
        ]
    )
    cb_k6.add_locations(cb_k6_locations, PE1Location)

    cb_k7_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - Treasurebox Set 7-01: PE",
        "Chrysler BLDG. - Treasurebox Set 7-01: M500-2",
        "Chrysler BLDG. - Treasurebox Set 7-01: Full Recover",
        "Chrysler BLDG. - Treasurebox Set 7-01: M500",
        "Chrysler BLDG. - Treasurebox Set 7-02: Defense",
        "Chrysler BLDG. - Treasurebox Set 7-03: XM177E2",
        "Chrysler BLDG. - Treasurebox Set 7-03: Tool",
        "Chrysler BLDG. - Treasurebox Set 7-03: Range",
        "Chrysler BLDG. - Treasurebox Set 7-03: Full Cure",
        "Chrysler BLDG. - Treasurebox Set 7-04: Super Tool",
        "Chrysler BLDG. - Treasurebox Set 7-04: Cm Armor 2",
        "Chrysler BLDG. - Treasurebox Set 7-04: Bullet Cap",
        "Chrysler BLDG. - Treasurebox Set 7-05: B Armor",
        "Chrysler BLDG. - Treasurebox Set 7-05: M96R",
        "Chrysler BLDG. - Treasurebox Set 7-05: Super Tool",
        "Chrysler BLDG. - Treasurebox Set 7-05: Tool",
        "Chrysler BLDG. - Treasurebox Set 7-06: Type3 T Card",
        "Chrysler BLDG. - Treasurebox Set 7-07: M203-6",
        "Chrysler BLDG. - Treasurebox Set 7-07: Offense",
        "Chrysler BLDG. - Treasurebox Set 7-07: Sv Armor 2",
        "Chrysler BLDG. - Treasurebox Set 7-08: Eagle T Card",
        "Chrysler BLDG. - Treasurebox Set 7-08: PE",
        "Chrysler BLDG. - Treasurebox Set 7-08: Club 5",
        "Chrysler BLDG. - Treasurebox Set 7-08: Cr Armor 2",
        "Chrysler BLDG. - 70F Queen Bee: Boss Drop"
        ]
    )
    cb_k7.add_locations(cb_k7_locations, PE1Location)

    cb_spire_locations = get_location_names_with_ids(
        [
        "Chrysler BLDG. - 77F Spire: Maya"
        ]
    )
    cb_spire.add_locations(cb_spire_locations, PE1Location)




def create_events(world: PE1World) -> None:

    cruiser = world.get_region("Cruiser: Boss")

    cruiser.add_event(
        "End Goal: Hell's Kitchen", "Victory", location_type=PE1Location, item_type=items.PE1Item
    )
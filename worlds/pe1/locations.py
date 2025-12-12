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
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Chest": 46,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Boss Drop": 47,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf: Cop's Ammo": 48,
    "N.Y.P.D. #17 - D3 3F Big Bad Wolf's Backroom: Chest": 49,
    "N.Y.P.D. #17 - D2 B1 Weapons Storage: Left Chest": 50,
    "N.Y.P.D. #17 - D2 B1 Weapons Storage: Center Chest": 51,
    "N.Y.P.D. #17 - D2 B1 Weapons Storage: Right Chest": 52,
    "N.Y.P.D. #17 - D3 3F Kerberos: Boss Drop": 53,
    "N.Y.P.D. #17 - D4 B1 Weapons Department: Tool Kit": 54,
    "N.Y.P.D. #17 - D4 B1 Weapons Department: Super Tool Kit": 55,
    "N.Y.P.D. #17 - D4 B1 Weapons Department: Leave It to Wayne": 56,

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

    "Soho - Apartment Interior: Chest": 81,
    "Soho - Apartment Exterior: Trash Card": 82,
    "Soho - Pharmacy: Aisle 3 Medicine Chest": 83,
    "Soho - Pharmacy: Aisle 5 Revive Chest": 84,
    "Soho - Pharmacy: Backroom Left Chest": 85,
    "Soho - Pharmacy: Backroom Right Chest": 86,
    "Soho - Pharmacy: Aisle 1 Left Shelf": 87,
    "Soho - Pharmacy: Aisle 3 Far Back Shelf": 88,
    "Soho - Pharmacy: Behind Phone Counter": 89,
    "Soho - Pharmacy: Aisle 4 Right Shelf": 90,
    "Soho - Sam's Gun Shop: Upper Left Chest": 91,
    "Soho - Sam's Gun Shop: Upper Right Chest": 92,
    "Soho - Sam's Gun Shop: Behind Counter Chest": 93,
    "Soho - Sam's Gun Shop: Lower Right Chest": 94,
    "Soho - Sam's Gun Shop: Green Box": 95,
    "Soho - Sam's Gun Shop: Red Box": 96,
    "Soho - Sam's Gun Shop: Shotgun Rack": 97,
    "Soho - Sam's Gun Shop: Rifle Rack": 98,

    "Hospital - 1F Outside: Maeda's Mayoke": 99,
    "Hospital - 1F Lobby: Corner Ammo Chest": 100,
    "Hospital - 1F Lobby: Closet Chest": 101,
    "Hospital - 1F Emergency Room: Chest": 102,
    "Hospital - 1F Flashback Room: Chest": 103,
    "Hospital - 1F Flashback Room: Nurse": 104,
    "Hospital - 1F Green Hallway: Chest": 105,
    "Hospital - 1F Nitrogen Storage: Chest": 106,
    "Hospital - 1F Nitrogen Storage: King Bacterium Drop": 107,
    "Hospital - B1 Storage: Upper Chest": 108,
    "Hospital - B1 Storage: Lower Chest": 109,
    "Hospital - B1 Storage: Shelf Fuse Sparkle": 110,
    "Hospital - B1 Save Office: Chest": 111,
    "Hospital - B1 Save Office: Key Drawer": 112,
    "Hospital - B1 Morgue: Chest": 113,
    "Hospital - B1 Autopsy: Lower Chest": 114,
    "Hospital - B1 Autopsy: Upper Chest": 115,
    "Hospital - B1 Crematory: Corner Chest": 116,
    "Hospital - B1 Crematory: Fuse Sparkle": 117,
    "Hospital - B1 Crematory: Cardkey Corpse": 118,
    "Hospital - B1 Blue Hallway: 50/50 Chest": 119,
    "Hospital - B1 Collapsed Back Stairway: Sparkle": 120,
    "Hospital - B1 Sterilization Room: Right Chest": 121,
    "Hospital - B1 Sterilization Room: Left Chest": 122,
    "Hospital - B1 Sterilization Room: Fuse Sparkle": 123,
    "Hospital - 13F Research Lab: Chest": 124,
    "Hospital - 13F Research Lab: Counter": 125,
    "Hospital - 13F Research Lab: Shelf": 126,
    "Hospital - 13F Kennel: Chest": 127,
    "Hospital - 13F Roof Elevator Access: Lower Chest": 128,
    "Hospital - 13F Roof Elevator Access: Upper Chest": 129,
    "Hospital - 13F Roof Elevator Access: 1st Sparkle (Junk)": 130,
    "Hospital - 13F Roof Elevator Access: 2nd Sparkle (Key)": 131,
    "Hospital - Roof Spiderwoman: Boss Drop": 132,

    "Chinatown - Near Entrance: Left Chest": 133,
    "Chinatown - Near Entrance: Right Chest": 134,
    "Chinatown - Antique Shop Exterior (Save): Lower Chest": 135,
    "Chinatown - Antique Shop Exterior (Save): Upper Chest": 136,
    "Chinatown - Antique Shop Interior: Chest": 137,
    "Chinatown - Antique Shop Interior: Shelf": 138,
    "Chinatown - End of the Street: Chest": 139,
    "Chinatown - End of the Street: Maeda's Narita": 140,
    "Chinatown - Sewers Labyrinth A-04: Super Tool Sparkle": 141,
    "Chinatown - Sewers Labyrinth B-01: Medicine 4 Chest": 142,
    "Chinatown - Sewers Labyrinth B-03: Cure-D Sparkle": 143,
    "Chinatown - Sewers Labyrinth B-06: Ammo Chest": 144,
    "Chinatown - Sewers Labyrinth C-02: Cr Protector Chest": 145,
    "Chinatown - Sewers Labyrinth C-06: Range Sparkle": 146,
    "Chinatown - Sewers Labyrinth D-03: M203-3 Chest": 147,
    "Chinatown - Sewers Labyrinth D-08: M870 Chest": 148,
    "Chinatown - Sewers Labyrinth D-11: Off or Def Chest": 149,
    "Chinatown - Sewers Labyrinth E-04: Medicine 3 Chest": 150,
    "Chinatown - Sewers Labyrinth E-10: Tool Sparkle": 151,
    "Chinatown - Sewers Labyrinth F-09: Offense Chest": 152,
    "Chinatown - Sewers Exit Catwalk: Club 3 Chest": 153,
    "Chinatown - Pump Station Exterior: Alligator Chest": 154,
    "Chinatown - Pump Station Exterior: Catwalk Chest": 155,
    "Chinatown - Pump Station Control Room: Chest": 156,

    "Subway - Platform (Save): Bench Chest": 157,
    "Subway - Platform (Save): Phone Chest": 158,
    "Subway - Exit Stairway: Chest": 159,
    "Subway - Left Mole Tunnel: Chest": 160,
    "Subway - Centipede: Boss Drop": 161,
    "Subway - Parked Passenger Car: Right Chest": 162,
    "Subway - Parked Passenger Car: Left Chest": 163,
    "Subway - Parked Passenger Car: Lower Chest": 164,
    "Subway - Bridge: Cop's Gate Key": 165,

    "Warehouse - Outside: Left Chest (Hidden)": 166,
    "Warehouse - Outside: Right Chest": 167,
    "Warehouse - Entrance: Forklift Chest": 168,
    "Warehouse - Tom and Jerry: Chest": 169,
    "Warehouse - Tom and Jerry: Key Sparkle": 170,
    "Warehouse - Save Room: Ladder Chest": 171,
    "Warehouse - Save Room: Upper Ground Chest": 172,
    "Warehouse - Save Room: Lower Ground Chest": 173,
    "Warehouse - Before Descent: Lower Left Chest": 174,
    "Warehouse - Before Descent: Upper Left Chest": 175,
    "Warehouse - Before Descent: Upper Right Chest": 176,
    "Warehouse - Giant Enemy Crab: Boss Drop": 177,
    "Warehouse - Giant Enemy Crab: Steamed Tool": 178,

    "Museum - 1F Klamp Pursuit East Exhibit: Chest": 179,
    "Museum - 1F Klamp Pursuit West Exhibit: Chest": 180,
    "Museum - 1F Klamp Pursuit Troodon Hall: Right Chest": 181,
    "Museum - 1F Klamp Pursuit Troodon Hall: Left Chest": 182,
    "Museum - 1F Rainforest Exhibit: Quiz": 183
    "Museum - 1F Rainforest Employee Hallway: Quiz": 184
    "Museum - 1F Rainforest Employee Hallway: Chest": 185,
    "Museum - 1F Rainforest Storage Room: Lower Right Chest": 186,
    "Museum - 1F Rainforest Storage Room: Lower Center Chest": 187,
    "Museum - 1F Rainforest Storage Room: Upper Chest": 188,
    "Museum - 1F Rainforest Storage Room: Hidden Closet Right Chest": 189,
    "Museum - 1F Rainforest Storage Room: Hidden Closet Left Chest": 190,
    "Museum - 1F Stingy Scorpion Hall: Quiz": 191,
    "Museum - 1F Tribal Staircase: Chest": 192,
    "Museum - 1F Stone Head Room: Ladder Access Chest": 193,
    "Museum - 1F Fire Escape: Stat Chest": 194,
    "Museum - 2F Gemstone Staircase: Quiz": 195,
    "Museum - 2F Gemstone Staircase: Right Chest": 196,
    "Museum - 2F Gemstone Staircase: Left Chest": 197,
    "Museum - 3F Fire Escape: Rocket Chest": 198,
    "Museum - 3F Hall of Evolution: Quiz": 199,
    "Museum - 2F Festive Lobby: Revive Chest": 200,
    "Museum - 3F Pterodactyl Ambush Hall: Chest": 201,
    "Museum - 3F Stegosaurus Room: Chest": 202,
    "Museum - 2F Museum Shop Tents: Upper Chest": 203,
    "Museum - 2F Museum Shop Tents: Lower Chest": 204,
    "Museum - 2F Security Office: Chest": 205,
    "Museum - 4F Security Storage: Lower Right Chest": 206,
    "Museum - 4F Security Storage: Lower Left Chest": 207,
    "Museum - 4F Security Storage: Upper Left Chest": 208,
    "Museum - 4F Security Storage: Center Chest": 209,
    "Museum - 2F Klamp's Office: Maeda's Gun": 210,
    "Museum - 2F Klamp's Office: Klamp's Key": 211,
    "Museum - 4F Forgotten Landing: Full Recover Chest": 212,
    "Museum - 3F Triceratops: Boss Drop": 213,
    "Museum - 1F T-Rex: Left Chest": 214,
    "Museum - 1F T-Rex: Right Chest": 215,
    "Museum - 1F T-Rex: Boss Drop": 216,
    "Museum - 2F Glass Exhibit Near Chocobo: Quiz": 217,
    "Museum - 2F Glass Exhibit Near Chocobo: Left Chest Behind Glass": 218,
    "Museum - 2F Glass Exhibit Near Chocobo: Right Chest Behind Glass": 219,
    "Museum - 3F Final Approach: Quiz": 220,
    "Museum - 3F Final Approach: Right Chest Behind Glass": 221,
    "Museum - 3F Final Approach: Left Chest Behind Glass": 222,

    "Cruiser - Deck: Daniel's Sacrifice": PELoctData("Cruiser", 6245223),

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
    "Chrysler BLDG. - 77F Spire: Maya": 474,
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



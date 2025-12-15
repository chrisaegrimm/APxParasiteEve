from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups#, option_presets




class PE1WebWorld(WebWorld):

    game = "Parasite Eve"
    theme = "ice"

    setup_en = Tutorial(
        "Parasite Eve AP Guide",
        "Instructions on how to set up Parasite Eve for single-player local seeds and multiworlds.",
        "English",
        "setup_en.md",
        "setup/en",
        ["chrisaegrimm"],
    )


    tutorials = [setup_en]
    option_groups = option_groups
   #option_presets = option_presets
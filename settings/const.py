# configuration file

from .assets_data import *

# tkinter commands
TK_COMMAND_SOURCE = "source"
TK_COMMAND_SET_THEME = "set_theme"

# tkinter attributes
TK_ATTRIBUTE_TOPMOST = "-topmost"
TK_ATTRIBUTE_FULLSCREEN = "-fullscreen"

# Application phases
PHASE_ACTIVE = "Active"
PHASE_INACTIVE = "Inactive"

# Others
AUTHOR_GITHUB_URL = ""
MOD_AUTHOR_GITHUB_URL = ""
TROLL_FACE_ANIMATION_FRAMES_COUNT = 65
BACKGROUND_ANIMATION_FRAMES_COUNT = 43
TROLL_FACE_FRAMES = []
RENDERING_DELAY = 0.07  # sec
LOADING_DELAY = 500     # ms
ATTACK_TARGETS_LIST = open(TARGETS_TXT, "r").read().splitlines()

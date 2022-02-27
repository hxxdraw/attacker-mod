# configuration file

import os


# Assets (folders)
ASSETS_FOLDER = r"assets/"
THEMES_DATA_FILES_FOLDER = os.path.join(ASSETS_FOLDER, "themes-data")
IMAGES_FOLDER = os.path.join(ASSETS_FOLDER, "img")
COMPONENTS_FOLDER = os.path.join(ASSETS_FOLDER, "components")

# Assets (files)
TROLL_FACE_ANIMATION_GIF = os.path.join(IMAGES_FOLDER, "troll.gif")
NINJA_LOGO_PNG = os.path.join(IMAGES_FOLDER, "loading-logo.png")
MOTTO_PNG = os.path.join(IMAGES_FOLDER, "motto.png")
BACKGROUND_JPG = os.path.join(IMAGES_FOLDER, "background.jpg")
TARGETS_TXT = "targets.txt"

# Assets (themes)
THEMES_DATA_FILES_LIST: list = [
    os.path.join(THEMES_DATA_FILES_FOLDER, file) for file in os.listdir(THEMES_DATA_FILES_FOLDER)
]

# Assets (components)
CARD_FRAME_CFG_FILE = os.path.join(COMPONENTS_FOLDER, "card-frame.json")
START_BUTTON_CFG_FILE = os.path.join(COMPONENTS_FOLDER, "start-button.json")
STOP_BUTTON_CFG_FILE = os.path.join(COMPONENTS_FOLDER, "stop-button.json")
ORIGINAL_GITHUB_BUTTON_CFG_FILE = os.path.join(COMPONENTS_FOLDER, "original-github-button.json")
MODIFICATION_GITHUB_BUTTON_CFG_FILE = os.path.join(COMPONENTS_FOLDER, "modification-github-button.json")
STATUS_LABEL_CFG_FILE = os.path.join(COMPONENTS_FOLDER, "status-label.json")

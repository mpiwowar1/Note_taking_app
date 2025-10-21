
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"

try:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        Config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    Config = {}


def InitConfig():
    Config.setdefault("Last", None)
    Config.setdefault("IconSet", {
        "File": str(BASE_DIR / "img/menubuttons/file.png"),
        "Save": str(BASE_DIR / "img/menubuttons/save.png"),
        "Settings": str(BASE_DIR / "img/menubuttons/settings.png")
    })
    SaveConfig() 


def SaveConfig():
    serializable_config = {}
    for key, value in Config.items():
        try:
            json.dumps({key: value})
            serializable_config[key] = value
        except TypeError:
            pass 


    temp_path = CONFIG_PATH.with_suffix(".tmp")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(serializable_config, f, indent=4)
    temp_path.replace(CONFIG_PATH)

import json
from pathlib import Path
from customtkinter import CTkImage
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent
config_path = BASE_DIR / "config.json"

with open(config_path, "r", encoding="utf-8") as file:
    Config = json.load(file)

def SaveConfig():
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(Config, file, indent=4)

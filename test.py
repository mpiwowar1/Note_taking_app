import json
from pathlib import Path
from customtkinter import CTkImage
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent


config_path = BASE_DIR / "objects" /"config.json"

with open(config_path, "r", encoding="utf-8") as file:
    Config = json.load(file)

print(config_path)

IMG_Path = BASE_DIR / Config["IconSet"]["Save"]
print(IMG_Path)
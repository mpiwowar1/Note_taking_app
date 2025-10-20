import customtkinter as ct
from .menu_frame import MenuFrame
from .text_frame import TextFrame
from .config import Config,InitConfig

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("NoteApp")
        self.geometry("1000x600")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1) 
        self.textframe = TextFrame(self)
        self.menuframe = MenuFrame(self, "Menu", Config["IconSet"].keys(), self.textframe)
        InitConfig()
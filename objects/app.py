import customtkinter as ct
from .menu_frame import MenuFrame
from .text_frame import TextFrame
from .config import Config,InitConfig
from .window_manager import WindowAuto

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("NoteApp")
        WindowAuto(self, 1000, 600)
        InitConfig()
        x = self.winfo_x()
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._set_appearance_mode(Config["Settings"]["Appearance"])
        self.textframe = TextFrame(self)
        self.menuframe = MenuFrame(self, "Menu", Config["IconSet"].keys(), self.textframe)
        

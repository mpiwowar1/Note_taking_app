import customtkinter as ct
from .menu_frame import MenuFrame
from .text_frame import TextFrame

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("NoteApp")
        self.geometry("1000x600")

        self.grid_columnconfigure(0, weight=0)  # Left frame fixed
        self.grid_columnconfigure(1, weight=1)  # Main area expands
        self.grid_rowconfigure(0, weight=1)  # Allow vertical stretch
        self.textframe = TextFrame(self)
        self.menuframe = MenuFrame(self, "Menu", ["Home", "Notes", "Texttotermial"], self.textframe)
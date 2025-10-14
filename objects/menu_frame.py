import customtkinter as ct
from .others import MenuButton
from .others import MenuButtonCreate
from .text_frame import TextFrame

class MenuFrame(ct.CTkFrame):
    def __init__(self, master, title, values, text_frame):
        super().__init__(master, width=60)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.text_frame = text_frame
        btns = MenuButtonCreate(self, values)
        self.grid_rowconfigure(len(values), weight=1)
        self.grid(row=0, column=0, sticky="ns")
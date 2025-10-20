import customtkinter as ct
from .menu_button import MenuButton
from .text_frame import TextFrame
from customtkinter import CTkImage
from PIL import Image

class MenuFrame(ct.CTkFrame):
    def __init__(self, master, title, values, text_frame):
        super().__init__(master, width=60,corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.text_frame = text_frame
        iconset = {"Save": CTkImage(light_image=Image.open(r"C:\Users\Maks\Documents\Learninng\Python\NoteApp\Note_taking_app\objects\img\menubuttons\save.png"), size=(32, 32),),
                   "File": CTkImage(light_image=Image.open(r"C:\Users\Maks\Documents\Learninng\Python\NoteApp\Note_taking_app\objects\img\menubuttons\file.png"), size=(32, 32),)
                   }
        btns = MenuButton.create_buttons(self, values, iconset, text_frame)
        self.grid_rowconfigure(len(values), weight=1)
        self.grid(row=0,rowspan=2, column=0, sticky="ns")

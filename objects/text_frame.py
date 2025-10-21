import customtkinter as ct
from .config import Config
from .footer import Footer

class TextFrame(ct.CTkFrame):
    def __init__(self, master, font=("Arial", 14)):
        super().__init__(master,corner_radius=0)
        self._set_appearance_mode(Config["Settings"]["Appearance"])
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.textbox = ct.CTkTextbox(self, wrap="word",corner_radius=0)
        self.textbox._set_appearance_mode(Config["Settings"]["Appearance"])
        self.textbox.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.grid(row=0, column=1, sticky="nsew")
        try:
            file=open(Config["Last"],"r",encoding="utf-8")
        except:
            Config["Last"]=None
        else:
            self.textbox.insert("0.0", file.read())
            file.close()
        self.textbox.focus_set()
        self.footer=Footer(master, self)
    def get_text(self):
        return self.textbox.get("1.0", "end-1c")
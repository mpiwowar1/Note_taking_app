from .config import Config
import customtkinter as ct

class Footer(ct.CTkFrame):
    def __init__(self, master, text_frame, height=30):
        super().__init__(master, height=height, corner_radius=0)
        self.text_frame = text_frame
        self.label = ct.CTkLabel(self, text=Config["Last"] if Config["Last"] else "No directory selected", anchor="w")
        self.label.pack(fill="both", expand=True, padx=10)
        self.grid(row=1, column=1, columnspan=2, sticky="ew")
        self.columnconfigure(0, weight=0)
    
    def update_status(self):
        self.label.configure(text=Config["Last"] if Config["Last"] else "No directory selected")
        self.update_idletasks()
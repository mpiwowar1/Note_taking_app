import customtkinter as ct

class TextFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master,corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.textbox = ct.CTkTextbox(self, wrap="word",corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.grid(row=0, column=1, sticky="nsew")  # Main area expands
    def get_text(self):
        return self.textbox.get("1.0", "end-1c")
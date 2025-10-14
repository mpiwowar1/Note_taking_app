import customtkinter as ct

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("NoteApp")
        self.geometry("1000x600")
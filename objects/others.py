import customtkinter as ct

class MenuButton(ct.CTkButton):
    def __init__(self, master, icon=None, command=None):
        super().__init__(master, text="", width=40, height=40, command=command)
        if icon:
            self.configure(image=icon)  # Set the icon if provided

def MenuButtonCreate(self,values):
    for i, value in enumerate(values):
            btns = MenuButton(self, icon=None, command=lambda v=value: print(self.text_frame.get_text()))
            btns.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
    
    return btns
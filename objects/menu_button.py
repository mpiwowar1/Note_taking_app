import customtkinter as ct

class MenuButton(ct.CTkButton):
    def __init__(self, master, icon=None, command=None, text=""):
        # If icon is provided, show only icon, otherwise show text
        if icon:
            super().__init__(master, text="", width=40, height=40, command=command, image=icon)
        else:
            super().__init__(master, text=text, width=40, height=40, command=command)

    @staticmethod
    def save_button_action(text_frame):
        print("Save command executed")
        texttosave=text_frame.get_text()
        plik=open("saved_text.txt","w",encoding="utf-8")
        plik.write(texttosave)
        plik.close()
    @staticmethod
    def create_buttons(master, values, iconset, text_frame, commandset=None):
        buttons = []
        commandset = {"Save": lambda: MenuButton.save_button_action(text_frame)  }
        for i, value in enumerate(values):
            icon = iconset.get(value)
            command = commandset.get(value)
            btn = MenuButton(master, icon=icon, command=command, text=value if not icon else "")
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
            buttons.append(btn)
        return buttons
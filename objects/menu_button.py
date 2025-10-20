import customtkinter as ct
from tkinter import filedialog
from .popup import Popup

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
    def file_button_action(text_frame):
        def frame_load_file():
            text_frame.textbox.delete("0.0", "end")
            text_frame.textbox.insert("0.0", open(file, "r", encoding="utf-8").read())
        file = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            popupaction=Popup.PopupSaveCreate(text_frame.master, "Action?", "What to do with the previous file?")
            match popupaction:
                case 0:
                    pass
                case 1:
                    MenuButton.save_button_action(text_frame)
                    frame_load_file()
                case 2:
                    frame_load_file()
                case 3:
                    pass
    @staticmethod
    def create_buttons(master, values, iconset, text_frame, commandset=None):
        buttons = []
        commandset = {"Save": lambda: MenuButton.save_button_action(text_frame) ,"File": lambda: MenuButton.file_button_action(text_frame)}
        for i, value in enumerate(values):
            icon = iconset.get(value)
            command = commandset.get(value)
            btn = MenuButton(master, icon=icon, command=command, text=value if not icon else "")
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
            buttons.append(btn)
        return buttons
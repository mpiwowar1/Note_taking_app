import customtkinter as ct
from tkinter import filedialog
from .popup import Popup
from .config import Config,SaveConfig
from .footer import Footer
from .Checksum import HashString

class MenuButton(ct.CTkButton):
    def __init__(self, master, icon=None, command=None, text=""):
        if icon:
            super().__init__(master, text="", width=40, height=40, command=command, image=icon)
            self._set_appearance_mode(Config["Settings"]["Appearance"])
        else:
            super().__init__(master, text=text, width=40, height=40, command=command)
            self._set_appearance_mode(Config["Settings"]["Appearance"])
    @staticmethod
    def settings_button_action(text_frame,menu_frame,app_frame):
        SettingsWindow=Popup.SettingsPopupCreate(text_frame,menu_frame,app_frame)
    @staticmethod
    def save_button_action(text_frame):
        texttosave=text_frame.get_text()
        if Config["Last"] is None:
            file = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                title="Save File As"
            )
            if file:
                Config["Last"] = file
                SaveConfig()
                text_frame.footer.update_status()
            else:
                return 
        plik=open(Config["Last"],"w",encoding="utf-8")
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
        if Config["Last"] == file or not file:
            return
        if Config["Last"] is not None and HashString(text_frame.get_text()) != HashString(open(Config["Last"], "r", encoding="utf-8").read()):
            popupaction=Popup.PopupSaveCreate(text_frame.master, "Action?", "What to do with the previous file?")
            match popupaction:
                case 0:
                    pass
                case 1:
                    MenuButton.save_button_action(text_frame)
                    frame_load_file()
                    Config["Last"]=file
                    SaveConfig()
                case 2:
                    frame_load_file()
                    Config["Last"]=file
                    SaveConfig()
                case 3:
                    pass
        else:
            frame_load_file()
            Config["Last"]=file
            SaveConfig()
        text_frame.footer.update_status()
    @staticmethod
    def create_buttons(master, values, iconset, text_frame, commandset=None):
        buttons = []
        commandset = {"Save": lambda: MenuButton.save_button_action(text_frame) ,"File": lambda: MenuButton.file_button_action(text_frame),"Settings": lambda: MenuButton.settings_button_action(text_frame,master,master.master)}
        for i, value in enumerate(values):
            icon = iconset.get(value)
            command = commandset.get(value)
            btn = MenuButton(master, icon=icon, command=command, text=value if not icon else "")
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
            buttons.append(btn)
        return buttons
    @staticmethod
    def button_update(buttons):
        for btn in buttons:
            btn._set_appearance_mode(Config["Settings"]["Appearance"])
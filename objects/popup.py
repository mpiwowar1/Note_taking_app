import customtkinter as ct
from .window_manager import WindowAuto

class Popup(ct.CTkToplevel):
    def __init__(self, master, title, message):
        super().__init__(master)
        self.title(title)
        self.grab_set()
        self.result = None

        self.label = ct.CTkLabel(self, text=message)
        self.label.pack(pady=20)

    @staticmethod
    def PopupSaveCreate(master, title, message):
        popup = Popup(master, title, message)

        def onclick(value):
            popup.result = value
            popup.destroy()

        frame = ct.CTkFrame(popup)
        frame.pack(pady=10)
        WindowAuto(popup, 450, 150)

        ct.CTkButton(frame, text="Save", command=lambda: onclick(1)).grid(row=0, column=0, padx=5)
        ct.CTkButton(frame, text="Don't Save", command=lambda: onclick(2)).grid(row=0, column=1, padx=5)
        ct.CTkButton(frame, text="Cancel", command=lambda: onclick(3)).grid(row=0, column=2, padx=5)
        popup.wait_window()

        return popup.result
    @staticmethod
    def SettingsPopupCreate():
        settings_popup = Popup(None, "Settings", "Settings window placeholder")
        WindowAuto(settings_popup, 500, 300)
        settings_popup.wait_window()

        return

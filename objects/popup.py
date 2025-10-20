import customtkinter as ct

class Popup(ct.CTkToplevel):
    def __init__(self, master, title, message):
        super().__init__(master)
        self.title(title)
        self.geometry("450x150")
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

        ct.CTkButton(frame, text="Save", command=lambda: onclick(1)).grid(row=0, column=0, padx=5)
        ct.CTkButton(frame, text="Don't Save", command=lambda: onclick(2)).grid(row=0, column=1, padx=5)
        ct.CTkButton(frame, text="Cancel", command=lambda: onclick(3)).grid(row=0, column=2, padx=5)
        popup.wait_window()

        return popup.result

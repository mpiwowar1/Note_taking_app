import customtkinter as ct
from .window_manager import WindowAuto
from .config import Config,SaveConfig

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
    @staticmethod
    def SettingsPopupCreate(text_frame, menu_frame, app_frame):
        settings_popup = ct.CTkToplevel()
        settings_popup.title("Settings")
        WindowAuto(settings_popup, 700, 225)

        # --- Parent frame ---
        parent_frame = ct.CTkFrame(settings_popup)
        parent_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Configure columns for 3 frames
        for i in range(3):
            parent_frame.columnconfigure(i, weight=1)

        # --- Appearance frame ---
        appearance_frame = ct.CTkFrame(parent_frame)
        appearance_frame.grid(row=0, column=0, padx=10, sticky="nsew")
        ct.CTkLabel(appearance_frame, text="Appearance mode", font=("Arial", 16)).pack(pady=(0, 20))

        appearance_var = ct.StringVar(value=Config["Settings"]["Appearance"])
        options = ["Light", "Dark"]  # add "System" if you implement safe handling
        for option in options:
            ct.CTkRadioButton(appearance_frame, text=option, variable=appearance_var, value=option).pack(anchor="w", pady=5)

        # --- Font size frame ---
        size_frame = ct.CTkFrame(parent_frame)
        size_frame.grid(row=0, column=1, padx=10, sticky="nsew")
        ct.CTkLabel(size_frame, text="Font Size (px)", font=("Arial", 16)).pack(pady=(0, 20))

        font_size_var = ct.StringVar(value=str(Config["Settings"].get("FontSize", 14)))
        ct.CTkEntry(size_frame, textvariable=font_size_var).pack(fill="x", pady=5)

        # --- Font selection frame ---
        font_frame = ct.CTkFrame(parent_frame)
        font_frame.grid(row=0, column=2, padx=10, sticky="nsew")
        ct.CTkLabel(font_frame, text="Font", font=("Arial", 16)).pack(pady=(0, 20))

        font_list = ["Arial", "Calibri", "Times New Roman", "Courier New", "Verdana", "Helvetica"]
        font_var = ct.StringVar(value=Config["Settings"].get("Font", "Arial"))
        ct.CTkOptionMenu(font_frame, values=font_list, variable=font_var).pack(fill="x", pady=5)

        # --- Buttons frame ---
        button_frame = ct.CTkFrame(settings_popup)
        button_frame.pack(pady=10, fill="x", padx=20)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # --- Button callbacks ---
        def on_cancel():
            settings_popup.destroy()  # Safe destruction

        def on_save():
            # Update config safely
            Config["Settings"]["Appearance"] = appearance_var.get()
            try:
                font_size = int(font_size_var.get())
                if font_size <= 0:
                    raise ValueError
                Config["Settings"]["FontSize"] = font_size
            except ValueError:
                print("Invalid font size, keeping previous value.")
            Config["Settings"]["Font"] = font_var.get()

            # Save to JSON
            SaveConfig()

            # Apply settings to the main app
            if hasattr(app_frame, "AppUpdate"):
                try:
                    app_frame.AppUpdate()
                except Exception as e:
                    print("Error updating app:", e)

            # Destroy the popup safely after all pending callbacks
            settings_popup.after_idle(settings_popup.destroy)

        ct.CTkButton(button_frame, text="Save", command=on_save).grid(row=0, column=0, sticky="ew", padx=5)
        ct.CTkButton(button_frame, text="Cancel", command=on_cancel).grid(row=0, column=1, sticky="ew", padx=5)

        # Make the popup modal
        settings_popup.grab_set()
        settings_popup.wait_window()

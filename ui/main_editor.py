import tkinter as tk

from customtkinter import *

from ui.Editor import SaveManager, SimpleRunEditor


class MainEditor:
    def __init__(self):
        self.window = CTk()
        self.window.geometry("600x500")
        self.window.title("Save File Editor")
        self.window.attributes("-toolwindow")
        self.window.resizable(False, False)

        CTkLabel(self.window, text="Save File Editor", font=CTkFont(size=50)).pack(
            pady=5
        )

        vbox = CTkFrame(self.window, fg_color="transparent")
        vbox.pack(anchor="center", expand=True)

        self.create_button(vbox, "Save Manager", command=self.open_save_manager)
        self.create_button(
            vbox, "Simple Run Editor", command=self.open_simple_run_editor
        )

        card_container = CTkFrame(vbox, fg_color="transparent")
        self.create_button(
            card_container, "Card Editor", "left", command=self.open_card_editor
        )
        self.create_button(
            card_container,
            "Custom Deck Manager",
            "left",
            command=self.open_custom_deck_manager,
        )
        card_container.pack()
        event_container = CTkFrame(vbox, fg_color="transparent")
        self.create_button(
            event_container, "Event Editor", "left", command=self.open_event_editor
        )
        self.create_button(
            event_container,
            "Chalenge Manager",
            "left",
            command=self.open_chalenge_manager,
        )
        event_container.pack()
        self.create_button(
            vbox, "Timecapsule Editor", command=self.open_timecapsule_editor
        )

    def start(self):
        self.window.mainloop()

    def create_button(self, root, text, side="top", command=None):
        CTkButton(
            root,
            text=text,
            font=CTkFont(size=25),
            border_spacing=8,
            corner_radius=8,
            command=command,
        ).pack(side=side, pady=5, padx=5)

    def open_save_manager(self):
        SaveManager()

    def open_simple_run_editor(self):
        SimpleRunEditor()

    def open_card_editor(self):
        pass

    def open_custom_deck_manager(self):
        pass

    def open_event_editor(self):
        pass

    def open_chalenge_manager(self):
        pass

    def open_timecapsule_editor(self):
        pass

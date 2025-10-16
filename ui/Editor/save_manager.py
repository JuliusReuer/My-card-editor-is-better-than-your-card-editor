import shutil

from customtkinter import *

from data_loader import find_current_save_folder, load_run_data


class SaveManager(CTkToplevel):
    def __init__(self):
        super().__init__()
        self._running: bool = False

        self.title("Save Manager")
        self.lift()  # lift window on top
        self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(
            10, self._create_widgets
        )  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable

    def _create_widgets(self):
        self._label = CTkLabel(
            master=self,
            width=300,
            wraplength=300,
            fg_color="transparent",
            text="Save Manager",
            font=CTkFont(size=25),
        )
        self._label.pack()

        self._files_frame = CTkFrame(master=self, fg_color="transparent")
        self._files_frame.pack()

        savefiles = {
            "File 1": "savegame1.save",
            "File 2": "savegame2.save",
            "File 3": "savegame3.save",
        }
        self._create_run_frame("Current Run", "savegame.save")
        for title in savefiles:
            self._create_run_frame(title, savefiles[title])

    def _create_run_frame(self, title, file):
        frame = CTkFrame(master=self._files_frame, width=200, height=100)
        frame.pack(side="left", pady=10, padx=10)
        title_label = CTkLabel(frame, text=title, font=CTkFont(size=20, weight="bold"))
        title_label.pack()

        data = load_run_data(file)
        if data:
            other = data[3]
            CTkLabel(frame, text=f"Day: {other.Day}").pack()
            CTkLabel(frame, text=f"Coins: {other.Coins}").pack()
            CTkLabel(frame, text=f"StarterDeck: {other.get_deck_name()}").pack()
            CTkLabel(frame, text=f"Cards: {len(data[1])}").pack()
            CTkLabel(frame, text=f"Toys: {len(other.SelectedItemIds)}").pack()
        else:
            CTkLabel(frame, text=f"").pack()
            CTkLabel(frame, text=f"").pack()
            CTkLabel(frame, text=f"Empty").pack()
            CTkLabel(frame, text=f"").pack()
            CTkLabel(frame, text=f"").pack()

        if title != "Current Run":

            def save():
                shutil.copy2(
                    find_current_save_folder() + "\\savegame.save",
                    find_current_save_folder() + "\\" + file,
                )
                self._reload()

            def load():
                shutil.copy2(
                    find_current_save_folder() + "\\" + file,
                    find_current_save_folder() + "\\savegame.save",
                )
                self._reload()

            CTkButton(frame, text=f"Save Current Run", command=save).pack(
                pady=2, padx=2
            )
            CTkButton(frame, text=f"Load Run", command=load).pack(pady=2, padx=2)

    def _on_closing(self):
        self.grab_release()
        self.destroy()

    def _reload(self):
        for widget in self.winfo_children():
            widget.destroy()
        self._create_widgets()

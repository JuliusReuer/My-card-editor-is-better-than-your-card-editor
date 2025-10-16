from customtkinter import *

from classes.save_data.other import Item
from data_loader import (
    find_current_save_folder,
    load_run_data,
    load_toy_data,
    store_run_data,
)


class SimpleRunEditor(CTkToplevel):
    def __init__(self):
        super().__init__()
        self._running: bool = False

        self.title("Simple Run Editor")
        self.lift()  # lift window on top
        # self.attributes("-topmost", True)  # stay on top
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(
            1, self._create_widgets
        )  # create widgets with slight delay, to avoid white flickering of background
        self.resizable(False, False)
        self.grab_set()  # make other windows not clickable

        self.run_data = load_run_data()

    def _create_widgets(self):
        self.grid_columnconfigure((0, 2), weight=1)
        self.rowconfigure(0, weight=1)
        self._label = CTkLabel(
            master=self,
            width=300,
            wraplength=300,
            fg_color="transparent",
            text="Simple Run Editor",
            font=CTkFont(size=25),
        )
        self._label.grid(columnspan=2)

        if self.run_data == None:
            CTkLabel(self, text="Sorry there is no Current Run").grid(
                columnspan=2, row=1
            )
            return

        def number_check(x: str):
            return x.isdigit() or x == ""

        # region Coin
        coin_label = CTkLabel(self, text="Coins :")
        coin_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self._coin_variable = StringVar(self, self.run_data[3].Coins, "Coins")
        self._max_hand_variable = StringVar(
            self, self.run_data[3].MaxHandSize, "MaxHandSize"
        )

        coin_edit = CTkEntry(
            self,
            textvariable=self._coin_variable,
            justify="right",
            validate="key",
            validatecommand=(self.register(number_check), "%P"),
        )
        coin_edit.grid(row=1, column=1)
        # endregion

        # region Max Hand
        max_hand_label = CTkLabel(self, text="Max Hand Size :")
        max_hand_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        max_hand_edit = CTkEntry(
            self,
            textvariable=self._max_hand_variable,
            justify="right",
            validate="key",
            validatecommand=(self.register(number_check), "%P"),
        )
        max_hand_edit.grid(row=2, column=1)
        # endregion

        # region Current Toys
        self._current_toy_container = CTkFrame(self)
        self._current_toy_container.grid(row=3, column=0, padx=5, pady=5, sticky=S)
        self._current_toy_list = CTkScrollableFrame(
            self._current_toy_container, fg_color="transparent"
        )
        self._current_toy_list.pack(fill=BOTH)
        self._current_toy_description = CTkFrame(self._current_toy_container)
        self._current_toy_description.pack()
        self._current_toy_description_label = CTkLabel(
            self._current_toy_description, text="", width=300, wraplength=300
        )
        self._current_toy_description_label.pack()

        def remove_toy(event, toy):
            self.run_data[3].SelectedItemIds.remove(toy)
            for child in self._current_toy_list.winfo_children():
                child.destroy()
            self.make_toy_list(
                self.run_data[3].SelectedItemIds,
                self._current_toy_list,
                self._current_toy_description_label,
                remove_toy,
            )

        self.make_toy_list(
            self.run_data[3].SelectedItemIds,
            self._current_toy_list,
            self._current_toy_description_label,
            remove_toy,
        )
        # endregion

        # region Toy List
        self._toy_list_container = CTkFrame(self)
        self._toy_list_container.grid(row=3, column=1, padx=5, pady=5)
        # region Filter
        self._toy_list_filter = CTkFrame(self._toy_list_container)
        self._toy_list_filter.pack(fill=BOTH)
        # Action Word
        self._action_word_filter = CTkOptionMenu(
            self._toy_list_filter, values=["ALL", "Gain", "Add", "Increase", "Decrease"]
        )
        self._action_word_filter.pack()
        # Key Word
        self._key_word_filter = CTkOptionMenu(
            self._toy_list_filter,
            values=["ALL", "Star", "Fav", "Card", "BonBon", "Feaver", "Discard", "Bug"],
        )
        self._key_word_filter.pack()
        # endregion

        self._toy_list = CTkScrollableFrame(
            self._toy_list_container, fg_color="transparent"
        )
        self._toy_list.pack(fill=BOTH)
        full_list = []
        for item in Item:
            full_list.append(item.value)

        self._toy_description = CTkFrame(self._toy_list_container)
        self._toy_description.pack()
        self._toy_description_label = CTkLabel(
            self._toy_description, text="", width=300, wraplength=300
        )
        self._toy_description_label.pack()

        def add_toy(event, toy):
            self.run_data[3].SelectedItemIds.append(toy)
            for child in self._current_toy_list.winfo_children():
                child.destroy()
            self.make_toy_list(
                self.run_data[3].SelectedItemIds,
                self._current_toy_list,
                self._current_toy_description_label,
                remove_toy,
            )

        self.make_toy_list(
            full_list, self._toy_list, self._toy_description_label, add_toy
        )
        # endregion

    def make_toy_list(
        self,
        toys: list[str],
        list_frame: CTkScrollableFrame,
        description: CTkLabel,
        click_event: callable,
    ):
        data = load_toy_data()

        def enter(event, toy):
            if toy in data:
                description.configure(text=data[toy]["Effect"])

        for toy in toys:
            name = toy
            bg_color = "red"
            if toy in data:
                name = data[toy]["ToyName"]
                bg_color = "green"
            l = CTkLabel(list_frame, text=name, bg_color=bg_color)
            l.pack(fill=BOTH)

            l.bind("<Enter>", lambda x, t=toy: enter(x, t))
            l.bind("<ButtonPress>", lambda x, t=toy: click_event(x, t))

    def _on_closing(self):
        if self.run_data:
            (header, cards, stickerbook, other) = self.run_data
            other.Coins = int(self._coin_variable.get())
            other.MaxHandSize = int(self._max_hand_variable.get())
            store_run_data(header, cards, stickerbook, other)
        self.grab_release()
        self.destroy()

    def _reload(self):
        for widget in self.winfo_children():
            widget.destroy()
        self._create_widgets()

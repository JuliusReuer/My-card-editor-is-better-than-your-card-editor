import csv
import json
import os

from classes import DataClassUnpack
from classes.save_data import Event, EventData, Item, Other
from classes.save_data.cards import Card, CardBackground, Effect, Sticker
from const import SAVEPATH


def find_current_save_folder() -> str:
    for entry in os.listdir(SAVEPATH):
        if os.path.isdir(SAVEPATH + entry):
            return SAVEPATH + entry


def load_run_data(
    file_name="savegame.save",
) -> tuple[str, list[Card], list[Sticker], Other] | None:
    save_file_path = f"{find_current_save_folder()}\\{file_name}"
    if not os.path.exists(save_file_path):
        return None
    header: str
    cards: list[Card] = []
    other: Other
    stickerbook: list[Sticker] = []
    with open(save_file_path) as file:
        lines = file.readlines()
        header = lines[0]
        for line in lines[1:]:
            arg = json.loads(line)

            if "Filename" in arg:
                n: str = arg["Filename"]
                if n.startswith("res://Content/Cards/"):
                    cards.append(DataClassUnpack.instantiate(Card, arg))
                else:
                    cards[-1].effects.append(DataClassUnpack.instantiate(Effect, arg))
            else:
                if "Coins" not in arg:
                    if (
                        arg["Parent"]
                        == "/root/StartScene/StickerBook/StickerBookScrollContainer/Panel"
                    ):
                        stickerbook.append(DataClassUnpack.instantiate(Sticker, arg))
                    else:
                        cards[-1].stickers.append(
                            DataClassUnpack.instantiate(Sticker, arg)
                        )

                else:
                    arg["CompletedAchievements"] = json.loads(
                        arg["CompletedAchievements"]
                    )
                    loopData = json.loads(arg["CoreLoopData"])
                    data = []
                    for event_data in loopData:
                        event: Event = DataClassUnpack.instantiate(Event, event_data)
                        EventData.parse_event(event, event_data)
                        data.append(event)

                    arg["RunStats"] = json.loads(arg["RunStats"])
                    arg["SelectedItemIds"] = json.loads(arg["SelectedItemIds"])
                    other = DataClassUnpack.instantiate(Other, arg)
                    other.CoreLoop = data
    return header, cards, stickerbook, other


def store_run_data(
    header: str, cards: list[Card], stickerbook: list[Sticker], other: Other
):
    save_file_path = f"{find_current_save_folder()}\\savegame.save"
    lines = []

    lines.append(header)
    for card in cards:
        lines.append(str(card) + "\n")
        for sticker in card.stickers:
            lines.append(str(sticker) + "\n")
        for effect in card.effects:
            lines.append(str(effect) + "\n")
    for sticker in stickerbook:
        lines.append(str(sticker) + "\n")
    lines.append(str(other))

    with open(save_file_path, "+w") as file:
        file.writelines(lines)


def load_toy_data():
    toys = {}
    with open("data/toy_data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            toys[row["ToyId"]] = row
    return toys


def load_character_data():
    toys = {}
    with open("data/character_data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            toys[row["CharacterId"]] = row
    return toys

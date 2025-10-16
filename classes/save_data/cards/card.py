import json
from dataclasses import dataclass, field
from enum import Enum

from classes.save_data.cards.effect import Effect
from classes.save_data.cards.sticker import Sticker


class CardBackground(Enum):
    HOLO = "res://Content/Cards/Card_Holo.tscn"
    BLUE = "res://Content/Cards/Card_Blue.tscn"
    PURPLE = "res://Content/Cards/Card_Purple.tscn"


@dataclass
class Card:
    Filename: str
    Index: int
    Parent: str
    PosX: float
    PosY: float
    UniqueId: str
    name: str
    stickers: list[Sticker] = field(default_factory=list[Sticker])
    effects: list[Effect] = field(default_factory=list[Effect])

    def set_background(self, background: CardBackground):
        self.Filename = background.value

    def __str__(self):
        return json.dumps(
            {
                "Filename": self.Filename,
                "Index": self.Index,
                "Parent": self.Parent,
                "PosX": self.PosX,
                "PosY": self.PosY,
                "UniqueId": self.UniqueId,
                "name": self.name,
            }
        )

import json
from dataclasses import dataclass
from enum import Enum


class StickerStyle(Enum):
    NONE = 0
    HOLO = 1
    GOLD = 2  # Double Activate


@dataclass
class Sticker:
    Index: int
    IsHolographic: int
    Parent: str
    PosX: float
    PosY: float
    SizeX: float
    SizeY: float
    StickerId: str
    name: str
    rotation: float

    def __str__(self):
        return json.dumps(
            {
                "Index": self.Index,
                "IsHolographic": self.IsHolographic,
                "Parent": self.Parent,
                "PosX": self.PosX,
                "PosY": self.PosY,
                "SizeX": self.SizeX,
                "SizeY": self.SizeY,
                "StickerId": self.StickerId,
                "name": self.name,
                "rotation": self.rotation,
            }
        )

from dataclasses import dataclass
import json


@dataclass
class Effect:
    Filename: str
    Index: str
    Parent: str
    PosX: float
    PosY: float
    Priority: float
    StickerResourceType: str
    name: str

    def __str__(self):
        return json.dumps(
            {
                "Filename": self.Filename,
                "Index": self.Index,
                "Parent": self.Parent,
                "PosX": self.PosX,
                "PosY": self.PosY,
                "Priority": self.Priority,
                "StickerResourceType": self.StickerResourceType,
                "name": self.name,
            }
        )

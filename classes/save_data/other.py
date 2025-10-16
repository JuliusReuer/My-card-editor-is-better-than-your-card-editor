import json
from dataclasses import dataclass, field
from enum import Enum

from classes.save_data.event import Event


class Item(Enum):
    ROBOT = "Shield"
    SWIMRING = "KnightHelmet"
    BALL8 = "ToyCar"
    SWEEDS_BAND = "HalloweenPumpkin"
    STAR_ORB = "Swing"
    ROLLER_SHOES = "RollerShoes"
    HANDHELD = "Handheld"
    PLANT = "Leaf"
    CASETTE_PLAYER = "Guitar"
    DUCK = "Bicycle"
    ETCHESKETCH = "Stethoscope"
    SOAP_BUBLES = "GardenHose"
    STICKY_HAND = "StickyHand"
    BUG_CONTAINER = "BugContainer"
    POGO_STICK = "PogoStick"
    BUCKET = "Bucket"
    TEDDY_BEAR = "TeddyBear"
    LAVA_LAMP = "LavaLamp"
    FLUFFY = "Fluffy"
    CRAYON = "Crayon"
    BUG_JAR = "BugJar"
    CANDY_TOY = "CandyToy"
    BAG_OF_CANDY = "BagOfCandy"
    ROBO_DOG = "RoboDog"
    GAME_CONTROLER = "GameControler"
    SPRING = "GameConsole"
    EXCAVATOR = "Excavator"
    VIRTUAL_PET = "VirtualPet"
    RC_CAR = "RCCar"
    Mermaid = "?"
    Trrarium = "?"
    Aquarium = "?"


@dataclass
class Other:
    ChosenStarterPackId: str
    Coins: int
    CompletedAchievements: list[str]
    Day: int
    DifficultyLevel: int
    MaxHandSize: int
    Motivation: int
    RNGSeed: int
    RNGState: int
    RunStats: object
    SelectedItemIds: list[str]
    StarterUnlockPercentage: int
    TreasureCoins: int

    CoreLoop: list[Event] = field(default_factory=list[Event])

    def add_item(self, item: Item):
        self.SelectedItemIds.append(item.value)

    def remove_item(self, item: Item):
        self.SelectedItemIds.remove(item.value)

    def get_deck_name(self) -> str:
        match self.ChosenStarterPackId:
            case "Starter1":
                return "Star Deck"
            case "Starter3":
                return "Bug Deck"
            case _:
                return self.ChosenStarterPackId

    def __str__(self):
        CoreLoop = []
        for event in self.CoreLoop:
            CoreLoop.append(event.toDict())
        return json.dumps(
            {
                "ChosenStarterPackId": self.ChosenStarterPackId,
                "Coins": self.Coins,
                "CompletedAchievements": json.dumps(self.CompletedAchievements),
                "CoreLoopData": json.dumps(CoreLoop),
                "Day": self.Day,
                "DifficultyLevel": self.DifficultyLevel,
                "MaxHandSize": self.MaxHandSize,
                "Motivation": self.Motivation,
                "RNGSeed": self.RNGSeed,
                "RNGState": self.RNGState,
                "RunStats": json.dumps(self.RunStats),
                "SelectedItemIds": json.dumps(self.SelectedItemIds),
                "StarterUnlockPercentage": self.StarterUnlockPercentage,
                "TreasureCoins": self.TreasureCoins,
            }
        )

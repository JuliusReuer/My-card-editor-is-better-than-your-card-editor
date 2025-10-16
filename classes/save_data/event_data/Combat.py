from dataclasses import dataclass

from classes.save_data.event import Event, EventData


@dataclass
class Combat(EventData):
    Id: str
    CombatPoolId: str
    OpponentId: str
    BackgroundPath: str
    Weight: int
    RandomRewardPoolId: str
    MinQuantity: int
    MaxQuantity: int
    FixedRewardPoolId: str
    CoinReward: int
    Fav: int
    UnlockRequirements: list[str]
    AnyOneOfUnlockRequirements: list[str]

    def toDict(self):
        return {
            "Id": self.Id,
            "CombatPoolId": self.CombatPoolId,
            "OpponentId": self.OpponentId,
            "BackgroundPath": self.BackgroundPath,
            "Weight": self.Weight,
            "RandomRewardPoolId": self.RandomRewardPoolId,
            "MinQuantity": self.MinQuantity,
            "MaxQuantity": self.MaxQuantity,
            "FixedRewardPoolId": self.FixedRewardPoolId,
            "CoinReward": self.CoinReward,
            "Fav": self.Fav,
            "UnlockRequirements": self.UnlockRequirements,
            "AnyOneOfUnlockRequirements": self.AnyOneOfUnlockRequirements,
        }

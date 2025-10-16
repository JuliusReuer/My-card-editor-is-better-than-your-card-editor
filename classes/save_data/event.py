import json
from dataclasses import dataclass, field

from classes.DataClassUnpack import DataClassUnpack


@dataclass
class EventData:
    @classmethod
    def parse_event(cls, event: "Event", event_data):
        match event.EventId:
            case "ScheduleSelection":
                from classes.save_data.event_data import ScheduleSelection

                scsl = ScheduleSelection([], [])
                data = json.loads(event_data["AdditionalStateInfoObject"])
                for new_event_data in data["Selection1SectionStates"]:
                    new_event: Event = DataClassUnpack.instantiate(
                        Event, new_event_data
                    )
                    EventData.parse_event(new_event, new_event_data)
                    scsl.Selection1SectionStates.append(new_event)
                for new_event_data in data["Selection2SectionStates"]:
                    new_event: Event = DataClassUnpack.instantiate(
                        Event, new_event_data
                    )
                    EventData.parse_event(new_event, new_event_data)
                    scsl.Selection2SectionStates.append(new_event)
                event.AdditionalStateInfo = scsl
            case s if s.startswith("Combat-") or s.startswith("Boss-"):
                from classes.save_data.event_data import Combat
                from data_loader import load_character_data

                info: Combat = DataClassUnpack.instantiate(
                    Combat, json.loads(event_data["AdditionalStateInfoObject"])
                )

                char_data = load_character_data()
                opponent = info.OpponentId.split("-")
                for part in opponent:
                    if part.startswith("D"):
                        opponent.remove(part)
                opponent_id = "-".join(opponent)
                if opponent_id not in char_data:
                    print("Unknown Character: ", info.OpponentId)
                event.AdditionalStateInfo = info

            case _:
                if event_data["AdditionalStateInfoObject"] != "":
                    print(event_data["AdditionalStateInfoObject"])
                event.AdditionalStateInfo = None

    def toDict(self):
        return None


@dataclass
class Event:
    EventId: str
    State: int
    HideInCalendarView: bool
    Day: int
    DontShowScheduleAfter: bool
    AdditionalStateInfo: EventData | None = field(default_factory=EventData)

    def toDict(self):
        info = ""
        if self.AdditionalStateInfo != None:
            info_data = self.AdditionalStateInfo.toDict()

            if info_data != None:
                info = json.dumps(info_data)
        return {
            "EventId": self.EventId,
            "State": self.State,
            "HideInCalendarView": self.HideInCalendarView,
            "AdditionalStateInfoObject": info,
            "Day": self.Day,
            "DontShowScheduleAfter": self.DontShowScheduleAfter,
        }

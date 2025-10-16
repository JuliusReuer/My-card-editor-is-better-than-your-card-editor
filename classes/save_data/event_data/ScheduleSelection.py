from dataclasses import dataclass

from classes.save_data.event import Event, EventData


@dataclass
class ScheduleSelection(EventData):
    Selection1SectionStates: list[Event]
    Selection2SectionStates: list[Event]

    def toDict(self):
        Selection1SectionStates_data = []
        for event in self.Selection1SectionStates:
            Selection1SectionStates_data.append(event.toDict())
        Selection2SectionStates_data = []
        for event in self.Selection2SectionStates:
            Selection2SectionStates_data.append(event.toDict())
        return {
            "Selection1SectionStates": Selection1SectionStates_data,
            "Selection2SectionStates": Selection2SectionStates_data,
        }

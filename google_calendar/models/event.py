from datetime import datetime

from pydantic import BaseModel, Field

from .attendee import Attendee
from .creator import Creator
from .event_time import EventTime
from .organizer import Organizer
from .resource import Resource


class Event(Resource):
    status: str
    html_link: str
    created: datetime
    updated: datetime
    summary: str
    description: str
    location: str
    color_id: str
    creator: Creator
    organizer: Organizer
    start: EventTime
    end: EventTime
    end_time_unspecified: bool
    recurrence: list[str] = Field(default_factory=list)
    recurring_event_id: str
    original_start_time: EventTime
    transparency: str
    visibility: str
    icaluid: str
    sequence: int
    attendees: list[Attendee] = Field(default_factory=list)

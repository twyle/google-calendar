from datetime import datetime

from pydantic import BaseModel, Field

from .attachment import Attachment
from .attendee import Attendee
from .conference_data import ConferenceData
from .creator import Creator
from .event_time import EventTime
from .focus_time_properties import FocusTimeProperties
from .organizer import Organizer
from .out_of_office_properties import OutOfficeProperties
from .reminders import Reminders
from .resource import Resource
from .source import Source
from .working_location_properties import WorkingLocationProperties


class Event(Resource):
    status: str = ''
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
    attendees_omitted: bool
    hangout_link: str
    color_id: str
    conference_data: ConferenceData
    etag: str
    event_type: str
    id: str
    kind: str
    location: str
    locked: bool
    out_of_office_properties: OutOfficeProperties
    focus_time_properties: FocusTimeProperties
    private_copy: bool
    attachments: list[Attachment] = Field(default_factory=list)
    working_location_properties: WorkingLocationProperties
    source: Source
    reminders: Reminders
    guests_can_invite_others: bool
    guests_can_modify: bool
    guests_can_see_other_guests: bool

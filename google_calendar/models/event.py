from datetime import datetime

from pydantic import Field

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
    creator: Creator
    end: EventTime
    etag: str
    event_type: str
    html_link: str
    icaluid: str
    id: str
    kind: str
    organizer: Organizer
    sequence: int
    start: EventTime
    summary: str

    attachments: list[Attachment] = Field(default_factory=list)
    attendees_omitted: bool = False
    attendees: list[Attendee] = Field(default_factory=list)
    color_id: str = ''
    conference_data: ConferenceData = None
    created: datetime = None
    description: str = ''
    end_time_unspecified: bool = False
    focus_time_properties: FocusTimeProperties = None
    guests_can_invite_others: bool = True
    guests_can_modify: bool = False
    guests_can_see_other_guests: bool = True
    hangout_link: str = ''
    location: str = ''
    locked: bool = False
    original_start_time: EventTime = None
    out_of_office_properties: OutOfficeProperties = None
    private_copy: bool = False
    recurrence: list[str] = Field(default_factory=list)
    recurring_event_id: str = ''
    reminders: Reminders = None
    source: Source = None
    status: str = ''
    transparency: str = ''
    updated: datetime = None
    visibility: str = ''
    working_location_properties: WorkingLocationProperties = None

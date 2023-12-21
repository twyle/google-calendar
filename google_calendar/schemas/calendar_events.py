from typing import Optional

from pydantic import BaseModel, Field

from ..models import (
    Attachment,
    ConferenceData,
    FocusTimeProperties,
    OutOfficeProperties,
    Resource,
    Source,
    WorkingLocationProperties,
)
from .attendee import Attendee
from .calendar_request import CalendarRequest
from .default_reminder import DefaultReminder
from .event_time import EventTime
from .reminders import Reminders


class ListCalendarEvents(CalendarRequest):
    calendarId: str = 'primary'


class ListCalendarEventsResponse(BaseModel):
    kind: str
    etag: str
    summary: str
    description: str
    updated: str
    time_zone: str
    access_role: str
    default_reminders: list[DefaultReminder] = Field(default_factory=list)
    items: list[Resource] = Field(default_factory=list)
    next_page_token: str = None
    next_sync_token: str = None


class CreateEvent(BaseModel):
    start: EventTime
    end: EventTime
    summary: str
    attachments: list[Attachment] = Field(default_factory=list)
    attendees: list[Attendee] = Field(default_factory=list)
    colorId: Optional[str] = ''
    conference_data: Optional[ConferenceData] = None
    description: Optional[str] = ''
    event_type: Optional[str] = ''
    focused_time_properties: Optional[FocusTimeProperties] = None
    id: Optional[str] = ''
    location: Optional[str] = ''
    original_start_time: Optional[EventTime] = None
    out_of_office_properties: Optional[OutOfficeProperties] = None
    recurrence: list[str] = Field(default_factory=list)
    reminders: Optional[Reminders] = None
    sequence: Optional[int] = None
    source: Optional[Source] = None
    transparency: Optional[str] = ''
    visibility: Optional[str] = ''
    working_location_properties: Optional[WorkingLocationProperties] = None

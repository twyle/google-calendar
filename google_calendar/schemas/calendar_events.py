from pydantic import BaseModel, Field

from ..models import Resource
from .calendar_request import CalendarRequest
from .default_reminder import DefaultReminder


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
    # items: list[Resource] = Field(default_factory=list)
    items: list[dict] = Field(default_factory=list)
    next_page_token: str = None
    next_sync_token: str = None

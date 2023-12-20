from ..models import Calendar
from ..schemas import CreateCalendar, PatchCalendar, UpdateCalendar
from .resource import Resource


class CalendarResource(Resource):
    def clear_calendar(self, calendar_id: str = 'primary') -> None:
        self.calendar_client.calendars().clear(calendar_id).execute()

    def delete_calendar(self, secondary_calendar_id: str) -> None:
        self.calendar_client.calendars().delete(
            calendarId=secondary_calendar_id
        ).execute()

    def get_calendar(self, calendar_id: str = 'primary') -> Calendar:
        self.calendar_client.calendars().get(calendarId=calendar_id).execute()

    def create_calendar(self, calendar: CreateCalendar) -> Calendar:
        raise NotImplementedError()

    def patch_calendar(self, calendar: PatchCalendar) -> Calendar:
        raise NotImplementedError()

    def update_calendar(self, calendar: UpdateCalendar) -> Calendar:
        raise NotImplementedError()

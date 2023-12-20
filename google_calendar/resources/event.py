from ..models import Event
from ..schemas import (
    EventInstances,
    EventInstancesResponse,
    EventSchema,
    ListCalendarEvents,
    ListCalendarEventsResponse,
    PatchEventSchema,
    UpdateEventSchema,
)
from .resource import Resource


class EventResource(Resource):
    def create_event(self) -> Event:
        event = {
            'summary': 'Google I/O 2015',
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': "A chance to hear more about Google's developer products.",
            'start': {
                'dateTime': '2015-05-28T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': '2015-05-28T17:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'recurrence': ['RRULE:FREQ=DAILY;COUNT=2'],
            'attendees': [
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = (
            self.calendar_client.events()
            .insert(calendarId='primary', body=event)
            .execute()
        )
        return event

    def get_event(
        self,
        event_id: str,
        calendar_id: str = 'primary',
        max_attendees: int = None,
        time_zone: str = None,
    ) -> Event:
        event = (
            self.calendar_client.events()
            .get(calendarId=calendar_id, eventId=event_id)
            .execute()
        )
        return event

    def delete_event(
        self,
        event_id: str,
        calendar_id: str = 'primary',
        send_notifications: bool = False,
        send_updates: str = 'all',
    ) -> None:
        self.calendar_client.events().delete(
            calendarId=calendar_id, eventId=event_id
        ).execute()

    def import_event(
        self,
        event_schema: EventSchema,
        calendar_id: str = 'primary',
        conference_data_version: int = 0,
        supports_attachment: bool = False,
    ):
        raise NotImplementedError()

    def get_recurring_event_instances(
        self, event_instance: EventInstances
    ) -> EventInstancesResponse:
        raise NotImplementedError()

    def list_calendar_events(
        self, list_calendar_events: ListCalendarEvents
    ) -> ListCalendarEventsResponse:
        raise NotImplementedError()

    def move_event(
        self,
        event_id: str,
        destination: str,
        calendar_id: str = 'primary',
        send_notifications: bool = False,
        send_updates: str = 'all',
    ) -> Event:
        raise NotImplementedError()

    def update_event(self, update: UpdateEventSchema) -> Event:
        raise NotImplementedError()

    def patch_event(self, patch: PatchEventSchema) -> Event:
        raise NotImplementedError()

    def quick_add(
        self,
        text: str,
        calendar_id: str = 'primary',
        send_notifications: bool = False,
        send_updates: str = 'all',
    ) -> Event:
        raise NotImplementedError()

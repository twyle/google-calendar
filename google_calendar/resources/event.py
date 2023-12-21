from typing import Any

from ..models import Creator, Event, EventTime, Organizer, Person
from ..schemas import (
    CalendarRequest,
    CreateEvent,
    DefaultReminder,
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
    def create_request_dict(self, request: CalendarRequest) -> dict[str, Any]:
        request_dict: dict[str, Any] = dict()
        for key, value in request.model_dump().items():
            if value:
                request_dict[key] = value
        return request_dict

    def parse_default_reminder(self, default_reminder: dict) -> DefaultReminder:
        return DefaultReminder(
            method=default_reminder['method'], minutes=default_reminder['minutes']
        )

    def parse_default_reminders(
        self, default_reminders: list[dict]
    ) -> list[DefaultReminder]:
        reminders: list[DefaultReminder] = list()
        for reminder in default_reminders:
            reminders.append(self.parse_default_reminder(reminder))
        return reminders

    def parse_person(self, person: dict[str, Any]) -> Person:
        parsed_person: dict = dict()
        parsed_person['email'] = person['email']
        parsed_person['display_name'] = person.get('displayName', '')
        parsed_person['self_'] = person.get('self', False)
        return Person(**parsed_person)

    def parse_event_time(self, event_time: dict) -> EventTime:
        parsed_time: dict = dict()
        parsed_time['time_zone'] = event_time.get('timeZone', '')
        parsed_time['date_'] = event_time.get('date', None)
        parsed_time[''] = event_time.get('dateTime', None)
        return EventTime(**parsed_time)

    def parse_item(self, item: dict[str, Any]) -> Event:
        parsed_item: dict[str, Any] = dict()
        parsed_item['created'] = item['created']
        parsed_item['updated'] = item['updated']
        parsed_item['id'] = item['id']
        parsed_item['kind'] = item['kind']
        parsed_item['etag'] = item['etag']
        parsed_item['icaluid'] = item['iCalUID']
        parsed_item['sequence'] = item['sequence']
        parsed_item['html_link'] = item['htmlLink']
        parsed_item['event_type'] = item['eventType']
        parsed_item['summary'] = item['summary']
        parsed_item['creator'] = Creator(
            **self.parse_person(item['creator']).model_dump()
        )
        parsed_item['organizer'] = Organizer(
            **self.parse_person(item['organizer']).model_dump()
        )
        parsed_item['start'] = self.parse_event_time(item['start'])
        parsed_item['end'] = self.parse_event_time(item['end'])
        return Event(**parsed_item)

    def parse_items(self, items: dict[str, Any]) -> list[Event]:
        parsed_items: list[Event] = list()
        for item in items:
            try:
                parsed_items.append(self.parse_item(item))
            except KeyError:
                pass
        return parsed_items

    def parse_list_calendar_events(
        self, calendar_response: dict[str, Any]
    ) -> ListCalendarEventsResponse:
        parsed_response: dict[str, Any] = dict()
        parsed_response['kind'] = calendar_response['kind']
        parsed_response['etag'] = calendar_response['etag']
        parsed_response['summary'] = calendar_response['summary']
        parsed_response['description'] = calendar_response['description']
        parsed_response['updated'] = calendar_response['updated']
        parsed_response['time_zone'] = calendar_response['timeZone']
        parsed_response['access_role'] = calendar_response['accessRole']
        parsed_response['default_reminders'] = self.parse_default_reminders(
            calendar_response['defaultReminders']
        )
        parsed_response['next_page_token'] = calendar_response.get('nextPageToken', '')
        parsed_response['next_sync_token'] = calendar_response.get('nextSyncToken', '')
        parsed_response['items'] = self.parse_items(calendar_response['items'])
        return ListCalendarEventsResponse(**parsed_response)

    def create_event(self, event_schema: CreateEvent) -> Event:
        event = {
            'summary': 'Google I/O 2015',
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': "A chance to hear more about Google's developer products.",
            'start': {
                'dateTime': '2023-12-21T12:11:36.355536Z',
                'timeZone': 'Africa/Nairobi',
            },
            'end': {
                'dateTime': '2023-12-21T14:11:36.355561Z',
                'timeZone': 'Africa/Nairobi',
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
            .insert(calendarId='primary', body=self.create_request_dict(event_schema))
            .execute()
        )
        return self.parse_item(event)

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
        return self.parse_item(event)

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
        request_dict: dict[str, Any] = self.create_request_dict(list_calendar_events)
        calendar_events = self.calendar_client.events().list(**request_dict).execute()
        return self.parse_list_calendar_events(calendar_events)

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
        created_event = (
            self.calendar_client.events()
            .quickAdd(calendarId='primary', text=text)
            .execute()
        )
        return self.parse_item(created_event)

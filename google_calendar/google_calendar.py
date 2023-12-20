from typing import Any, Optional

from oryks_google_oauth import GoogleCalendarScopes, GoogleOAuth
from pydantic import BaseModel, Field

from .models import Event
from .resources import EventResource
from .schemas import (
    EventInstances,
    EventInstancesResponse,
    EventSchema,
    ListCalendarEvents,
    ListCalendarEventsResponse,
)


class GoogleCalendar(BaseModel):
    secret_file: Optional[str] = None
    api_service_name: Optional[str] = 'calendar'
    api_version: Optional[str] = 'v3'
    credentials_dir: Optional[str] = '.calendar'
    scopes: Optional[list[str]] = Field(
        default=[
            GoogleCalendarScopes.calendar.value,
            GoogleCalendarScopes.calendar_events.value,
            GoogleCalendarScopes.calendar_settings_readonly.value,
        ]
    )
    calendar_client: Optional[Any] = None

    def authenticate(self, secret_file: Optional[str] = None) -> None:
        if secret_file:
            self.secret_file = secret_file
        if not self.secret_file:
            raise ValueError('The secret file was not provided.')
        oauth: GoogleOAuth = GoogleOAuth(
            secrets_file=self.secret_file,
            scopes=self.scopes,
            api_service_name=self.api_service_name,
            api_version=self.api_version,
            credentials_dir=self.credentials_dir,
        )
        self.calendar_client = oauth.authenticate_google_server()

    def create_event(self) -> Event:
        event_resource: EventResource = EventResource(
            calendar_client=self.calendar_client
        )
        return event_resource.create_event()

    def delete_event(
        self,
        event_id: str,
        calendar_id: str = 'primary',
        send_notifications: bool = False,
        send_updates: str = 'all',
    ) -> None:
        event_resource: EventResource = EventResource(
            calendar_client=self.calendar_client
        )
        return event_resource.delete_event(
            event_id, calendar_id, send_notifications, send_updates
        )

    def get_event(
        self,
        event_id: str,
        calendar_id: str = 'primary',
        max_attendees: int = None,
        time_zone: str = None,
    ) -> Event:
        event_resource: EventResource = EventResource(
            calendar_client=self.calendar_client
        )
        return event_resource.get_event(event_id, calendar_id, max_attendees, time_zone)

    def import_event(
        self,
        event_schema: EventSchema,
        calendar_id: str = 'primary',
        conference_data_version: int = 0,
        supports_attachment: bool = False,
    ):
        event_resource: EventResource = EventResource(
            calendar_client=self.calendar_client
        )
        return event_resource.import_event(
            event_schema, calendar_id, conference_data_version, supports_attachment
        )

    def get_recurring_event_instances(
        self, event_instance: EventInstances
    ) -> EventInstancesResponse:
        event_resource: EventResource = EventResource(
            calendar_client=self.calendar_client
        )
        return event_resource.get_recurring_event_instances(event_instance)

    def list_calendar_events(
        self, list_calendar_events: ListCalendarEvents
    ) -> ListCalendarEventsResponse:
        event_resource: EventResource = EventResource(
            calendar_client=self.calendar_client
        )
        return event_resource.get_recurring_event_instances(list_calendar_events)
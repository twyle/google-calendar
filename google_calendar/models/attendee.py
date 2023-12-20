from pydantic import BaseModel

from .person import Person


class Attendee(BaseModel):
    person: Person
    organizer: bool
    resource: bool
    optional: bool
    response_status: str
    comment: str
    additional_guests: int

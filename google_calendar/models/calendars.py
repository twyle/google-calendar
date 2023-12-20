from .conference_properties import ConferenceProperty
from .resource import Resource


class Calendar(Resource):
    summary: str
    description: str
    location: str
    time_zone: str
    conference_property: ConferenceProperty

from pydantic import BaseModel

from .office_location import OfficeLocation


class CustomLocation(BaseModel):
    label: str


class WorkingLocationProperties(BaseModel):
    type: str
    home_office: str
    custom_location: CustomLocation
    office_location: OfficeLocation

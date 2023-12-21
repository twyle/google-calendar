from pydantic import BaseModel
from typing import Optional


class Attendee(BaseModel):
    email: str
    additionalGuests: Optional[int] = 0
    comment: Optional[str] = ''
    displayName: Optional[str] = ''
    optional: Optional[bool] = False
    resource: Optional[bool] = False
    responseStatus: Optional[str] = ''

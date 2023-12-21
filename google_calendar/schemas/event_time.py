from typing import Optional

from pydantic import BaseModel


class EventTime(BaseModel):
    dateTime: Optional[str]
    timeZone: Optional[str] = 'Africa/Nairobi'

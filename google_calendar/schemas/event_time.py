import datetime
from typing import Optional

from pydantic import BaseModel


class EventTime(BaseModel):
    timeZone: Optional[str] = 'Nairobi/Kenya'
    date: Optional[str] = None
    dateTime: Optional[str] = None

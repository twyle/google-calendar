from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class EventTime(BaseModel):
    time_zone: str = ''
    date_: Optional[date] = None
    date_time: Optional[datetime] = None

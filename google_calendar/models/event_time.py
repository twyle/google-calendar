from datetime import date, datetime

from pydantic import BaseModel


class EventTime(BaseModel):
    date_: date
    date_time: datetime
    time_zone: str

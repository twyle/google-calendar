from typing import Any

from pydantic import BaseModel


class CalendarResource(BaseModel):
    calendar_client: Any

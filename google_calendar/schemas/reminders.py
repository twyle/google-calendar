from pydantic import BaseModel, Field

from .reminder import Reminder


class Reminders(BaseModel):
    useDefault: bool
    overrides: list[Reminder] = Field(default_factory=list)

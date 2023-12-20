from pydantic import BaseModel, Field

from .reminder import Reminder


class Reminders(BaseModel):
    use_default: bool
    overrides: list[Reminder] = Field(default_factory=list)

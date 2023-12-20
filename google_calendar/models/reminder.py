from pydantic import BaseModel


class Reminder(BaseModel):
    method: str
    minutes: int

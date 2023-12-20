from pydantic import BaseModel


class DefaultReminder(BaseModel):
    method: str
    minutes: int

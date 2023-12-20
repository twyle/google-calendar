from pydantic import BaseModel


class FocusTimeProperties(BaseModel):
    auto_decline_mode: str
    decline_message: str
    chat_status: str

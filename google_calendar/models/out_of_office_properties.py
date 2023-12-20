from pydantic import BaseModel


class OutOfficeProperties(BaseModel):
    auto_decline_mode: str
    decline_message: str

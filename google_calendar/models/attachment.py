from pydantic import BaseModel


class Attachment(BaseModel):
    file_url: str
    title: str
    mime_type: str
    icon_link: str
    file_id: str

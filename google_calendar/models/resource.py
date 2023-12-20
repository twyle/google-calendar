from pydantic import BaseModel, Field


class Resource(BaseModel):
    id: str
    etag: str
    resource_type: str = ''

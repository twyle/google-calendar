from typing import Any

from pydantic import BaseModel


class Resource(BaseModel):
    calendar_client: Any

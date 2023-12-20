from pydantic import BaseModel


class Key(BaseModel):
    type: str


class ConferenceSolution(BaseModel):
    key: Key
    name: str
    icon_uri: str

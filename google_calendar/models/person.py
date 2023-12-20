from pydantic import BaseModel


class Person(BaseModel):
    id: str
    email: str
    display_name: str
    self_: bool

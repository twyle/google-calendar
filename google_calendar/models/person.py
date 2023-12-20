from pydantic import BaseModel


class Person(BaseModel):
    email: str
    display_name: str = ''
    self_: bool = False

from pydantic import BaseModel


class EntryPoint(BaseModel):
    entrypoint_type: str
    uri: str
    label: str
    pin: str
    accesscode: str
    meetingcode: str
    passcode: str
    password: str

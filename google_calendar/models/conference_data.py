from pydantic import BaseModel, Field

from .conference_solution import ConferenceSolution
from .entry_point import EntryPoint


class ConferenceSolutionKey(BaseModel):
    type: str


class Status(BaseModel):
    status_code: str


class CreateRequest(BaseModel):
    request_id: str
    conference_solution_key: ConferenceSolutionKey
    status: Status


class ConferenceData(BaseModel):
    conference_id: str
    conference_solution: ConferenceSolution
    create_request: CreateRequest
    status: Status
    entry_points: list[EntryPoint] = Field(default_factory=list)
    notes: str
    signature: str

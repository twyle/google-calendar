from pydantic import BaseModel, Field


class ConferenceProperty(BaseModel):
    allowed_conference_solution_types: list[str] = Field(default_factory=list)

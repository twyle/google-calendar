from pydantic import BaseModel


class OfficeLocation(BaseModel):
    building_id: str
    floor_id: str
    floor_section_id: str
    desk_id: str
    label: str

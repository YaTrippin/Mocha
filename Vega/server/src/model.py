from pydantic import BaseModel
from typing import List

class Light(BaseModel):
    name: str
    light_type: str
    network_id: int
    groups: List[str]


class Lights(BaseModel):
    lights: List[Light] = []

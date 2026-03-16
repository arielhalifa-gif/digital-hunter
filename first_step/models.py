from pydantic import BaseModel, Field
from datetime import datetime



class Intel(BaseModel):
    timestamp: datetime
    signal_id: str
    entity_id:str
    reported_lat: float
    reported_lon: float
    signal_type: str
    priority_level: int = Field(ge=1, le=5 | 99)


class Attack(BaseModel):
    timestamp: datetime
    attack_id: str
    entity_id: str
    weapon_type: str



class Damage(BaseModel):
    timestamp: datetime
    attack_id: str
    entity_id: str
    result: str

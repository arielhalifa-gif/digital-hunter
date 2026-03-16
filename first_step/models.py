from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from kafka.kafka_producer import Producer




class Intel(BaseModel):
    timestamp: datetime
    signal_id: str
    entity_id:str
    reported_lat: float
    reported_lon: float
    signal_type: str
    priority_level: int = Field(ge=1, le=5 | 99, default=None)
    distance: float = None


    def validate_intel(target: dict):
        try:
            intel = Intel(timestamp=target['timestamp'],
                        signal_id=target['signal_id'],
                        entity_id=target['entity_id'],
                        reported_lat=target['reprted_lat'],
                        reported_lon=target['reported_lon'],
                        signal_type=target['signal_type'],
                        priority_level=target['priority_level'],
                        distance=target['distance'])
            return True
        except ValidationError as err:
            print(err)
            Producer.send_to_topic(intel, err)
            return False



class Attack(BaseModel):
    timestamp: datetime
    attack_id: str
    entity_id: str
    weapon_type: str

    def validate_attack(target):
        try:
            attack = Attack(timestamp=target['timestamp'],
                            attack_id=target['attack_id'],
                            entity_id=target['entity_id'],
                            weapon_type=target['weapons_type'])
            return True
        except ValidationError as err:
            return False


class Damage(BaseModel):
    timestamp: datetime
    attack_id: str
    entity_id: str
    result: str


    def validate_damage(target):
        try:
            damage = Damage(timestamp=target['timestamp'],
                            attack_id=target['attack_id'],
                            entity_id=target['entity_id'],
                            result=target['result'])
            return True
        except ValidationError as err:
            return False
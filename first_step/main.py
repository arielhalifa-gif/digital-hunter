from kafka.kafka_consumer import Consumer
from models import Intel, Attack, Damage
from database.mysql_config import Mysql
from students_part_1.haversine import haversine_km


def run_main_operations():
    for target in Consumer.listen_intel():
       #validate the target from kafka
       response = Intel.validate_intel(target)
       if response: # True if validate is ok
           # search if the target is already on the targets bank based on entity_id
           result = Mysql.search_target_in_sql(target['entity_id'])
           if result: # not None
               # calculate the distance between the bank data and the topic data
               # return the answer in km
               distance = haversine_km(result[3],
                                       result[4],
                                       target['reported_lat'],
                                       target['reported_lon'])
               Mysql.update_distance(distance, target['entity_id'])
    for target in Consumer.listen_attack():
        response = Attack.validate_attack(target)
        if response:
            Mysql.insert_into_attack(target)
    for target in Consumer.listen_damage():
        response = Damage.validate_damage(target)
        if response:
            Mysql.insert_into_damage(target)
               


if __name__ == "__main__":
    run_main_operations()
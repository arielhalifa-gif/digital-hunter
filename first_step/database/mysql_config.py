import mysql.connector



class Mysql:
    @staticmethod
    def get_mysql_connection():
        cnx = mysql.connector.connect(user = 'root', database = 'targets-bank')
        return cnx
    

    


    @staticmethod
    def insert_into_intel(data: dict):
        cnx = Mysql.get_mysql_connection()
        add_new_target = ("INSERT INTO intel (timestamp, signal_id, entity_id, reported_lat, reported_lon, signal_type, priority_level)"
                        "VALUES(%s, %s, %s, %s, %s, %s, %s)")
        values = tuple(data.values())
        cursor = cnx.cursor()
        cursor.execute(add_new_target, values)
        cursor.close()
        cnx.close()
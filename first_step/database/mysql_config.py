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


    @staticmethod
    def search_target_in_sql(entity_id_target):
        query  = '''SELECT * FROM intel
                    WHERE entity_id LIKE %s'''
        cnx = Mysql.get_mysql_connection()
        cursor = cnx.cursor()
        cursor.execute(query, entity_id_target)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result

import mysql.connector



class Mysql:

    def get_mysql_cursor():
        cnx = mysql.connector.connect(user = 'root', database = 'targets-bank')
        cursor = cnx.cursor()
        return cursor
    

    def insert_into_intel(data):
        cursor = Mysql.get_mysql_cursor()
        add_new_target = ("INSERT INTO intel (timestamp, signal_id, entity_id, reported_lat, reported_lon, signal_type, priority_level)"
                        "VALUES(%s, %s, %s, %s, %s, %s, %s)")
        values = 

import pymysql

mysql_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='smart_home'
)

def insert_into_mysql(table_name, data):
    with mysql_connection.cursor() as cursor:
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        cursor.execute(sql, list(data.values()))
        mysql_connection.commit()

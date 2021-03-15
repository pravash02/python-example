import sys
import json
import mysql.connector
from mysql.connector import errorcode


def mysql_conn(**kwargs):
    connection = None
    try:
        connection = mysql.connector.connect(user=kwargs['user'],
                                             password=kwargs['password'],
                                             host=kwargs['host'],
                                             port=kwargs['port'],
                                             database=kwargs['database'])
        connection.autocommit = True

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            sys.exit(1)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            sys.exit(1)
        else:
            print(err)
            sys.exit(1)

    return connection


if __name__ == '__main__':
    # db_cursor = mysql_conn('localhost', 'root', 'root@123', 'user_database', 3306)
    with open('../connection_details/mysql.json') as f:
        data = json.load(f)
    # conn = mysql_conn(**data)
    # db_cursor = conn.cursor(buffered=True)
    # query = "select * from users"
    # db_cursor.execute(query)
    # print(db_cursor.fetchone())



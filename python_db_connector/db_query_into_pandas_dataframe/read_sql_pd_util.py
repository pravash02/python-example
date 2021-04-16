import json
import pandas as pd
import teradata
import pandas_gbq as pd_gbq
from google.cloud import bigquery
from google_auth_oauthlib import flow
from google.oauth2 import service_account
from sqlalchemy import create_engine


# Service account file for GCP connection
credentials = service_account.Credentials.from_service_account_file('../connection_details/prav-proj-5d21e9018f12.json')
# client = bigquery.Client(credentials=credentials, project=credentials.project_id,)


# BigQuery Variables
PROJECT_ID = 'prav-proj'
DATASET_ID = 'data_load_common'


# MySQL Variables
with open('../connection_details/' + 'mysql.json') as f:
    data = json.load(f)
MYSQL_USERNAME = data['user']
MYSQL_PASSWORD = data['password']
MYSQL_HOST = data['host']


# MySQL Connection
def create_conn(database_name):
    sql_engine = ''
    conn_uri = 'mysql+pymysql://{}:{}@{}/{}'.format(
        MYSQL_USERNAME,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        database_name
    )
    try:
        sql_engine = create_engine(conn_uri, pool_recycle=3600).connect()
    except Exception as e:
        print('Error {}'.format(e))

    return conn_uri, sql_engine

# Teradata Connection
# udaExec = teradata.UdaExec(appName="DataTransfer", version="1.0",
#                            logConsole=False)
# session = udaExec.connect(method="odbc", system="",
#                           username="", password="")
# session.execute("SELECT * FROM table_nm")


def get_table_list(conn_uri):
    list_tables_query = 'SELECT table_name ' \
                  'FROM information_schema.tables ' \
                  'WHERE TABLE_TYPE = "BASE TABLE" ' \
                  'AND TABLE_SCHEMA = "user_database";'
    list_tables_df = pd.read_sql(list_tables_query, conn_uri)

    list_table = list_tables_df['TABLE_NAME'].to_list()

    return list_table


def load_to_gbq(list_table, conn_uri):
    for val in list_table:
        table_id = '{}.{}'.format(DATASET_ID, val).upper()

        data_query = 'SELECT * FROM {}'.format(val)
        df = pd.read_sql(data_query, conn_uri)
        if not df.empty:
            df.columns = map(str.upper, df.columns)
            print(df)
            pd_gbq.to_gbq(df, table_id,
                          project_id=PROJECT_ID,
                          if_exists='replace',
                          chunksize=10000000,
                          progress_bar=True)


if __name__ == '__main__':
    db_list = ['user_database']
    con_uri, engine = create_conn(db_list[0])
    list_tables = get_table_list(con_uri)
    load_to_gbq(list_tables, con_uri)

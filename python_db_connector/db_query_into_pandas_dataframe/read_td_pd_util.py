import json
import pandas as pd
import teradata
# import pyodbc as pyodbc
import pandas_gbq as pd_gbq
from google.cloud import bigquery
from google.oauth2 import service_account
from sqlalchemy import *


# Service account file for GCP connection
credentials = service_account.Credentials.from_service_account_file('../connection_details/prav-proj-5d21e9018f12.json')
# client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

# BigQuery Variables
PROJECT_ID = 'prav-proj'
DATASET_ID = 'data_load_common'

# TeraData Variables
with open('../connection_details/' + 'teradata.json') as f:
    data = json.load(f)
TD_USERNAME = data['user']
TD_PASSWORD = data['password']
TD_HOST = data['host']


# TeraData Connection
def create_conn(database_name):

    td_engine = create_engine('teradatasql://{}:{}@{}/{}'.format(TD_USERNAME, TD_PASSWORD, TD_HOST, database_name))
    print(td_engine)
    # udaExec = teradata.UdaExec(appName="td_playground", version="1.0",
    #                            logConsole=False)
    # session = udaExec.connect(method="odbc",
    #                           username="dbc", password="dbc",
    #                           database='console')
    # session.execute("SELECT * FROM table_nm")
    # employee_df = pd.read_sql(td_query, session)

    # link = 'DRIVER={DRIVERNAME};' \
    #        'DBCNAME={hostname};' \
    #        'UID={uid};' \
    #        'PWD={pwd}'.format(
    #     DRIVERNAME='Teradata Database ODBC Driver 17.00',
    #     hostname='172.16.114.2', uid='dbc', Database='console', pwd='dbc')
    # conn = pyodbc.connect(link)
    return td_engine


def get_table_list(conn, db_name):
    list_table = []
    list_tables_query = 'SELECT TableName ' \
                        'FROM DBC.TablesV ' \
                        'WHERE DatabaseName = \'{}\';'.format(db_name)

    list_tables_df = pd.read_sql(list_tables_query, conn)

    if not list_tables_df.empty:
        list_table = list_tables_df['TableName'].to_list()

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
    db_list = ['console']
    td_conn = create_conn(db_list[0])
    list_tables = get_table_list(td_conn, db_list[0])
    load_to_gbq(list_tables, td_conn)

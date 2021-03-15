import sys
import os
import json
import argparse
# from google.cloud import bigquery
from python_db_connector.dbconn import mysql_conn
from python_db_connector.get_datatype_mapping import get_datatype_mapping
from python_db_connector.get_table_names import get_table_names

parser = argparse.ArgumentParser(add_help=False,
                                 description='BQconvertor:- Convert any database schema to BigQuery Tables. Supported Databases: AWS RedShift.''')

parser.add_argument('-h', '--host', dest='db_host', action='store', required=False, help="Database server IP/Endpoint")
parser.add_argument('-u', '--user', dest='db_user', action='store', required=False, help="Database username")
parser.add_argument('-p', '--password', dest='db_password', action='store', required=False, help="Database Password")
parser.add_argument('-P', '--port', dest='db_port', action='store', required=False, help="Database Port")
parser.add_argument('-d', '--database', dest='db_name', action='store', required=False, help="Database name")
parser.add_argument('-s', '--source', dest='source', action='store', required=True, type=str.lower,
                    choices=['redshift', 'mysql'], help="Source platform (eg:redshift, sqlserver)")
parser.add_argument('-m', '--mapping', dest='mapping', action='store', required=False,
                    help="Path for your custom Datatype mapping file")
# parser.add_argument('-bq_p', '--bq_project', dest='bq_project', action='store', required=True,help="Bigquery project name")
# parser.add_argument('-bq_loc', '--bq_location', dest='bq_location', action='store', help="Bigquery dataset location")
# parser.add_argument('-bq_d', '--bq_dataset', dest='bq_dataset', action='store', required=True, help="Bigquery dataset name")


args = parser.parse_args()
# client = bigquery.Client()
print(str(args.db_host))
print(str(args.source))
print(str(args.mapping))
args.sh_whitelist = None
args.sh_blacklist = None
args.tbl_whitelist = None
args.tbl_blacklist = None

if str(args.source) == 'mysql':
    with open('connection_details/' + args.source + '.json') as f:
        data = json.load(f)

# Get the DB connection
conn = mysql_conn.mysql_conn(**data)

db_cursor = conn.cursor(buffered=True)  # Buffered cursor helps the connector to fetch ALL rows behind the scenes and we just take one from the connector so the mysql db won't complain

if __name__ == '__main__':
    data_mapping = get_datatype_mapping(args.mapping, args.source)
    finalized_schema_table_names = get_table_names(db_cursor, args.sh_whitelist,
                                                   args.sh_blacklist,
                                                   args.tbl_whitelist,
                                                   args.tbl_blacklist,
                                                   args.source)
    # ['profiles', 'users']
    table_names = finalized_schema_table_names[1]

    # 'user_database','user_database'
    schema_name_in = "'"+"','".join(finalized_schema_table_names[0])+"'"

    for t_name in table_names:
        q_get_columndetails = '''SELECT column_name, data_type, is_nullable 
                                 FROM INFORMATION_SCHEMA.COLUMNS WHERE 
                                 (table_schema not in ('information_schema', 'pg_catalog') and 
                                 table_schema not like('pg_temp_%')) and 
                                 table_name='{}' and 
                                 table_schema in ({});'''.format(t_name, schema_name_in)
        db_cursor.execute(q_get_columndetails)

        # [('profie_id', 'int', 'NO'), ('profile_name', 'varchar', 'NO')]
        # [('user_id', 'int', 'NO'), ('user_name', 'varchar', 'NO'), ('submission_date', 'date', 'YES')]
        column_details = db_cursor.fetchall()

        columns_string = ""
        schema = []
        i = 1
        for mapping in column_details:
            # Set BigQuery
            # table_id = '''{}.{}.{}'''.format(bq_project, bq_dataset, t_name)
            # q_info = '''-- Table Name: {}'''.format(t_name)
            # q_drop_tbl = '''DROP TABLE if exists `{}.{}.{}`;'''.format(bq_project, bq_dataset, t_name)

            source_name = mapping[0]
            source_type = mapping[1]
            target_type = data_mapping[source_type]

            apply = 'no'
            if apply.lower() == 'yes':
                if mapping[2] == 'NO':
                    is_nullable = 'REQUIRED'
                else:
                    is_nullable = 'NULLABLE'
                # schema.append(bigquery.SchemaField(source_name, target_type, is_nullable))
            else:
                if mapping[2] == 'NO':
                    is_nullable = 'NOT NULL'
                else:
                    is_nullable = ''
                column_string = '     {} {} {}'.format(source_name, target_type, is_nullable)
                if i < len(column_details):
                    column_string += ','
                    column_string += '\n'
                columns_string += column_string
                i += 1
            print(columns_string)
            # table = bigquery.Table(table_id, schema=schema)

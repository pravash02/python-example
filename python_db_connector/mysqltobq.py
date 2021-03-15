import json
# from google.cloud import bigquery
from python_db_connector.dbconn import mysql_conn
from python_db_connector.get_datatype_mapping import get_datatype_mapping
from python_db_connector.get_table_names import get_table_names


def convert_mysql_to_bq(source, mapping):
    print('Inside MySQL Conversion Function')
    with open('connection_details/' + source + '.json') as f:
        data = json.load(f)

    # Get the DB connection
    conn = mysql_conn.mysql_conn(**data)

    # Buffered cursor helps the connector to fetch ALL rows behind the scenes and
    # we just take one from the connector so the mysql db won't complain
    db_cursor = conn.cursor(buffered=True)

    data_mapping = get_datatype_mapping(mapping, source)
    finalized_schema_table_names = get_table_names(db_cursor)

    # ['profiles', 'users']
    table_names = finalized_schema_table_names[1]

    # 'user_database','user_database'
    schema_name_in = "'"+"','".join(finalized_schema_table_names[0])+"'"

    for t_name in table_names:
        q_get_column_details = '''SELECT column_name, data_type, is_nullable 
                                 FROM INFORMATION_SCHEMA.COLUMNS WHERE 
                                 (table_schema not in ('information_schema') and 
                                 table_schema not like('performance_schema%')) and 
                                 table_name='{}' and 
                                 table_schema in ({});'''.format(t_name, schema_name_in)
        db_cursor.execute(q_get_column_details)

        # [('profile_id', 'int', 'NO'), ('profile_name', 'varchar', 'NO')]
        # [('user_id', 'int', 'NO'), ('user_name', 'varchar', 'NO'), ('submission_date', 'date', 'YES')]
        column_details = db_cursor.fetchall()

        columns_string = ""
        schema = []
        i = 1   # to append till the last element in column details list

        apply = 'no'
        drop_flag = 'no'

        for mapping in column_details:
            # Set BigQuery
            # table_id = '''{}.{}.{}'''.format(bq_project, bq_dataset, t_name)
            # bq_info = '''-- Table Name: {}'''.format(t_name)
            # bq_drop_tbl = '''DROP TABLE if exists `{}.{}.{}`;'''.format(bq_project, bq_dataset, t_name)

            source_name = mapping[0]
            source_type = mapping[1]
            target_type = data_mapping[source_type]

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

            # table = bigquery.Table(table_id, schema=schema)

            if apply.lower() == 'yes':
                if drop_flag.lower() == 'yes':
                    pass
                    # client.query(bq_drop_tbl)
                # table = client.create_table(table)
            else:
                pass
                # bq_create_body = '''CREATE TABLE `{}.{}.{}` \n(\n{}\n); '''.format(bq_project, bq_dataset, t_name,
                #                                                                   columns_string)

                # if drop_flag.lower() == 'yes':
                #     sql_query = bq_info + '\n' + bq_drop_tbl + '\n' + bq_create_body
                # else:
                #     sql_query = bq_info + '\n' + bq_create_body

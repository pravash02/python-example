def get_table_names(dbcursor):

    query_get_table_name = \
        '''select table_schema, table_name from information_schema.tables WHERE
           (table_schema not in ('information_schema','pg_catalog')
           and table_schema NOT LIKE ('mysql')) and 
           table_schema NOT LIKE ('performance_schema') and
           table_schema NOT LIKE ('sys');'''

    cursor = dbcursor
    cursor.execute(query_get_table_name)
    query_table_name_result = cursor.fetchall()

    schema_names = [i[0] for i in query_table_name_result]
    table_names = [i[1] for i in query_table_name_result]

    # ['user_database', 'user_database'] ['profiles', 'users']
    return schema_names, table_names

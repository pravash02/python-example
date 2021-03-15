from python_db_connector.get_filter_tables import sql_table_filter


def get_table_names(dbcursor, sh_whitelist, sh_blacklist, tbl_whitelist,
                    tbl_blacklist, source):

    # tables_filtered = sql_table_filter(sh_whitelist, sh_blacklist,
    #                                    tbl_whitelist, tbl_blacklist, source)

    query_get_tablename = \
        '''select table_schema, table_name from information_schema.tables WHERE
           (table_schema not in ('information_schema','pg_catalog')
           and table_schema NOT LIKE ('mysql')) and 
           table_schema NOT LIKE ('performance_schema') and
           table_schema NOT LIKE ('sys');'''
    # {};'''.format(tables_filtered)

    cursor = dbcursor
    cursor.execute(query_get_tablename)
    query_tablename_result = cursor.fetchall()

    schema_names = [i[0] for i in query_tablename_result]
    table_names = [i[1] for i in query_tablename_result]

    # ['user_database', 'user_database'] ['profiles', 'users']
    return schema_names, table_names



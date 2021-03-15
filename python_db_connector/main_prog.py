import sys
import os
import json
import argparse
# from google.cloud import bigquery
from python_db_connector.mysqltobq import convert_mysql_to_bq

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--source', dest='source', action='store', required=True, type=str.lower,
                    choices=['mysql', 'teradata'], help="Source platform (eg:redshift, sqlserver)")
parser.add_argument('--mapping', dest='mapping', action='store', required=False,
                    help="Path for your custom Datatype mapping file")
# parser.add_argument('--bq_project', dest='bq_project', action='store', required=True,help="Bigquery project name")
# parser.add_argument('--bq_location', dest='bq_location', action='store', help="Bigquery dataset location")
# parser.add_argument('--bq_dataset', dest='bq_dataset', action='store', required=True, help="Bigquery dataset name")
parser.add_argument('--bq_drop_tbl', dest='drop_table', action='store', required=False, default='no', type = str.lower,
                    choices=['yes', 'no'], help="Drop tables on Bigquery before migrating the schema")
parser.add_argument('--bq_create_tbl', dest='create_table', action='store', required=False, default='no', type = str.lower,
                    choices=['yes', 'no'], help="Create the tables on BigQuery")

args = parser.parse_args()
# client = bigquery.Client()
print(str(args.source))

if __name__ == '__main__':
    if str(args.source) == 'mysql':
        convert_mysql_to_bq(args.source, args.mapping)

import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# DROP tables just in case before inserting them back again when running the create_tables query

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

# This function will create the required tables in this project 
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
# use conn and cur to connect to the redshift
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    print('You are now connected to Redshift cluster. Database and tables have been created, and configured. Now run `etl.py` to load staging tables and to create analytic tables.')
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
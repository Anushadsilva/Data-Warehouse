Objective
To build an ETL pipeline for a database hosted on Redshift.

Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.
The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, I load the data from S3 to staging tables on Redshift, and execute the SQL statement to create analytical tables based on star schema from staging tables.

Files
create_tables.py
It will create fact and dimension tables for the star schema in redshift

dwh.cfg
It stores information about config, and connections to the redshift. 
Configure dwh.cfg file
[AWS]
KEY=*
SECRET=*

[DWH]
DWH_CLUSTER_TYPE=multi-node
DWH_NUM_NODES=1
DWH_NODE_TYPE=dc2.large

DWH_IAM_ROLE_NAME=dwhRole
DWH_CLUSTER_IDENTIFIER=dwhcluster
DWH_DB=dwh
DWH_DB_USER=dwhuser
DWH_DB_PASSWORD=***
DWH_PORT=5439

[CLUSTER]
HOST=dwhcluster.**.amazonaws.com
DB_NAME=dwh
DB_USER=dwhuser
DB_PASSWORD=**
DB_PORT=5439

[IAM_ROLE]
ARN='aws:iam::**:role/dwhRole'

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'

etl.py
It loads the data from S3 to staging tables on Redshift, and executes the SQL statement for processing data

sql_queries.py
It defines the sql statements, and are imported to the other two py files

Tables
There are three types of tables here in this project.

For staging tables I created two staging tables (staging_events and staging_songs) to store data from two S3 buckets.
For fact tables As I used star schema for designing my database, the fact table I created is for song play event. It stores data about artist_id, level, location, session_id, song_id, start_time, user_agent, user_id.
For dimension tables I created four dimension tables - users, artists, songs, and time.
How to run the scripts to make the ETL happen?
Run the create_tables.py to create all the tables needed in this database
Run the etl.py to finish the ETL process including loading data to staging tables, and inserting data to dimension/fact tables
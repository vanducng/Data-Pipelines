# Data Pipelines 
## Introduction

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of CSV logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

## Project Description
This project will implement the data process pipeline as below diagram. Music application logs reside on AWS S3 in either JSON or CSV format. Data pipe is constructed as DAG components and orchestrated by Airflow. This block is reponsible for gather data from S3, perform stage raw data, transform dimensional & fact table before feeding into Redshift Data warehouse. 

<p align="center">
    <image src="./images/DataArchitechture.png" width="70%">
    <div align="center">Data pipeline</div>
</p>

The detail DAG diagram is presented in below figure.
<p align="center">
    <image src="./images/DAG Flow.png" width="80%">
    <div align="center">DAG Diagram</div>
</p>


## Environment setup and execution
- Install apache-airflow version 1.10.2, the latest 1.10.3 got a bug of not displaying task schedule.
    ```python
    pip install apache-airflow==1.10.2
    ```
- Setup environment and run aiflow web-server: 
    ```bash
    $ cd project_workspace # where your dags & plugins folder located
    $ EXPORT AIRFLOW_HOME=`pwd`
    $ airflow initdb
    $ airflow webserver
    ```
- DAG default settings:
    ```bash
    default_args = {
    'owner': 'vanducng',
    'start_date': datetime(2018, 5, 1),
    'end_date': datetime(2018, 11, 30),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False
    }
    ```

## Files in repository
    .
    ├── airflow.cfg
    ├── airflow.db
    ├── airflow-webserver.pid
    ├── dags
    │   └── dag.py
    ├── plugins
    │   ├── helpers
    │   │   ├── __init__.py
    │   │   └── sql_queries.py
    │   ├── __init__.py
    │   └── operators
    │       ├── create_tables.py
    │       ├── create_tables.sql
    │       ├── data_quality.py
    │       ├── __init__.py
    │       ├── load_dimension.py
    │       ├── load_fact.py
    │       └── stage_redshift.py
    └── README.md

* `dag.py`: the main program to control the DAG components
* `sql_queries.py`: contains SQL queries used for data transform, extract and load to Redshift
* `create_tables.py` & `create_tables.sql`: used for initial setup for creating new tables on Redshift
* `data_quality.py`: verify the data quality and raise the error once occured to ensure the data pipline is working in correct manner.
* `load_dimension.py`: load the dimensional tables including: songs, artists, time and user into Redshift.
* `load_fact.py`: load the fact table for song information based on staging event & song table.
* `stage_redshift.py`: inital load raw data from S3 into staging table.

## Dataset used in S3
* Log data: `s3://udacity-dend/log_data`
* Song data: `s3://udacity-dend/song_data`

# Data-Pipelines
## Introduction

A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app

## Project Description
This project will implement the data process pipeline as below diagram. Music application logs reside on AWS S3 in either JSON or CSV format. Data pipe is constructed as DAG components and orchestrated by Airflow. This block is reponsible for gather data from S3, perform stage raw data, transform dimensional & fact table before feeding into Redshift Data warehouse. 

<p align="center">
    <image src="./images/DataArchitechture.png" width="80%">
    <div align="center">Data pipeline overview</div>
</p>

The detail DAG diagram is presented in below figure.
<p align="center">
    <image src="./images/DAG Flow.png" width="80%">
    <div align="center">Data pipeline overview</div>
</p>


## Environment setup
- Install apache-airflow version 1.10.2, the latest 1.10.3 got a bug of not displaying task schedule.
    ```python
    pip install apache-airflow==1.10.2
    ```
- Setup environment and run aiflow web-server: 
    ```bash
        $ cd project_workspace
        $ EXPORT AIRFLOW_HOME=`pwd`
        $ airflow initdb
        $ airflow webserver
    ```
- File in repository
    ```bash      .
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

    ```


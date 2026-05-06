An end-to-end data engineering project that automates the collection, cleaning, and storage of 100+ job 
listings to analyze modern hiring trends.

Project Overview:
This project implements a complete ETL pipeline to track the evolving job market. 
By programmatically extracting data and transforming it into a structured relational format, 
the system enables high-efficiency querying of salary benchmarks and technical skill requirements.

Technical Features:
Automated Extraction: Scrapes and ingests data from 1,000+ active job listings.
Standardized Transformation: Utilizes Pandas for data cleaning, string processing, and handling missing values to ensure high data integrity.
Relational Storage: Implements a structured MySQL database schema for efficient storage and complex relational querying.
Database ORM: Leverages SQLAlchemy to manage database connections and programmatically execute SQL operations within Python.

ETL Workflow:
Extract: Programmatically gathers raw job listing data.
Transform: Cleanses text data, normalizes salary formats, and categorizes job roles using Pandas.
Load: Ingests the refined dataset into a MySQL database via an optimized SQLAlchemy pipeline.

Motivation: 
The primary objective of this project was to move beyond manual market research and build a scalable system for data-driven career analysis. Developing this pipeline allowed me to:
Master Data Engineering Basics: Implement a robust integration workflow between Python and SQL.
Enable Trend Discovery: Turn thousands of unstructured listings into actionable insights regarding salary distributions and high-demand skills.

How to Run:
Prerequisites
Python 3.x
MySQL Server
Required libraries: pandas, sqlalchemy, mysql-connector-python

Installation & Setup:
Clone the repository:
git clone https://github.com
cd Job-Market-ETL

Install dependencies:
pip install pandas sqlalchemy mysql-connector-python
Configure Database: Update your MySQL credentials in the config.py or script header.
Setup database: run database/schema.sql in your MySQL environment to create the tables
Configure credentials: ensure load.py or config.py file has your MySQL access details
Run the Pipeline:
python etl_pipeline.py

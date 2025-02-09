# Daily Commute Analytics & Recommendation

**Daily Commute Analytics & Recommendation** is an ETL pipeline project that gathers daily traffic and weather data to help users optimize their commute routes. This project demonstrates practical data engineering skills by integrating multiple free APIs, processing and transforming data with Python, and orchestrating the workflow using Apache Airflow. The final processed data can be loaded into a data warehouse (e.g., AWS Redshift or PostgreSQL) for further analysis and visualization.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies & Tools](#technologies--tools)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

The goal of this project is to build an automated ETL pipeline that:
- **Extracts** traffic data using the Google Maps Distance Matrix API and weather data using the OpenWeatherMap API.
- **Transforms** the data by cleaning, normalizing, and merging it to create a unified dataset.
- **Loads** the processed data into a cloud storage solution (AWS S3) and further into a data warehouse (AWS Redshift or PostgreSQL).
- **Orchestrates** the entire process with Apache Airflow, running the pipeline automatically every day before the user's commute.

By analyzing this data, users can receive insights and recommendations to adjust their departure times or routes based on traffic conditions and weather forecasts.

## Features

- **Real-time Traffic Data**: Retrieve current traffic conditions using the Google Maps Distance Matrix API.
- **Real-time Weather Data**: Get up-to-date weather information from the OpenWeatherMap API.
- **Data Transformation**: Combine and clean traffic and weather data using Pandas.
- **Cloud Integration**: Upload processed data to AWS S3 and load it into AWS Redshift (or PostgreSQL).
- **Workflow Orchestration**: Schedule and manage the ETL pipeline with Apache Airflow.
- **Extensibility**: Easily extend the pipeline for additional data sources or further analysis (e.g., creating dashboards or sending notifications).

## Architecture

The overall architecture consists of the following steps:

1. **Extract**: 
   - Traffic data is obtained via the Google Maps Distance Matrix API.
   - Weather data is obtained via the OpenWeatherMap API.
2. **Transform**:
   - Use Python (Pandas) to clean and merge the traffic and weather datasets.
3. **Load**:
   - Save the transformed data as a CSV file.
   - Upload the CSV file to AWS S3 using Boto3.
   - Load the data from S3 into a data warehouse (AWS Redshift or PostgreSQL) using a COPY command.
4. **Orchestration**:
   - Automate and schedule the entire process with Apache Airflow.

## Technologies & Tools

- **Programming Language**: Python 3.7+
- **Data Processing**: Pandas, NumPy
- **HTTP Requests**: Requests
- **Cloud Integration**: Boto3 (for AWS S3)
- **Database Connectivity**: psycopg2-binary (for PostgreSQL/Redshift)
- **Workflow Orchestration**: Apache Airflow
- **Version Control**: Git & GitHub
- **Optional Tools**: Docker (for containerizing the Airflow setup), VS Code (IDE)
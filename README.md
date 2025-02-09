# Daily Commute Analytics & Recommendation

## Overview

**Daily Commute Analytics & Recommendation** is an ETL pipeline project that gathers daily traffic and weather data to help users optimize their commute routes. This project integrates multiple APIs, processes and transforms data using Python, and orchestrates the workflow with Apache Airflow. The final processed data is stored in SQLite for further analysis and visualization.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Technologies & Tools](#technologies--tools)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- **Real-time Traffic Data**: Retrieve current traffic conditions using the HERE Maps API.
- **Real-time Weather Data**: Get up-to-date weather information from the OpenWeatherMap API.
- **Data Transformation**: Clean and merge traffic and weather data using Pandas.
- **Local Storage**: Save processed data in SQLite instead of cloud storage.
- **Workflow Orchestration**: Schedule and manage the ETL pipeline with Apache Airflow.
- **Extensibility**: Easily add more data sources or enhance data analysis features.

## Architecture

The ETL pipeline follows these steps:

1. **Extract**:
   - Traffic data is obtained via the HERE Maps API.
   - Weather data is obtained via the OpenWeatherMap API.
2. **Transform**:
   - Use Python (Pandas) to clean and merge the traffic and weather datasets.
3. **Load**:
   - Store the processed data in an SQLite database.
4. **Orchestration**:
   - Automate and schedule the entire ETL process using Apache Airflow.

## Technologies & Tools

- **Programming Language**: Python 3.9+
- **Data Processing**: Pandas, NumPy
- **HTTP Requests**: Requests
- **Database**: SQLite
- **Workflow Orchestration**: Apache Airflow
- **Version Control**: Git & GitHub

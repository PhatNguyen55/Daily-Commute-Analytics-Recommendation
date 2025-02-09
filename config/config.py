import os

HERE_API_KEY = os.getenv('HERE_API_KEY')
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
SQLITE_DB_PATH = os.getenv('SQLITE_DB_PATH', 'commute_data.db')

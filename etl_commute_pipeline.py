from traffic_extractor import fetch_traffic_data
from weather_extractor import fetch_weather_data
from transformer import transform_data
from sqlite_loader import load_data_to_sqlite
import pandas as pd
from config.config import SQLITE_DB_PATH

def run_commute_etl():
    # Bước 1: Extract Data
    # Lấy dữ liệu giao thông từ HERE Maps API:
    # Ví dụ: tọa độ trung tâm TP. Hồ Chí Minh, bán kính 5000m.
    lat = 10.762622
    lon = 106.660172
    radius = 5000
    traffic_data = fetch_traffic_data(lat, lon, radius)
    
    # Lấy dữ liệu thời tiết từ OpenWeatherMap API:
    weather_city = "Ho Chi Minh"
    weather_data = fetch_weather_data(weather_city)
    
    # Bước 2: Transform Data
    df_transformed = transform_data(traffic_data, weather_data)
    
    # Xuất dữ liệu đã xử lý ra file CSV
    output_file = "commute_data.csv"
    df_transformed.to_csv(output_file, index=False)
    
    # Bước 3: Load Data vào SQLite
    load_data_to_sqlite(output_file, SQLITE_DB_PATH)

if __name__ == "__main__":
    run_commute_etl()

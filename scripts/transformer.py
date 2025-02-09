import pandas as pd
from datetime import datetime

def transform_data(traffic_data, weather_data):
    # Chuyển dữ liệu dictionary thành DataFrame
    df_traffic = pd.DataFrame([traffic_data])
    df_weather = pd.DataFrame([weather_data])
    
    # Thêm cột ngày tháng
    current_date = datetime.today().strftime("%Y-%m-%d")
    df_traffic["date"] = current_date
    df_weather["date"] = current_date
    
    # Ghép dữ liệu dựa trên cột "date"
    df_combined = pd.merge(df_traffic, df_weather, on="date", how="left")
    return df_combined

if __name__ == "__main__":
    # Sử dụng dữ liệu mẫu để thử nghiệm
    traffic_info = {
        "lat": 10.762622,
        "lon": 106.660172,
        "radius": 5000,
        "speed": 30,        # km/h
        "jam_factor": 3,    # ví dụ: 3 trên 10
    }
    weather_info = {
        "city": "Ho Chi Minh",
        "timestamp": "2025-02-02 07:00:00",
        "temperature": 28,
        "weather": "clear sky"
    }
    df_final = transform_data(traffic_info, weather_info)
    print(df_final)

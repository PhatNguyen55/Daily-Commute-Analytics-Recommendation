import requests
from config.config import HERE_API_KEY

def fetch_traffic_data(lat, lon, radius):
    """
    Lấy dữ liệu giao thông từ HERE Traffic Flow API dựa trên tọa độ và bán kính.
    """
    url = "https://traffic.ls.hereapi.com/traffic/6.3/flow.json"
    params = {
        "prox": f"{lat},{lon},{radius}",
        "apiKey": HERE_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Xử lý dữ liệu trả về: lấy thông tin từ các "RWS" trong JSON.
    try:
        traffic_info = data["RWS"][0]["RW"][0]["FIS"][0]["FI"][0]
        # Ví dụ: Lấy thông tin về tốc độ lưu thông và mức độ tắc nghẽn (Jam Factor)
        speed = traffic_info["CF"][0]["SP"]  # Tốc độ (km/h)
        jam_factor = traffic_info["CF"][0]["JF"]  # Mức độ tắc nghẽn
        return {
            "lat": lat,
            "lon": lon,
            "radius": radius,
            "speed": speed,
            "jam_factor": jam_factor,
            "raw": traffic_info  # Lưu lại toàn bộ dữ liệu nếu cần tham khảo
        }
    except (KeyError, IndexError) as e:
        raise Exception("Error processing HERE Maps API response: " + str(e))

if __name__ == "__main__":
    # Ví dụ: Tọa độ trung tâm TP. Hồ Chí Minh, bán kính 5000m
    lat = 10.762622
    lon = 106.660172
    radius = 5000
    traffic_data = fetch_traffic_data(lat, lon, radius)
    print(traffic_data)

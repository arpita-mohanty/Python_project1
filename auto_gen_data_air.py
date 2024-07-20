import pandas as pd
from datetime import datetime, timedelta
import random

# Function to generate random data for the dataset
def generate_data(num_records, start_date, end_date, station_ids):
    date_range = pd.date_range(start=start_date, end=end_date, freq='h')
    data = []

    for timestamp in date_range:
        for station_id in station_ids:
            record = {
                "timestamp": timestamp,
                "station_id": station_id,
                "PM2.5": round(random.uniform(10, 50), 1),
                "PM10": round(random.uniform(20, 60), 1),
                "NH3": round(random.uniform(5, 30), 1),
                "NO": round(random.uniform(5, 25), 1),
                "NO2": round(random.uniform(10, 50), 1),
                "SO2": round(random.uniform(5, 20), 1),
                "CO": round(random.uniform(0.1, 2), 2),
                "O3": round(random.uniform(5, 30), 1),
                "temperature": round(random.uniform(15, 35), 1),
                "humidity": random.randint(40, 90),
                "wind_speed": round(random.uniform(0, 10), 1),
                "wind_direction": random.randint(0, 360),
                "traffic_volume": random.randint(100, 2000)
            }
            data.append(record)
    
    return pd.DataFrame(data)

# Generate the dataset
start_date = "2024-07-01"
end_date = "2024-07-02"
station_ids = [1, 2]

df = generate_data(24, start_date, end_date, station_ids)

# Save to CSV
file_path = "C:/Users/pc/Desktop/air_dataset/air.csv"
df.to_csv(file_path, index=False)


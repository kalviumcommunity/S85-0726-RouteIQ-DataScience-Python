import csv
import random
import numpy as np
import os

def generate_data(num_rows=2500, seed=42):
    np.random.seed(seed)
    random.seed(seed)
    
    # Domains
    vehicle_types = ['bike', 'car', 'scooter']
    areas = ['central', 'suburb', 'industrial', 'old_city', 'tech_park']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weathers = ['clear', 'rain', 'fog']
    
    data = []
    
    for i in range(1, num_rows + 1):
        trip_id = i
        driver_id = np.random.randint(100, 150)
        vehicle_type = np.random.choice(vehicle_types, p=[0.4, 0.2, 0.4])
        pickup_area = np.random.choice(areas)
        dropoff_area = np.random.choice(areas)
        
        # Distance between 1 and 25 km
        distance_km = round(np.random.uniform(1.0, 25.0), 2)
        
        time_of_day = np.random.randint(0, 24)
        day_of_week = np.random.choice(days)
        
        # Traffic index logic
        base_traffic = np.random.uniform(0.1, 0.4)
        if time_of_day in [8, 9, 10, 17, 18, 19]:
            traffic_index = base_traffic + np.random.uniform(0.4, 0.6)
        else:
            traffic_index = base_traffic + np.random.uniform(0.0, 0.3)
            
        traffic_index = min(round(traffic_index, 2), 1.0)
        
        weather = np.random.choice(weathers, p=[0.7, 0.2, 0.1])
        
        # Base speed based on vehicle type (km per minute)
        speeds = {'bike': 0.3, 'car': 0.5, 'scooter': 0.4}
        speed = speeds[vehicle_type]
        
        planned_duration_min = round(distance_km / speed, 2)
        
        # Actual duration calculation
        # old_city has higher base times
        area_penalty = 1.2 if pickup_area == 'old_city' or dropoff_area == 'old_city' else 1.0
        weather_penalty = 1.3 if weather == 'rain' else (1.15 if weather == 'fog' else 1.0)
        
        # Traffic effect (1.0 to 2.0 multiplier)
        traffic_penalty = 1.0 + traffic_index
        
        noise = np.random.normal(0, 5) # random noise
        
        actual_duration_min = round((planned_duration_min * area_penalty * weather_penalty * traffic_penalty) + noise, 2)
        actual_duration_min = max(actual_duration_min, 1.0) # Ensure it's at least 1 min
        
        # Delivery status
        if actual_duration_min > planned_duration_min + 15:
            delivery_status = 'delayed'
        elif actual_duration_min < planned_duration_min - 5:
            delivery_status = 'early'
        else:
            delivery_status = 'on_time'
            
        driver_experience_days = np.random.randint(30, 1000)
        
        row = {
            'trip_id': trip_id,
            'driver_id': driver_id,
            'vehicle_type': vehicle_type,
            'pickup_area': pickup_area,
            'dropoff_area': dropoff_area,
            'distance_km': distance_km,
            'time_of_day': time_of_day,
            'day_of_week': day_of_week,
            'traffic_index': traffic_index,
            'weather': weather,
            'planned_duration_min': planned_duration_min,
            'actual_duration_min': actual_duration_min,
            'delivery_status': delivery_status,
            'driver_experience_days': driver_experience_days
        }
        data.append(row)
        
    # Introduce outliers in actual_duration_min (approx 1%)
    outlier_indices = np.random.choice(range(num_rows), size=int(num_rows * 0.01), replace=False)
    for idx in outlier_indices:
        data[idx]['actual_duration_min'] = round(data[idx]['actual_duration_min'] + np.random.uniform(100, 200), 2)
        
    # Introduce missing values (3-5% for weather, actual_duration_min, distance_km)
    missing_indices = np.random.choice(range(num_rows), size=int(num_rows * 0.04), replace=False)
    for idx in missing_indices:
        col_to_blank = np.random.choice(['weather', 'actual_duration_min', 'distance_km'])
        data[idx][col_to_blank] = ''
        
    # Introduce duplicate rows (2%)
    duplicate_count = int(num_rows * 0.02)
    duplicates = [dict(data[i]) for i in np.random.choice(range(num_rows), size=duplicate_count, replace=False)]
    for i in range(len(duplicates)):
        # slightly modify traffic index just to make it a subtle duplicate if requested, but instructions say "same trip_id but slightly different values"
        duplicates[i]['traffic_index'] = min(1.0, duplicates[i]['traffic_index'] + 0.01)
    
    data.extend(duplicates)
    
    # Shuffle after adding duplicates
    np.random.shuffle(data)
    
    return data

def main():
    print("Generating dataset...")
    data = generate_data()
    
    fieldnames = [
        'trip_id', 'driver_id', 'vehicle_type', 'pickup_area', 'dropoff_area', 
        'distance_km', 'time_of_day', 'day_of_week', 'traffic_index', 'weather', 
        'planned_duration_min', 'actual_duration_min', 'delivery_status', 
        'driver_experience_days'
    ]
    
    # Preview
    print("Preview of first 3 rows:")
    for i in range(3):
        print(data[i])
        
    # Save to CSV
    # Ensure relative path works no matter where script is run from
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '..', 'data', 'raw')
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, 'delivery_trips.csv')
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Dataset with {len(data)} rows successfully saved to {output_file}")

if __name__ == '__main__':
    main()

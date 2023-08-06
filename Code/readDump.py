import pandas as pd
import numpy as np
import os 

def haversine(lat1, lon1, lat2, lon2):
    # Calculate the Haversine distance between two sets of latitude and longitude
    R = 6371  # Earth's radius in km
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat/2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = R * c
    return distance

def calculate_metrics(speed_data_file):
    print("Inside calucaluate metrics")
    print("for the path: ", speed_data_file)
    try:
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(speed_data_file)

        # Calculate the distance for each row
        # (You need to have the haversine function defined as shown in a previous response)
        data['distance'] = haversine(data['lat'], data['lon'], data['lat'].shift(-1), data['lon'].shift(-1))

        # Calculate the average speed
        avg_speed = data['spd'].mean()

        # Calculate the number of speed violations based on 'osf' column
        speed_violations = data['osf'].sum()

        return data['lic_plate_no'].iloc[0], data['distance'].sum(), avg_speed, speed_violations

    except FileNotFoundError:
        # If the file is not found, return metrics as '-'
        return '-', '-', '-', '-'
    

if __name__ == "__main__":
    # Your original DataFrame containing unique vehicle information (output from the previous code)
    vehicle_info = pd.DataFrame({
        'vehicle_number': ["GJ03AT4282", "GJ03BT6388", "GJ06AV0041", "GJ06TT6762", "GJ06Z8611"],
        'transporter_name': ["Amarnath Petroleum", "JAY RADHA MADHAV ROADLINES", "SHREE SAHJANAND PETROLEUM", "Gauri Filling Station Pvt Ltd", "Suresh Petroleum Co."],
        'trip_count': [4, 1, 1, 2, 1]
    })

    # Folder path containing CSV files with speed data for each vehicle
    speed_data_folder = r'C:\Numadic Test\Data\Data test\EOL-dump'  # Replace with the actual folder path

    # Create an empty list to store the calculated metrics for each vehicle
    vehicle_metrics = []

    # Loop through the files in the speed data folder
    for filename in os.listdir(speed_data_folder):
        if filename.endswith(".csv"):
            speed_data_file = os.path.join(speed_data_folder, filename)
            lic_plate_no, distance, avg_speed, speed_violations = calculate_metrics(speed_data_file)
            vehicle_metrics.append([lic_plate_no, distance, avg_speed, speed_violations])

    # Create a DataFrame from the calculated metrics
    metrics_df = pd.DataFrame(vehicle_metrics, columns=['lic_plate_no', 'distance', 'avg_speed', 'speed_violations'])
    print("metrics DF is", metrics_df)
    # vehicle_info['lic_plate_no'] = vehicle_info['lic_plate_no'].astype(str)
    # metrics_df['lic_plate_no'] = metrics_df['lic_plate_no'].astype(str)
    print("vehicleinfo DF is ",vehicle_info)

    # Merge the two DataFrames based on the 'lic_plate_no' column
    combined_data = pd.merge(vehicle_info, metrics_df, on='lic_plate_no')

    # Save the combined DataFrame to a new CSV file
    combined_data.to_csv("output_file.csv", index=False)

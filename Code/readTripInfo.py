import pandas as pd

def get_vehicle_info(csv_file, start_time, end_time):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file)

    # Convert the 'date_time' column to a pandas datetime format
    data['date_time'] = pd.to_datetime(data['date_time'], format='%Y%m%d%H%M%S')

    # Filter rows based on the given timestamp range
    filtered_data = data[(data['date_time'] >= start_time) & (data['date_time'] <= end_time)]

    # Get unique vehicle numbers, their transporter names, and count of distinct trip_ids
    unique_vehicles = filtered_data[['vehicle_number', 'transporter_name', 'trip_id']].drop_duplicates()
    vehicle_count = unique_vehicles.groupby(['vehicle_number', 'transporter_name'])['trip_id'].count().reset_index()
    
    # Rename the 'trip_id' column to 'trip_count'
    vehicle_count.rename(columns={'trip_id': 'trip_count'}, inplace=True)
    # print("vehicle count: ", vehicle_count)
    return vehicle_count

if __name__ == "__main__":
    csv_file = r'C:\Numadic Test\Data\Data test\Trip-Info.csv'
    start_time = pd.to_datetime("2018-03-28 00:00:00", format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime("2018-03-28 01:59:59", format="%Y-%m-%d %H:%M:%S")

    result = get_vehicle_info(csv_file, start_time, end_time)
    print(result)

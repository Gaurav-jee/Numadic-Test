import pandas as pd
import numpy as np

def getData(path):
    data = pd.read_csv(path)
    return data.head(10)

def retrieve_rows_in_range(csv_file_path, start_time, end_time):
    #csv_file = "your_csv_file.csv"
    start_time = pd.to_datetime(start_time, format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime(end_time, format="%Y-%m-%d %H:%M:%S")

    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file_path)
    # Convert the 'date_time' column to a pandas datetime format
    data['date_time'] = pd.to_datetime(data['date_time'], format='%Y%m%d%H%M%S')
    # Filter rows based on the given timestamp range
    filtered_data = data[(data['date_time'] >= start_time) & (data['date_time'] <= end_time)]

    return filtered_data


if __name__ == "__main__":
    # csv_file_path = r'C:\Numadic Test\Data\Data test\Trip-Info.csv'
    # start_time = pd.to_datetime("2018-03-28 00:00:00", format="%Y-%m-%d %H:%M:%S")
    # end_time = pd.to_datetime("2018-03-28 23:59:59", format="%Y-%m-%d %H:%M:%S")

    # data = retrieve_rows_in_range(csv_file_path, start_time, end_time)
    # print(type(data))
    # print(data.count())
    pass
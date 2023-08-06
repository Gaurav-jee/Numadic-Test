from flask import Flask, request, jsonify
from functions import getData, retrieve_rows_in_range
from readTripInfo import get_vehicle_info
from readDump2 import getcombinedDataFromDump
import pandas as pd
import numpy as np

app = Flask(__name__)

# Sample data representing vehicle trails and trip info (replace with actual data from CSV files)
vehicle_trails_data = []
# Your vehicle trail data goes here (e.g., [{'fk_asset_id': 1, 'lic_plate_no': 'ABC123', ...}, ...])


trip_info_data = getData(r'C:\Numadic Test\Data\Data test\Trip-Info.csv')
    # Your trip info data goes here (e.g., [{'trip_id': 1, 'vehicle_number': 'ABC123', ...}, ...])


# API endpoint to generate the asset report
@app.route('/generate_asset_report', methods=['GET'])
def generate_asset_report():
    start_time = int(request.args.get('start_time'))
    end_time = int(request.args.get('end_time'))

    # Implement your data filtering, computations, and report generation here
    # ...

    # Sample response for demonstration purposes (replace with actual data and computations)
    path = r'C:\Numadic Test\Data\Data test\Trip-Info.csv'
    start_time = pd.to_datetime("2018-03-28 00:00:00", format="%Y-%m-%d %H:%M:%S")
    end_time = pd.to_datetime("2018-03-28 23:59:59", format="%Y-%m-%d %H:%M:%S")

    retrieved_data = get_vehicle_info(path, start_time, end_time)

    final_result = getcombinedDataFromDump(retrieved_data)
    
    print("THE FINAL RESULT IS: ", final_result)
    # response = {
    #     'License plate number': 'ABC123',
    #     'Distance': 100.5,
    #     'Number of Trips Completed': 5,
    #     'Average Speed': 60.2,
    #     'Transporter Name': 'XYZ Transport',
    #     'Number of Speed Violations': 3
    # }
    json_data = final_result.to_json(orient='records')

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)

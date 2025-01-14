import pandas as pd
import os

# Define the path to the folder containing your CSV files
# Update this path if the folder is located elsewhere on your system
data_folder = r'C:\Users\mwash\Downloads\Class Project\temperature_data'

# Function to read all the CSV files in the folder and concatenate them into one DataFrame
def read_all_csv_files(data_folder):
    # List all files in the folder and filter only the ones with a .csv extension
    files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
    
    df_list = []  # Initialize an empty list to hold dataframes for each CSV file
    
    # Loop through each CSV file
    for file in files:
        file_path = os.path.join(data_folder, file)  # Construct the full file path
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        df_list.append(df)  # Add the DataFrame to the list
    
    # Concatenate all DataFrames in the list into one single DataFrame
    all_data = pd.concat(df_list, ignore_index=True)
    return all_data

# Load all temperature data into a single DataFrame
temperature_data = read_all_csv_files(data_folder)

# List of month names in order, corresponding to the columns in each CSV file
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# 1. Calculate the average temperature for each month across all years
monthly_avg_temperatures = temperature_data[months].mean()  # Calculate mean for each month

# Save the result to "average_temp.txt"
with open('average_temp.txt', 'w') as f:
    # Write a header for the monthly temperature data
    f.write('---------------------------\n')
    f.write('Average Temperature by Month\n')
    f.write('---------------------------\n')
    
    # Write the average temperature for each month to the file
    for month, avg_temp in zip(months, monthly_avg_temperatures):
        f.write(f'{month}: {avg_temp:.2f} Degree Celsius\n')  # Format the temperature to 2 decimal places
    
    f.write('\n')  # Add an extra line for separation

# 2. Calculate the average temperature for each season across all years
# Defining seasons with their corresponding months
seasons = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

season_avg_temperatures = {}  # Dictionary to store average temperature for each season

# Loop through each season and calculate the average temperature for that season
for season, months_in_season in seasons.items():
    # Calculate the mean temperature for each season across all years
    season_avg_temperatures[season] = temperature_data[months_in_season].mean().mean()

# Append the seasonal averages to "average_temp.txt"
with open('average_temp.txt', 'a') as f:
    f.write('---------------------------\n')
    f.write('Average Temperature by Season\n')
    f.write('---------------------------\n')
    
    # Write the average temperature for each season to the file
    for season, avg_temp in season_avg_temperatures.items():
        f.write(f'{season}: {avg_temp:.2f} Degree Celsius\n')  # Format the temperature to 2 decimal places

# 3. Find the station/stations with the largest temperature range
# Calculate the temperature range for each station (Max temperature - Min temperature)
temperature_data['Temperature_Range'] = temperature_data[months].max(axis=1) - temperature_data[months].min(axis=1)

# Find the station/stations with the largest temperature range by finding the max range
max_temp_range = temperature_data['Temperature_Range'].max()

# Identify all stations that have the maximum temperature range
stations_with_largest_range = temperature_data[temperature_data['Temperature_Range'] == max_temp_range]['STATION_NAME']

# Save the result to "largest_temp_range_station.txt"
with open('largest_temp_range_station.txt', 'w') as f:
    f.write('---------------------------\n')
    f.write('Stations with Largest Temperature Range\n')
    f.write('---------------------------\n')
    
    # Write the station names with the largest temperature range to the file
    for station in stations_with_largest_range:
        f.write(f'{station}\n')

# 4. Find the warmest and coolest station/stations based on the average temperature
# Calculate the average temperature for each station across all months
temperature_data['Avg_Temperature'] = temperature_data[months].mean(axis=1)

# Find the warmest station (station with the highest average temperature)
warmest_station = temperature_data.loc[temperature_data['Avg_Temperature'].idxmax()]['STATION_NAME']

# Find the coolest station (station with the lowest average temperature)
coolest_station = temperature_data.loc[temperature_data['Avg_Temperature'].idxmin()]['STATION_NAME']

# Save the result to "warmest_and_coolest_station.txt"
with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write('---------------------------\n')
    f.write('Warmest and Coolest Stations\n')
    f.write('---------------------------\n')
    
    # Write the warmest and coolest station names to the file
    f.write(f'Warmest Station: {warmest_station}\n')
    f.write(f'Coolest Station: {coolest_station}\n')

# Print a message indicating that the analysis has completed and results have been saved
print("Analysis completed. Results saved to text files.")

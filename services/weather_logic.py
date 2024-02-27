# services/weather_logic.py

import requests
from datetime import datetime, timedelta
from datetime import timezone


# Function to fetch the latest sensor reading
def get_latest_sensor_reading(sensor_id):
    url = f"http://3.145.131.67:8000/api/sensor-readings/?sensor={sensor_id}"
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        readings = response.json()
        return readings[-1] if readings else None
    else:
        return None

# Function to fetch grid point data
def get_grid_point(latitude, longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['properties']
    else:
        return None

# Function to fetch forecast data
def get_forecast(office, gridX, gridY):
    url = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['properties']['periods']
    else:
        return None

# Function to parse wind speed from string to m/s
def parse_wind_speed(wind_speed_str):
    speeds = [float(s) for s in wind_speed_str.split() if s.isdigit()]
    avg_speed_mph = sum(speeds) / len(speeds)
    return avg_speed_mph * 0.44704  # Convert mph to m/s

# Function to check if it's safe to fly
def is_safe_to_fly(wind_speed_m_s, precipitation_mm):
    MAX_SAFE_WIND_SPEED = 5  # m/s
    MAX_SAFE_PRECIPITATION = 2.5  # mm/h
    if wind_speed_m_s > MAX_SAFE_WIND_SPEED:
        return False, "Wind speed too high for safe flight."
    if precipitation_mm > MAX_SAFE_PRECIPITATION:
        return False, "Precipitation too high for safe flight."
    return True, "Conditions safe for flight."

# Main function to check conditions
def check_conditions(start_time, flight_duration):
    # Constants for latitude and longitude
    latitude = 38.67437279416018
    longitude = -90.39682390342499

    # Convert start time to UTC and calculate end time
    start_time_utc = start_time.astimezone(timezone.utc)
    end_time_utc = start_time_utc + timedelta(minutes=flight_duration)

    # Check real-time sensor data (only relevant if start time is near current time)
    real_time_check = "Data unavailable"
    if datetime.utcnow().replace(tzinfo=timezone.utc) >= start_time_utc:
        wind_sensor_id = 5
        precipitation_sensor_id = 2

        latest_wind_reading = get_latest_sensor_reading(wind_sensor_id)
        latest_precipitation_reading = get_latest_sensor_reading(precipitation_sensor_id)

        if latest_wind_reading and latest_precipitation_reading:
            wind_speed = latest_wind_reading['value']
            precipitation = latest_precipitation_reading['value']
            _, real_time_check = is_safe_to_fly(wind_speed, precipitation)

    # Check forecast data
    forecast_check = "Forecast data unavailable"
    grid_point = get_grid_point(latitude, longitude)
    if grid_point:
        forecast = get_forecast(grid_point['gridId'], grid_point['gridX'], grid_point['gridY'])
        if forecast:
            for period in forecast:
                period_start = datetime.fromisoformat(period['startTime'].replace('Z', '+00:00'))
                period_end = datetime.fromisoformat(period['endTime'].replace('Z', '+00:00'))
                # Check if the period overlaps with the flight time
                if period_start < end_time_utc and period_end > start_time_utc:
                    wind_speed_str = period.get('windSpeed', '')
                    wind_speed = parse_wind_speed(wind_speed_str)
                    precipitation = 2.5 if "rain" in period['shortForecast'].lower() else 0.0
                    _, temp_message = is_safe_to_fly(wind_speed, precipitation)
                    if temp_message != "Conditions safe for flight":
                        forecast_check = temp_message
                        break
                    forecast_check = temp_message

    return real_time_check, forecast_check
 

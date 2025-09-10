import pandas as pd
import numpy as np


def find_num_stops_within_radius(property_lat, property_lon, stops_df, radius_km):
    """
    Calculate the number of transport stops within a given radius (in km) of a property.

    Parameters:
    property_lat (float): Latitude of the property
    property_lon (float): Longitude of the property
    stops_df (DataFrame): DataFrame containing transport stops with 'Latitude' and 'Longitude' columns
    radius_km (float): Radius in kilometers

    Returns:
    int: Number of stops within the specified radius
    """
    # Haversine formula
    lat_diff = np.radians(stops_df['Latitude'] - property_lat)
    lon_diff = np.radians(stops_df['Longitude'] - property_lon)

    a = np.sin(lat_diff / 2)**2 + np.cos(np.radians(property_lat)) * \
        np.cos(np.radians(stops_df['Latitude'])) * np.sin(lon_diff / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distances_km = 6371 * c  # Earth radius in km

    # Mask for rows within radius
    mask = distances_km <= radius_km
    stops_within_radius = stops_df[mask]

    # Print matching rows
    # print(stops_within_radius)

    return np.sum(mask)


def return_stop_insights_per_type(property_lat, property_lon, stops_df, radius):
    output = dict()
    output["NumMetroBusStops"] = find_num_stops_within_radius(
        property_lat, property_lon, stops_df[stops_df["StopType"] == "Metro Bus"], radius)
    output["NumMetroTramStops"] = find_num_stops_within_radius(
        property_lat, property_lon, stops_df[stops_df["StopType"] == "Metro Tram"], radius)
    output["NumMetroTrainStops"] = find_num_stops_within_radius(
        property_lat, property_lon, stops_df[stops_df["StopType"] == "Metro Train"], radius)
    output["NumRegionalTrainStops"] = find_num_stops_within_radius(
        property_lat, property_lon, stops_df[stops_df["StopType"] == "Regional Train"], radius)
    output["NumRegionalBusStops"] = find_num_stops_within_radius(
        property_lat, property_lon, stops_df[stops_df["StopType"] == "Regional Bus"], radius)
    return output


def return_stop_insights_metro_bus(property_lat, property_lon, stops_df, radius):
    return find_num_stops_within_radius(property_lat, property_lon, stops_df[stops_df["StopType"] == "Metro Bus"], radius)


def return_stop_insights_metro_tram(property_lat, property_lon, stops_df, radius):
    return find_num_stops_within_radius(property_lat, property_lon, stops_df[stops_df["StopType"] == "Metro Tram"], radius)


def return_stop_insights_metro_train(property_lat, property_lon, stops_df, radius):
    return find_num_stops_within_radius(property_lat, property_lon, stops_df[stops_df["StopType"] == "Metro Train"], radius)


def return_stop_insights_regional_train(property_lat, property_lon, stops_df, radius):
    return find_num_stops_within_radius(property_lat, property_lon, stops_df[stops_df["StopType"] == "Regional Train"], radius)


def return_stop_insights_regional_bus(property_lat, property_lon, stops_df, radius):
    return find_num_stops_within_radius(property_lat, property_lon, stops_df[stops_df["StopType"] == "Regional Bus"], radius)


# Test, my address longitude and latitude:
test_lat = -37.662281
test_long = 145.032432
radius_km = 2

data = pd.read_csv("data/processed/transport/transport_stops.csv")
metro_bus = data[data["StopType"] == "Metro Bus"]
metro_tram = data[data["StopType"] == "Metro Tram"]
metro_train = data[data["StopType"] == "Metro Train"]
regional_train = data[data["StopType"] == "Regional Train"]
regional_bus = data[data["StopType"] == "Regional Bus"]

print(return_stop_insights_per_type(test_lat, test_long, data, radius_km))

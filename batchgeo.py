# This script automates the process of batch geocoding a large number of addresses using the ArcGIS Geocoding API.

## Import necessary libraries

import csv  # for reading and writing CSV files
import requests  # for making HTTP requests

## Set up the API endpoint and your API key

endpoint = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
key = "YOUR_API_KEY"  # replace with your own API key

## Read in the input addresses from a CSV file

# Open the input CSV file in read mode
with open("input_addresses.csv", "r") as f:
    # Create a CSV reader object
    reader = csv.reader(f)
    # Extract the addresses from the first column of the CSV file and store them in a list
    addresses = [row[0] for row in reader]

## Set up the request parameters

params = {
    "f": "json",  # the response format is JSON
    "outFields": "Match_addr",  # include the matching address in the response
    "maxLocations": "1",  # return only one result per address
    "forStorage": "false",  # do not store the results for later use
    "singleLine": "",  # the address to geocode (will be set in the loop below)
}

## Initialize a list to store the results

results = []

## Geocode the addresses one by one

# Iterate over the list of addresses
for address in addresses:
    # Set the singleLine parameter to the current address
    params["singleLine"] = address
    # Make a request to the API endpoint
    response = requests.get(endpoint, params=params, timeout=10)
    # If the request was successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        # If there are any candidates (possible matches)
        if data["candidates"]:
            # Get the first candidate
            candidate = data["candidates"][0]
            # Extract the matching address and coordinates from the candidate
            match_addr = candidate["address"]
            x = candidate["location"]["x"]
            y = candidate["location"]["y"]
            # Add the result (address, matching address, x, y) to the results list
            results.append([address, match_addr, x, y])

## Write the results to a CSV file

# Open the output CSV file in write mode
with open("output_locations.csv", "w", newline="") as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    # Write the results to the CSV file
    writer.writerows(results)

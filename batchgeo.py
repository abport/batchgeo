import csv
import requests

# Set the API endpoint and your API key
endpoint = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
key = "YOUR_API_KEY"

# Read in the input addresses from a CSV file
with open("input_addresses.csv", "r") as f:
    reader = csv.reader(f)
    addresses = [row[0] for row in reader]

# Set up the request parameters
params = {
    "f": "json",
    "outFields": "Match_addr",
    "maxLocations": "1",
    "forStorage": "false",
    "singleLine": "",
}

# Initialize a list to store the results
results = []

# Iterate over the addresses and geocode them one by one
for address in addresses:
    params["singleLine"] = address
    response = requests.get(endpoint, params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if data["candidates"]:
            # Get the first candidate and extract the match address and coordinates
            candidate = data["candidates"][0]
            match_addr = candidate["address"]
            x = candidate["location"]["x"]
            y = candidate["location"]["y"]
            # Add the result to the list
            results.append([address, match_addr, x, y])

# Write the results to a CSV file
with open("output_locations.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

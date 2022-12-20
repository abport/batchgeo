
# Python script for batch geocoding addresses using the ArcGIS Geocoding API

This script automates the process of batch geocoding a large number of addresses using the ArcGIS Geocoding API. It reads in a list of addresses from a CSV file, geocodes each address using the API, and writes the resulting locations (matching addresses and coordinates) to a new CSV file.

## Prerequisites

-   You will need to have Python installed on your computer. You can download the latest version of Python from the official website at [https://www.python.org/](https://www.python.org/).
-   You will need to obtain an API key from ArcGIS. You can sign up for a free ArcGIS Developer account at [https://developers.arcgis.com/](https://developers.arcgis.com/) and request a free API key.

## Setup

1.  Clone or download this repository to your computer.
2.  Navigate to the directory where you saved the script.
3.  Replace `YOUR_API_KEY` with your actual API key on line 6 of the script.
4. Create a CSV file called `input_addresses.csv` containing a single column of addresses, with each address in a separate row. For example:

    1600 Pennsylvania Ave NW, Washington, DC 20500
    221B Baker St, London, England
    Leaning Tower of Pisa, Piazza del Duomo, 56126 Pisa PI, Italy
    Mount Everest, Nepal
    Eiffel Tower, Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France

## Usage

To run the script, open a terminal or command prompt and navigate to the directory where you saved the script. Then run the following command:

    python batch_geocode.py

The script will read in the addresses from the `input_addresses.csv` file, geocode each address using the ArcGIS Geocoding API, and write the resulting locations (matching addresses and coordinates) to a new CSV file called `output_locations.csv`.

## Customization

You can customize the script to suit your specific needs and preferences. Here are a few examples of how you can modify the script:

-   Change the endpoint URL to use a different geocoding service or API.
-   Add or modify request parameters to customize the results. For example, you can specify a different output spatial reference or set the `magicKey` parameter to improve the accuracy of the results.
-   Modify the output fields to include additional information in the results. For example, you can include the `score` field to indicate the confidence level of the match.
-   Use the script as a starting point and build upon it to create more complex automation tasks, such as batch geocoding addresses and then adding the resulting locations to a map or GIS dataset.

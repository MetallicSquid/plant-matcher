# Script to find information about an plant in the wikipedia table
import requests
from googlesearch import search
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


def find_sci_information(category_string):
    url = f"https://en.wikipedia.org/wiki/{category_string}"
    # Use wikipedia respectfully, give it 2 seconds to rest
    sleep(2)

    # Account for connection errors and 404s
    try:
        request = requests.get(url)
        if request.status_code == 404:
            return "Page not found"
    except requests.exceptions.ConnectionError:
        return "Connection failed - check your wifi"

    # Return scientific information about the given plant
    try:
        scientific = pd.read_html(url, header=1, index_col=0)[0]
        scientific_dict = {}
        for row in scientific.iterrows():
            if "kingdom" in row[0].lower():
                scientific_dict["Kingdom"] = row[1][0]
            elif "family" in row[0].lower():
                scientific_dict["Family"] = row[1][0]
            elif "genus" in row[0].lower():
                scientific_dict["Genus"] = row[1][0]

        #print(scientific_dict)
        return scientific_dict
    except:
        return f"No entry for {category_string}"

# Script to find information about an plant in the wikipedia table
import requests
'''
This script needs to find information about a given plant.

This means that I need to send a request to Wikipedia, trying the `plant string`.
As I see it there are a few ways a given request could go:
    1.  Request is not recieved
    2.  Request is recieved - page doesn't exist
    3.  Request is recieved - incorrect page is found
    4.  Request is recieved - correct page is found
The first two scenarios are easy to detect:
    1.  Connection error occurs
    2.  404 response
The second two scenarios are a bit harder, I have to find a consistent pattern
between them.
'''

def find_information(category_string):
    url = f"https://en.wikipedia.org/wiki/{category_string}"
    # Test for case 1 - Request is not recieved
    try:
        request = requests.get(url)

        # Test for case 2 - Page doesn't exist
        if request.status_code == 404:
            return "Page not found"

        # Test for case 3 - incorrect page is found

        # Test for case 4 - correct page is found

    except requests.exceptions.ConnectionError:
        return "Connection failed - check your wifi"

print(find_information("https://en.wikipedia.org/wiki/iuabwnopk"))

#!/usr/bin/python3
"""Function that queries Redddit API and return number of subscribers. If an invalid subreddit is given , the function should return 0"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json"
    headers = {
        "User-Agent": "Ademola/1.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

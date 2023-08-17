#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid API limitations
    headers = {'User-Agent': 'CustomUserAgent'}

    # Make a request to the Reddit API
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Get the number of subscribers from the response data
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    elif response.status_code == 404:
        # Subreddit not found
        return 0
    else:
        # Other errors
        return 0

# Example usage
subreddit_name = 'programming'
subscribers = number_of_subscribers(subreddit_name)
if subscribers:
    print(f'The subreddit {subreddit_name} has {subscribers} subscribers.')
else:
    print(f'The subreddit {subreddit_name} is not valid or not found.')


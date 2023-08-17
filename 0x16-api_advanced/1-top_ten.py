#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Set a custom User-Agent to avoid API limitations
    headers = {'User-Agent': 'CustomUserAgent'}

    # Make a request to the Reddit API
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10', headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Get the list of posts from the response data
        posts = data['data']['children']
        
        if not posts:
            print(f"No hot posts found in subreddit '{subreddit}'.")
            return
        
        print(f"Top 10 hot posts in subreddit '{subreddit}':")
        for index, post in enumerate(posts, start=1):
            post_title = post['data']['title']
            print(f"{index}. {post_title}")
    elif response.status_code == 404:
        # Subreddit not found
        print("Invalid subreddit.")
    else:
        # Other errors
        print("An error occurred while fetching data.")

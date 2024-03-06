#!/usr/bin/python3
"""queries the Reddit API and returns the top 10 posts"""
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
    subreddit (str): The subreddit to query.

    Returns:
    None
    """
    headers = {"User-Agent": "https://github.com/Pronothurah"}
    params = {"limit": 10}
    url = f"{BASE_URL}/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for post in data.get("children")[:10]:
            print(post.get("data").get("title"))
    else:
        print("None")

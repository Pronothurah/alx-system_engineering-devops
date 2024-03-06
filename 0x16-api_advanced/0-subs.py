#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers
        for a given subreddit

        Args:
        subreddit (str): The subreddit to query.

        Returns:
            int: The number of subscribers for the subreddit.
                Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "https://github.com/Pronothurah"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0

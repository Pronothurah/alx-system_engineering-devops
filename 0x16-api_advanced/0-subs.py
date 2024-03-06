#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers
        for a given subreddit

        Args:
        subreddit (str): The subreddit to query.

        Returns:
            int: The number of subscribers for the subreddit.
                Returns 0 if the subreddit is invalid.
    """
    def number_of_subscribers(subreddit):
        """Returns total subscribers of a sub reddit"""
        headers = {"User-Agent": "https://github.com/Pronothurah"}
        response = requests.get(url=BASE_URL,
                                headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data").get("subscribers")
        return 0

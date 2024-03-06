#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers of a sub reddit"""
    def number_of_subscribers(subreddit):
        """Returns total subscribers of a sub reddit"""
        BASE_URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {"User-Agent": "https://github.com/Pronothurah"}
        response = requests.get(url=BASE_URL,
                                headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data").get("subscribers")
        return 0

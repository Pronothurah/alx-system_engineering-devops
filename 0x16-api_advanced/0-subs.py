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
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    res = requests.get(
        f'{BASE_URL}/r/{subreddit}/about/.json',
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0

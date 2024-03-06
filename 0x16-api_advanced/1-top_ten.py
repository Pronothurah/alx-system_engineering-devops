#!/usr/bin/python3
"""queries the Reddit API and returns the top 10 posts"""
import requests

BASE_URL = 'https://www.reddit.com'

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
    subreddit (str): The subreddit to query.

    Returns:
    None
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
        f'{BASE_URL}/r/{subreddit}/hot/.json',
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)

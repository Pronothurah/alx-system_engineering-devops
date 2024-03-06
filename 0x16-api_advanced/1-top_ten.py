#!/usr/bin/python3
"""queries the Reddit API and returns the top 10 posts"""
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def top_ten(subreddit):
    """Return the top ten of a sub reddit"""
    headers = {"User-Agent": "MyRedditBot/1.0 (onsongo)"}
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

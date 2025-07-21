#!/usr/bin/python3
"""This module queries the Reddit API to fetch the top 10 hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditClient/1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post['data']['title'])

    except Exception:
        print(None)

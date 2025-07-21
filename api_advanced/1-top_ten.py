#!/usr/bin/python3
"""A script to print the titles of the first 10 hot posts from a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the top 10 hot post titles for a given subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = requests.get(reddit_url, headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post['data']['title'])
    except Exception:
        print(None)

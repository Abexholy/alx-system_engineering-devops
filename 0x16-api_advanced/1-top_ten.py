#!/usr/bin/python3
"""
Module 1-top_ten that contains the top_ten functions
"""
import requests


def top_ten(subreddit):
    """function queries Reddit API and prints the total
    titles of the first 10 hot posts listed for the given
    subreddit
    """
    url = 'http://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    params = {'limit': 10}
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json().get('data')
        [print(child["data"]["title"]) for child in data["children"]]
        return
    print('None')

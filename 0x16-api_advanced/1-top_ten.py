#!/usr/bin/python3
"""1-top_ten queries the reddit api and returns the top ten
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'dennisrequest'}
    req = requests.get(url, headers=headers)
    if req.status_code == 404 or req.status_code == 302:
        print(None)
    else:
        req = req.json()
        if req.get('data', None) is not None:
            for item in req.get('data').get('children'):
                print(item.get('data').get('title'))
        else:
            return None

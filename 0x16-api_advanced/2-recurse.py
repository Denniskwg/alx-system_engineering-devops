#!/usr/bin/python3
"""2-recurse defines a function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """
    if after is None:
        return
    url = "https://www.reddit.com/r/{}/hot.\
json?after={}".format(subreddit, after)
    headers = {'user-agent': 'dennisrequest'}
    req = requests.get(url, headers=headers)
    if req.status_code == 404 or req.status_code == 302:
        return None
    req = req.json()
    for post in req.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    recurse(subreddit, hot_list, req.get('data').get('after'))
    return hot_list

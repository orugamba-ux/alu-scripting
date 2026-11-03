#!/usr/bin/python3
"""Gets the number of subscribers of a subreddit from the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Returns how many subscribers a subreddit has, or 0 if it is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/alu_student)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)

#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom_user_agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for status code 200 (valid subreddit) and ensure it's JSON data
        if response.status_code == 200 and response.headers['Content-Type']
        .startswith('application/json'):
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)

        # Return 0 for invalid subreddit or any other error
        return 0

    except requests.RequestException:
        return 0

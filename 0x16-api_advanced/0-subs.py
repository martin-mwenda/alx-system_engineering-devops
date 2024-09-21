#!/usr/bin/python3
"""Function to query the number of subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a specific subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        int: The number of subscribers. Returns 0 if subreddit is not found.
    """
    # Construct URL to fetch subreddit details
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set up custom user-agent to avoid request rejection
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is not found, return 0
    if response.status_code == 404:
        return 0

    # Extract the 'data' field from the response JSON
    results = response.json().get("data")

    # Return the number of subscribers from the 'data' field
    return results.get("subscribers")


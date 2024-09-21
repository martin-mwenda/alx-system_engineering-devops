#!/usr/bin/python3
"""This script takes an employee ID and returns information
about their TODO list progress using a REST API."""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
            )
    name = user.json().get('name')

    # Fetch todos data
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    completed_tasks = 0

    # Process each task
    for task in todos.json():
        if task.get('userId') == int(user_id):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1

    # Print user task completion
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_tasks, total_tasks))

    # Print titles of completed tasks
    print(
            '\n'.join(
                ["\t " + task.get('title') for task in todos.json()
                    if task.get('userId') == int(user_id) and 
                    task.get('completed')]
                )
            )

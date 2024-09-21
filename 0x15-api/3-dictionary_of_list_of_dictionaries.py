#!/usr/bin/python3
"""A Python script that fetches data from a REST API for employee todo lists."""

import json
import requests
import sys

if __name__ == '__main__':
    # Base URL for users
    base_url = "https://jsonplaceholder.typicode.com/users"

    # Get the list of all users
    response = requests.get(base_url)
    users = response.json()

    # Dictionary to store all users' tasks
    users_tasks = {}

    # Loop through each user to fetch their todos
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        
        # Construct URL to fetch tasks for each user
        todos_url = '{}/todos/'.format(base_url + '/' + str(user_id))
        response = requests.get(todos_url)

        # Get the list of tasks
        tasks = response.json()
        
        # Store tasks for the user in a dictionary
        users_tasks[user_id] = []
        for task in tasks:
            task_completed = task.get('completed')
            task_title = task.get('title')
            
            # Append task details to the user's task list
            users_tasks[user_id].append({
                "task": task_title,
                "completed": task_completed,
                "username": username
            })

    # Write the collected data to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_tasks, f)


#!/usr/bin/python3

"""
Python script that exports employee task data in JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    # Fetch all todo items from the API
    todos_response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()

    tasks_list = []
    
    # Fetch all user data from the API
    users_response = get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    # Get the username and id of the employee matching the provided employee ID
    for user in users_data:
        if user['id'] == int(argv[1]):
            username = user['username']
            employee_id = user['id']

    tasks_list = []

    # Iterate through the todos and gather data for the specified employee
    for task in todos_data:

        task_dict = {}

        if task['userId'] == int(argv[1]):
            task_dict['username'] = username
            task_dict['task'] = task['title']
            task_dict['completed'] = task['completed']
            tasks_list.append(task_dict)

    # Create the final dictionary with employee ID as key and task list as value
    final_data = {}
    final_data[employee_id] = tasks_list
    
    # Convert dictionary to JSON format
    json_output = json.dumps(final_data)

    with open(argv[1] + ".json", "w") as file:
        file.write(json_output)


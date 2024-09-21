#!/usr/bin/python3
"""Script to interact with a REST API and retrieve TODO lists for a given employee"""

import requests
import sys

if __name__ == '__main__':
    # Fetch the employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Define the base URL for the API endpoint
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + "/" + employee_id

    # Get the employee's details from the API
    response = requests.get(user_url)
    username = response.json().get('username')  # Extract username from the JSON response

    # Get the employee's todo list from the API
    todos_url = user_url + "/todos"
    response = requests.get(todos_url)
    todos = response.json()  # List of todo tasks

    # Write the data to a CSV file named after the employee's ID
    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get('title')))  # Write each task's details in CSV format


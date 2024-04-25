#!/usr/bin/python3
"""The api is used to call the employee id and returns certain values"""

import requests
import sys


def getapi():
    """makes the call for each employee id"""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee data
    try:
        employee_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        employee_data = employee_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee data: {e}")
        sys.exit(1)

    if "name" not in employee_data:
        print(f"No employee found with ID {employee_id}")
        sys.exit(1)

    employee_name = employee_data["name"]

    # Fetch TODO list for the employee
    try:
        todo_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
        todo_data = todo_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO list: {e}")
        sys.exit(1)

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Display progress
    print(
        f"Employee {employee_name} is done with tasks\
        ({completed_tasks}/{total_tasks}):"
    )
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    getapi()

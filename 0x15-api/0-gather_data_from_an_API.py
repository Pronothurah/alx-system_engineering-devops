#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Returns to do progress of employee"""
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    employee_response = requests.get(employee_url)
    employee_name = employee_response.json()["name"]

    # get todos
    todos_response = requests.get(todo_url)
    todos = todos_response.json()

    # calculate progress
    total_tasks = len(todos)
    completed_tasks = len([todo for todo in todos if todo["completed"]])
    progress = f"{completed_tasks}/{total_tasks}"

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({progress}):")
    for todo in todos:
        if todo["completed"]:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

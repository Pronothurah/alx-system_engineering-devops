#!/usr/bin/python3
"""gathers employee data from api."""

import csv
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = int(sys.argv[1])
        req = requests.get(f'{REST_API}/users/{user_id}').json()
        task_req = requests.get(f'{REST_API}/todos').json()
        username = req.get('username')
        tasks = [task for task in task_req if task.get('userId') == user_id]
        with open(f'{user_id}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in tasks:
                writer.writerow([user_id, username, task.get('completed'), task.get('title')])
        print(f'Data exported to {user_id}.csv successfully.')

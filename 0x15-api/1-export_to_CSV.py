#!/usr/bin/python3
"""gathers employee data from api."""

import csv
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        url_user = f'{REST_API}/users/{user_id}'
        res = requests.get(url_user)
        user_name = res.json().get('username')

        task_url = f'{url_user}/todos'
        tasks_res = requests.get(task_url)
        tasks = tasks_res.json()

        with open(f'{user_id}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for task in tasks:
                completed = task.get('completed')
                title_task = task.get('title')
                writer.writerow([user_id, user_name, completed, title_task])

        print(f'Data exported to {user_id}.csv successfully.')

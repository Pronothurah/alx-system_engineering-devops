#!/usr/bin/python3
'''A script that gathers data from an API and exports it to a JSON file.
'''
import json
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


def fetch_user_data(user_id):
    '''Fetch user data from the API.'''
    user_res = requests.get(f'{API_URL}/users/{user_id}')
    if user_res.status_code != 200:
        print(f'Failed to fetch user data for user ID {user_id}.')
        return None
    return user_res.json()


def fetch_todos(user_id):
    '''Fetch todos for a given user ID from the API.'''
    todos_res = requests.get(f'{API_URL}/todos?userId={user_id}')
    if todos_res.status_code != 200:
        print(f'Failed to fetch todos for user ID {user_id}.')
        return None
    return todos_res.json()


def export_to_json(user_id, user_data, todos):
    '''Export user data and todos to a JSON file.'''
    user_name = user_data.get('username')
    user_tasks = [{'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': user_name} for todo in todos]
    data = {str(user_id): user_tasks}
    with open(f'{user_id}.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not re.fullmatch(r'\d+', sys.argv[1]):
        print('Usage: python script.py <user_id>')
        sys.exit(1)

    user_id = int(sys.argv[1])
    user_data = fetch_user_data(user_id)
    if user_data is None:
        sys.exit(1)

    todos = fetch_todos(user_id)
    if todos is None:
        sys.exit(1)

    export_to_json(user_id, user_data, todos)

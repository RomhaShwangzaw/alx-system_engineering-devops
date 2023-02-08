#!/usr/bin/python3
""" Script that returns information about an employee's TODO list """

import requests
import sys


if __name__ == "__main__":
    total = 0
    completed = 0
    titles_completed = []
    users = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]

    x = requests.get(users)
    y = requests.get(todos)

    name = x.json().get('name')

    for a in y.json():
        total += 1
        if a.get('completed') is True:
            completed += 1
            titles_completed.append(a.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, total))

    for title in titles_completed:
        print('\t {}'.format(title))

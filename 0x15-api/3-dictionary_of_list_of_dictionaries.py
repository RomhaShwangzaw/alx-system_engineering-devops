#!/usr/bin/python3
""" Script that exports data of all employees in the JSON format """

import json
import requests


if __name__ == "__main__":
    users = 'https://jsonplaceholder.typicode.com/users/'
    final_dict = {}

    x = requests.get(users)
    for u in x.json():
        user_id = str(u.get('id'))
        todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
        tasks = []

        y = requests.get(todos)

        username = u.get('username')

        for a in y.json():
            d = {}
            d["username"] = username
            d["task"] = a.get('title')
            d["completed"] = a.get('completed')
            tasks.append(d)

        final_dict["{}".format(user_id)] = tasks

    # Serializing json
    json_object = json.dumps(final_dict)

    # Writing to todo_all_employees.json
    with open("todo_all_employees.json", "w") as outfile:
        outfile.write(json_object)

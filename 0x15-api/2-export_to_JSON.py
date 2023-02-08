#!/usr/bin/python3
""" Script that exports data in the JSON format """

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    users = 'https://jsonplaceholder.typicode.com/users/' + user_id
    todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    tasks = []

    x = requests.get(users)
    y = requests.get(todos)

    username = x.json().get('username')

    for a in y.json():
        d = {}
        d["task"] = a.get('title')
        d["completed"] = a.get('completed')
        d["username"] = username
        tasks.append(d)

    final_dict = {}
    final_dict["{}".format(user_id)] = tasks

    # Serializing json
    json_object = json.dumps(final_dict)

    # Writing to USER_ID.json
    with open("{}.json".format(user_id), "w") as outfile:
        outfile.write(json_object)

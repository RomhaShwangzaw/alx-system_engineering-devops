#!/usr/bin/python3
""" Script that exports data in the CSV format """

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    users = 'https://jsonplaceholder.typicode.com/users/' + user_id
    todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id

    x = requests.get(users)
    y = requests.get(todos)

    username = x.json().get('username')

    # open the file in the write mode
    f = open('{}.csv'.format(user_id), 'w', encoding='UTF8')

    # create the csv writer
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    for a in y.json():
        row = []
        row.append(user_id)
        row.append(username)
        row.append(a.get('completed'))
        row.append(a.get('title'))

        # write a row to the csv file
        writer.writerow(row)

    # close the file
    f.close()

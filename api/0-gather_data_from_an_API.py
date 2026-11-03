#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""

import sys
import urllib.request
import json


def get_data(url):
    """Fetch and decode JSON data from a URL."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    employee = get_data(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    tasks = get_data(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )

    employee_name = employee.get("name")
    completed = [task for task in tasks if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed), len(tasks)
        )
    )

    for task in completed:
        print("\t {}".format(task.get("title")))

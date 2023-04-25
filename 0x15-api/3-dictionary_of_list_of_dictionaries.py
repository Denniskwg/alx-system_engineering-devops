#!/usr/bin/python3
"""0-gather_data_from_an_API gathers data from an api
using requests library
"""


if __name__ == "__main__":
    import json
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url).json()
    users = requests.get(url2).json()
    json_dict = {}

    with open("todo_all_employees.json", 'w') as f:
        for user in users:
            username = user.get("username")
            id = str(user.get("id"))
            user_list = []
            for todo in r:
                if user.get("id") == todo.get("userId"):
                    user_dict = {}
                    user_dict['username'] = username
                    user_dict['task'] = todo.get('title')
                    user_dict['completed'] = todo.get('completed')
                    user_list.append(user_dict)
            json_dict[id] = user_list
        json.dump(json_dict, f)

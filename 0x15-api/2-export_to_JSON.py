#!/usr/bin/python3
"""0-gather_data_from_an_API gathers data from an api
using requests library
"""


if __name__ == "__main__":
    import json
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    r = requests.get(url).json()
    user = requests.get(url2).json()
    user_list = []
    json_dict = {}

    with open("{}.json".format(sys.argv[1]), 'w') as f:
        for todo in r:
            if todo.get("userId") == int(sys.argv[1]):
                user_dict = {}
                user_dict['task'] = todo.get('title')
                user_dict['completed'] = todo.get('completed')
                user_dict['username'] = user.get('username')
                user_list.append(user_dict)
        json_dict[sys.argv[1]] = user_list
        json.dump(json_dict, f)

#!/usr/bin/python3
"""0-gather_data_from_an_API gathers data from an api
using requests library
"""


if __name__ == "__main__":
    import requests
    import sys
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    r = requests.get(url).json()
    user = requests.get(url2).json()

    with open("{}.csv".format(sys.argv[1]), 'w') as f:
        for todo in r:
            if todo.get("userId") == int(sys.argv[1]):
                id = todo.get('userId')
                name = user.get('username')
                comp = todo.get('completed')
                title = todo.get('title')
                f.write('"{}","{}","{}","{}"\n'.format(id, name, comp, title))

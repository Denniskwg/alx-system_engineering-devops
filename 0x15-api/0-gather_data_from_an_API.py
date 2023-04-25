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
    r2 = requests.get(url2).json()
    name = r2.get('name')
    num = 0
    completed = 0
    tasks = []
    for i in range(len(r)):
        id = r[i].get("userId")
        if id == int(sys.argv[1]):
            num = num + 1
            if r[i].get('completed'):
                completed = completed + 1
            tasks.append(r[i])

    s = "Employee {} is done with tasks({}/{})".format(name, completed, num)
    print(s)
    for task in tasks:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))

import requests

base_url = 'http://127.0.0.1:5000'

def get_user(id):
    url = f'{base_url}/users/'

    params = {
        'id': id
    }

    response = requests.get(url, params=params)
    return response.json()

def add_user(data):
    url = f'{base_url}/users/'

    response = requests.post(url, json=data)
    return response.json()

def update_user(id, info):
    url = f'{base_url}/users/'

    response = requests.put(url, json={'id': id, 'info': info})
    return response.json()

def delete_user(id):
    url = f'{base_url}/users/'

    response = requests.delete(url, json={'id': id})
    return response.json()

if __name__ == '__main__':
    # print (get_user(1))
    # print (add_user({'name': 'John', 'age': 30}))
    # print (update_user(4, {'age': 25}))
     print (delete_user(4))
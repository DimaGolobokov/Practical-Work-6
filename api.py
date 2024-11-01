from flask import Flask, request, jsonify
import json
import os
import requests

def get_users():
    with open('users.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_user(id):
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

        if id in users:
            return users[id]

        return {'error': 'User not found'}

def add_user(data):
    users = get_users()
    with open('users.json', 'w', encoding='utf-8') as f:
        id = len(users) + 1

        users[id] = data
        json.dump(users, f)
        return {'success': 'User added'}

def update_user(id, info):
    users = get_users()

    with open('users.json', 'w', encoding='utf-8') as f:
        if id in users:
            for key, value in info.items():
                users[id][key] = value

            json.dump(users, f)
            return {'success': 'User updated'}

        return {'error': 'User not found'}

def delete_user(id):
    users = get_users()

    with open('users.json', 'w', encoding='utf-8') as f:
        if id in users:
            del users[id]
            json.dump(users, f)
            return {'success': 'User deleted'}

        return {'error': 'User not found'}

app = Flask(__name__)

@app.route('/users/', methods=['GET'])
def returnUsersInfo():
    id = request.args.get('id')

    return get_user(id)

@app.route('/users/', methods=['POST'])
def addUser():
    data = request.get_json()

    return add_user(data)

@app.route('/users/', methods=['DELETE'])
def deleteUser():
    id = request.get_json()['id']

    return delete_user(str(id))

@app.route('/users/', methods=['PUT'])
def updateUser():
    data = request.get_json()

    return update_user(str(data['id']), data['info'])

if __name__ == '__main__':
    app.run(debug=True)
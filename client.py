import requests
import json

class Client:

    def __init__(self):
        self.url = 'http://45.143.139.222'
        self.token = "none"

    def register(self, username, password):
        creds = {"username": username, "password": password}
        r = requests.post(f'{self.url}/register', data=creds)
        jsonData = json.loads(r.text)
        if jsonData["status"] != 200:
            return {'Error': jsonData['errors']}
        else:
            return {'Success': f'User {username}  was successfully created'}

    def setToken(self, username, password):
        creds = {"username": username, "password": password}
        r = requests.post(f'{self.url}/api/login_check', json=creds)
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData["message"]}
        else:
            self.token = jsonData["token"]
            return {'Success': 'Token was successfully set'}

    def getTodos(self):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.get(f'{self.url}/api/todo', headers={'Authorization': f'Bearer {self.token}'})
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData['errors']}
        return jsonData

    def getTodo(self, id):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.get(f'{self.url}/api/todo/{id}', headers={'Authorization': f'Bearer {self.token}'})
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData['errors']}
        return jsonData

    def addTodo(self,name):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.post(f'{self.url}/api/todo', headers={'Authorization': f'Bearer {self.token}'},
                          json={'name': name})
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData['errors']}
        else:
            return {'Success':'Post added successfully'}

    def deleteTodo(self, id):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.delete(f'{self.url}/api/todo/{id}', headers={'Authorization': f'Bearer {self.token}'})
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData['errors']}
        else:
            return {'Success': 'Post deleted successfully'}

    def updateTodo(self,id,name):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.put(f'{self.url}/api/todo/{id}', headers={'Authorization': f'Bearer {self.token}'},
                         json={'name':name})
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData['errors']}
        else:
            return {'Success': 'Post updated successfully'}
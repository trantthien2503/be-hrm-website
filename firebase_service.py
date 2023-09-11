import firebase_admin
from firebase_admin import credentials, db
import json
import random
import string
with open('resful-api-38eda-firebase-adminsdk-6u38o-0f93a07228.json', 'r') as json_file:
    appsettings = json.load(json_file)

certificate = credentials.Certificate(appsettings)

firebaseApp = firebase_admin.initialize_app(
    certificate, {"databaseURL": appsettings['databaseURL']})


class HRMCollection():

    def __init__(self, collection_name):
        self.collection = db.reference(collection_name)

    def __getSnapshot(self):
        return self.collection.get()

    def get_all_data(self):
        snapshot = self.__getSnapshot()
        if snapshot is None:
            return []
        all_data = []
        for key, value in snapshot.items():
            data = value.copy()  # Tạo bản sao của value để tránh thay đổi trong dictionary gốc
            all_data.append(data)
        return all_data

    def add_data(self, content):
        new_data = self.collection.push()
        new_id = new_data.key.lstrip("-")
        content['_id'] = new_id
        new_data.set(content)
        return content

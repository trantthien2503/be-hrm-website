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

    def get_all_data(self):
        try:
            snapshot = self.collection.get()
            if snapshot is None:
                return []
            all_data = list(snapshot.values())
            return all_data
        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", str(e))
            return []

    def add_data(self, data):
        try:
            new_data = self.collection.push()
            new_id = new_data.key
            data['_id'] = new_id
            new_data.set(data)
            return data
        except Exception as e:
            print("Lỗi khi thêm dữ liệu:", str(e))
            return None

    def update_data(self, data_id, new_data):
        try:
            data_ref = self.collection.child(data_id)
            data_ref.set(new_data)
        except Exception as e:
            print("Lỗi khi cập nhật dữ liệu:", str(e))

    def delete_data(self, data_id):
        try:
            data_ref = self.collection.child(data_id)
            data_ref.delete()
        except Exception as e:
            print("Lỗi khi xóa dữ liệu:", str(e))

    def search_data(self, field, value):
        try:
            query = self.collection.order_by_child(field).equal_to(value)
            result = query.get()
            if result is None:
                return []
            data = list(result.values())
            return data
        except Exception as e:
            print("Lỗi khi tìm kiếm dữ liệu:", str(e))
            return []

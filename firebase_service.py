import firebase_admin
from firebase_admin import credentials, db, auth
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
        # Lấy toàn bộ dữ liệu từ collection
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
        # Thêm dữ liệu mới vào collection
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
        # Cập nhật dữ liệu trong collection
        try:
            data_ref = self.collection.child(data_id)
            data_ref.set(new_data)
        except Exception as e:
            print("Lỗi khi cập nhật dữ liệu:", str(e))

    def delete_data(self, data_id):
        # Xóa dữ liệu khỏi collection
        try:
            data_ref = self.collection.child(data_id)
            data_ref.delete()
        except Exception as e:
            print("Lỗi khi xóa dữ liệu:", str(e))

    def search_data(self, field, value):
        # Tìm kiếm dữ liệu trong collection dựa trên trường và giá trị
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

    def create_user(self, email, password):
        # Tạo người dùng mới với email và mật khẩu.
        # Trả về thông tin người dùng được tạo thành công hoặc None nếu có lỗi.
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            return user
        except Exception as e:
            print("Lỗi khi tạo người dùng:", str(e))
            return None

    def delete_user(self, user_id):
        # Xóa người dùng dựa trên user_id.
        try:
            auth.delete_user(user_id)
        except Exception as e:
            print("Lỗi khi xóa người dùng:", str(e))

    def get_user(self, user_id):
        # Lấy thông tin người dùng dựa trên user_id.
        # Trả về thông tin người dùng hoặc None nếu không tìm thấy người dùng.
        try:
            user = auth.get_user(user_id)
            return user
        except Exception as e:
            print("Lỗi khi lấy thông tin người dùng:", str(e))
            return None

    def update_user(self, user_id, display_name=None, password=None):
        # Cập nhật thông tin người dùng dựa trên user_id.
        # Trả về thông tin người dùng sau khi cập nhật hoặc None nếu có lỗi.
        try:
            user = auth.update_user(
                user_id,
                display_name=display_name,
                password=password
            )
            return user
        except Exception as e:
            print("Lỗi khi cập nhật người dùng:", str(e))
            return None
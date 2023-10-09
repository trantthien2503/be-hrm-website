import firebase_admin
from firebase_admin import credentials, db, firestore

import json

with open('resful-api-38eda-firebase-adminsdk-6u38o-0f93a07228.json', 'r') as json_file:
    appsettings = json.load(json_file)

certificate = credentials.Certificate(appsettings)

firebaseApp = firebase_admin.initialize_app(
    certificate, {"databaseURL": appsettings['databaseURL']})

db = firestore.client()


class FirestoreCollection():

    def __init__(self, collection_name):
        self.collection = db.collection(collection_name)

    def get_all_data(self):
        """Return all documents in collection"""
        try:
            collections = self.collection.get()
            collections_dict = []
            
            for doc in collections:
                collections_dict.append(doc.to_dict())
            
            return collections_dict
        except Exception as e:
            print("Error getting collections:", e)
            return []    

    def add_data(self, data):
        try:
            # Tạo document mới 
            doc_ref = self.collection.document()  
            doc_ref.set(data)

            doc = doc_ref.get()
            doc_data = doc.to_dict()

            return doc_data

        except Exception as e:
            print("Error adding document: ", e)
            return None

    def update_data(self, doc_id, updates):
        # Cập nhật dữ liệu trong collection
        try:
            # Lấy document theo id
            doc = self.collection.document(doc_id)
            
            # Cập nhật dữ liệu
            doc.update(updates)

        except Exception as e:
            print("Error updating document: ", e)

    # def delete_data(self, data_id):
    #     # Xóa dữ liệu khỏi collection
    #     try:
    #         print("data_id \n", data_id)
    #         # Tìm kiếm dữ liệu theo trường _id trong collection
    #         query = self.collection.order_by_child(
    #             '_id').equal_to(data_id).get()

    #         # Kiểm tra xem có dữ liệu tồn tại hay không
    #         if query:
    #             # Lấy khóa của dữ liệu tồn tại
    #             existing_key = list(query.keys())[0]

    #             # Thực hiện xóa dữ liệu
    #             self.collection.child(existing_key).delete()

    #             return None
    #         else:
    #             print("Không tìm thấy dữ liệu với _id =", data_id)
    #     except Exception as e:
    #         print("Lỗi khi xóa dữ liệu:", str(e))

    # def search_data(self, field, value):
    #     # Tìm kiếm dữ liệu trong collection dựa trên trường và giá trị
    #     try:
    #         query = self.collection.order_by_child(field).equal_to(value)
    #         result = query.get()
    #         if result is None:
    #             return []
    #         data = list(result.values())
    #         return data
    #     except Exception as e:
    #         print("Lỗi khi tìm kiếm dữ liệu:", str(e))
    #         return []

    # def create_user(self, email, password):
    #     # Tạo người dùng mới với email và mật khẩu.
    #     # Trả về thông tin người dùng được tạo thành công hoặc None nếu có lỗi.
    #     try:
    #         user = auth.create_user(
    #             email=email,
    #             password=password
    #         )
    #         return user
    #     except Exception as e:
    #         print("Lỗi khi tạo người dùng:", str(e))
    #         return None

    # def delete_user(self, user_id):
    #     # Xóa người dùng dựa trên user_id.
    #     try:
    #         auth.delete_user(user_id)
    #     except Exception as e:
    #         print("Lỗi khi xóa người dùng:", str(e))

    # def get_user(self, user_id):
    #     # Lấy thông tin người dùng dựa trên user_id.
    #     # Trả về thông tin người dùng hoặc None nếu không tìm thấy người dùng.
    #     try:
    #         user = auth.get_user(user_id)
    #         return user
    #     except Exception as e:
    #         print("Lỗi khi lấy thông tin người dùng:", str(e))
    #         return None

    # def update_user(self, user_id, display_name=None, password=None):
    #     # Cập nhật thông tin người dùng dựa trên user_id.
    #     # Trả về thông tin người dùng sau khi cập nhật hoặc None nếu có lỗi.
    #     try:
    #         user = auth.update_user(
    #             user_id,
    #             display_name=display_name,
    #             password=password
    #         )
    #         return user
    #     except Exception as e:
    #         print("Lỗi khi cập nhật người dùng:", str(e))
    #         return None

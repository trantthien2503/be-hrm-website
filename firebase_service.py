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
            # Lấy id và thêm vào data
            doc_ref = self.collection.document()
            id = doc_ref.id
            data['id'] = id
            
            doc_ref.set(data)

            doc = doc_ref.get()
            doc_data = doc.to_dict()

            # Thêm thông báo thành công
            response = {
            'data': doc_data,
            'message': 'Thêm dữ liệu thành công'
            }

            return response

        except Exception as e:
            print("Error adding document: ", e)
            return {
            'message': 'Lỗi khi thêm dữ liệu'  
            }

    def update_data(self, doc_id, updates):
        # Cập nhật dữ liệu trong collection
        try:    
            doc = self.collection.document(doc_id)

            doc.update(updates)

            return {'message': 'Cập nhật thành công'}

        except ValueError as e:
            return {'message': str(e)}

        except Exception as e:
            return {'message': f'Lỗi không xác định: {e}'}

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

    def search_data(self, field, value):
        try:
  
            # Kiểm tra đầu vào 
    
            query = self.collection.order_by(field)
            
            # Truy vấn trực tiếp
            results = query.document(value).get()  

            if not results:
                return []

            data = []
            for doc in results:
                data.append(doc.to_dict())
            
            return data

        except ValueError as err:
            return {'message': str(err)}

        except Exception as err:
            return {'message': f'Lỗi không xác định: {err}'}
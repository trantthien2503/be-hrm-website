from flask import Blueprint, jsonify, request
from firebase_service import FirestoreCollection
from datetime import datetime

# Tạo blueprint với tên là "main"
main_bp = Blueprint('main', __name__)
# Định nghĩa route cho blueprint "main"

# Api lấy danh toàn bộ danh sách actors
@main_bp.route('/api/get-actors', methods=['GET'])
def getActor():
    fire = FirestoreCollection("actors")
    data = fire.get_all_data()
    return jsonify(data)


# # APi lấy actor theo id
# @main_bp.route('/api/get-actor', methods=['POST'])
# def getActorById():
#     req = request.get_json()
#     idActor = req.get('_id')
#     hrm = HRMCollection("actors")
#     data = hrm.get_data_by_field('_id', idActor)[0]
#     # dữ liệu phương thức get_data_by_field sẽ trả về dạng mảng
#     return jsonify(data)


# Api api thêm 1 actor
@main_bp.route('/api/add-actor', methods=['POST'])
def addActor():
   # Thực hiện lấy toàn bộ dữ liệu truyền từ client theo dạng post
    req = request.get_json()
    data = {
        'firstname': req.get('firstname'),
        'lastname': req.get('lastname'),
    }
    fire = FirestoreCollection("actors")
    newData = fire.add_data(data)
    return jsonify(newData)


# # Api api cập 1 actor theo trường _id
# @main_bp.route('/api/update-actor', methods=['POST'])
# def updateActorById():
#    # Thực hiện lấy toàn bộ dữ liệu truyền từ client theo dạng post
#     req = request.get_json()
#     idActor = req.get('_id')
#     dataUpdate = {
#         'firstname': req.get('firstname'),
#         'lastname': req.get('lastname'),
#         'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     }
#     hrm = HRMCollection("actors")
#     data = hrm.update_data(idActor, dataUpdate)
#     # Kiểm tra dữ liệu trả về là None thì thành công
#     if (data == None):
#         return jsonify(
#             {'message': 'Cập nhật thành công !', 'result': True})
#     else:
#         return jsonify(
#             {'message': 'Cập nhật không thành công !', 'result': False})


# # Api api xóa 1 actor
# @main_bp.route('/api/delete-actor', methods=['POST'])
# def deleteActorById():
#    # Thực hiện lấy toàn bộ dữ liệu truyền từ client theo dạng post
#     req = request.get_json()
#     idActor = req.get('_id')
#     hrm = HRMCollection("actors")
#     data = hrm.delete_data(idActor)
#     # Kiểm tra dữ liệu trả về là None thì thành công
#     if (data == None):
#         return jsonify(
#             {'message': 'Xóa thành công !', 'result': True})
#     else:
#         return jsonify(
#             {'message': 'Xóa không thành công !', 'result': False})

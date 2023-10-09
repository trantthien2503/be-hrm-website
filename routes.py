from flask import Blueprint, jsonify, request
from firebase_service import FirestoreCollection

from model.staffinfo import Staffinfo

# Tạo blueprint với tên là "main"
main_bp = Blueprint('main', __name__)
# Định nghĩa route cho blueprint "main"

# Api lấy danh toàn bộ danh sách staffinfo
@main_bp.route('/api/get-all-staffinfo', methods=['GET'])
def get_allStaffinfo():
    firestore = FirestoreCollection("staffinfos")
    data = firestore.get_all_data()
    return jsonify(data)

# Api thêm staffinfo bất kỳ
@main_bp.route('/api/add-staffinfo', methods=['POST'])
def add_staff():
    req = request.get_json() # Tạo đối tượng Staffinfo từ dữ liệu nhận được
    staff = Staffinfo(req)# Tạo đối tượng Staffinfo từ dữ liệu nhận được
    staff_dict = staff.__dict__   # Chuyển đổi đối tượng Staffinfo sang dictionary

    firestore = FirestoreCollection("staffinfos")# Khởi tạo đối tượng giao tiếp với collection staffinfos trong Firestore
    newData = firestore.add_data(staff_dict) # Thêm dữ liệu vào Firestore
    return jsonify(newData)

# Api cập nhật staffinfo bất kỳ
@main_bp.route('/api/update-staffinfo', methods=['POST'])
def update_staffById():
    req = request.get_json() # Tạo đối tượng Staffinfo từ dữ liệu nhận được
    id = req.get('id')
    if id:
        staff = Staffinfo(req)# Tạo đối tượng Staffinfo từ dữ liệu nhận được
        staff_dict = staff.__dict__   # Chuyển đổi đối tượng Staffinfo sang dictionary
        firestore = FirestoreCollection("staffinfos")# Khởi tạo đối tượng giao tiếp với collection staffinfos trong Firestore
        update = firestore.update_data(id,staff_dict)
        return jsonify(update)
    else:
        return jsonify({'message': 'Thiếu id dữ liệu'})

 




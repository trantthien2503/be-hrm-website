from flask import Blueprint, jsonify, request
from firebase_service import FirestoreCollection
from datetime import datetime

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
    req = request.get_json()
    staff = Staffinfo(req)
    firestore = FirestoreCollection("staffinfos")
    newData = firestore.add_data(staff)
    return jsonify(newData)


from flask import Blueprint, jsonify
from firebase_service import HRMCollection

# Tạo blueprint với tên là "main"
main_bp = Blueprint('main', __name__)
# Định nghĩa route cho blueprint "main"


@main_bp.route('/api/', methods=['GET'])
def index():
    data = {"name": "John Doe", "age": 32}
    hrm = HRMCollection("employees")
    new_id = hrm.add_data(data)
    print(jsonify(new_id))
    return jsonify(new_id)


@main_bp.route('/api/get-employees', methods=['GET'])
def getEmployees():
    hrm = HRMCollection("employees")
    data = hrm.get_all_data()
    return jsonify(data)

from flask import Blueprint, jsonify

# Tạo blueprint với tên là "main"
main_bp = Blueprint('main', __name__)

# Định nghĩa route cho blueprint "main"
@main_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my project'})

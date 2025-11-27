from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)

# Cấu hình đường dẫn tới thư mục Mapdata
# Đảm bảo bạn đã tạo thư mục 'Mapdata' cùng cấp với file app.py và chứa các file .geojson
MAP_DATA_FOLDER = os.path.join(os.getcwd(), 'Mapdata')

@app.route('/')
def index():
    """Route chính để hiển thị giao diện bản đồ"""
    return render_template('index.html')

@app.route('/api/map/<filename>')
def get_map_data(filename):
    """API để frontend gọi và lấy dữ liệu GeoJSON"""
    # Chỉ cho phép tải các file an toàn
    allowed_files = [
        'Wards_2008.geojson', 
        'Wards_2025.geojson',
        'Districts_2008.geojson', 
        'Provinces_2025_34.geojson', 
        'Provinces_2008_63.geojson'
    ]
    
    if filename not in allowed_files:
        return jsonify({"error": "File not found or not allowed"}), 404
        
    return send_from_directory(MAP_DATA_FOLDER, filename)

if __name__ == '__main__':
    # Kiểm tra thư mục tồn tại chưa
    if not os.path.exists(MAP_DATA_FOLDER):
        print(f"Cảnh báo: Thư mục '{MAP_DATA_FOLDER}' không tồn tại. Hãy tạo nó và copy file GeoJSON vào.")
    
    print("Server đang chạy tại http://127.0.0.1:5000")
    app.run(debug=True)
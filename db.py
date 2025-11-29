# file: db.py
import json

DATABASE_FILE = "db.json"

def load_db():
    """Tải dữ liệu từ file db.json."""
    try:
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Trả về dictionary rỗng nếu file chưa tồn tại
        return {} 
    except json.JSONDecodeError:
        # Xử lý trường hợp file bị hỏng hoặc rỗng
        return {} 

def save_db(data):
    """Lưu dữ liệu vào file db.json."""
    with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


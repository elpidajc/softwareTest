from flask import Flask, request, jsonify
import pymysql
from werkzeug.security import generate_password_hash
import traceback

app = Flask(__name__)

def get_conn():
    return pymysql.connect(
        host="localhost",           # 本地 MySQL
        user="root",                # 你的 MySQL 用户
        password="Jx12345678",      # 你的 MySQL 密码
        database="db_01",           # 你的数据库名
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': '用户名和密码必填'}), 400

    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            # 插入新用户
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)
            )
            conn.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        print("数据库错误:", e)
        traceback.print_exc()
        return jsonify({'error': '数据库错误'}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(port=5000)
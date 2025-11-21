from flask import Flask, request
import pymysql

app = Flask(__name__)


def get_db_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Jx12345678",
        database="db_01",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # 演示危险写法：直接拼接SQL（仅用于学习，实际项目绝对禁止！）
    sql = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    try:
        conn = get_db_conn()
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
        conn.close()
        if result:
            return "登录成功"
        else:
            return "用户名或密码错误", 400
    except Exception as e:
        return f"数据库错误: {e}", 500


if __name__ == "__main__":
    app.run()

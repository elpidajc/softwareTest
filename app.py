from flask import Flask, request, jsonify, make_response
import pymysql
import os
import time
import traceback

app = Flask(__name__)


def get_conn():
    host = os.environ.get("DB_HOST", "codes-mysql_db-1")
    user = os.environ.get("DB_USER", "root")
    password = os.environ.get("DB_PASSWORD", "Jx12345678")
    database = os.environ.get("DB_NAME", "db_01")
    retries = 5
    while retries > 0:
        try:
            print(f"尝试连接数据库主机: {host}")
            return pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset="utf8mb4",
                connect_timeout=5,
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            print(f"数据库连接失败，重试中... 剩余重试次数: {retries}")
            retries -= 1
            time.sleep(2)
    raise Exception("无法连接到数据库，请检查配置")


def no_cache_response(data, status):
    resp = make_response(jsonify(data), status)
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp


@app.route("/order", methods=["POST"])
def order():
    if not request.is_json or request.json is None:
        return no_cache_response({"error": "请求体不是有效的JSON"}, 400)
    item = request.json.get("item")
    qty = request.json.get("qty", 1)
    if not item or not isinstance(qty, int) or qty < 1:
        return no_cache_response({"error": "参数无效"}, 400)
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            cursor.execute("SELECT stock FROM inventory WHERE item=%s", (item,))
            row = cursor.fetchone()
            if not row:
                return no_cache_response({"error": "不存在的商品"}, 400)
            stock = row["stock"]
            if stock < qty:
                return no_cache_response({"error": "库存不足", "当前库存": stock, "请求数量": qty}, 400)
            cursor.execute("UPDATE inventory SET stock=stock-%s WHERE item=%s", (qty, item))
            conn.commit()
            cursor.execute("SELECT stock FROM inventory WHERE item=%s", (item,))
            left = cursor.fetchone()["stock"]
        return no_cache_response({"success": True, "剩余库存": left}, 200)
    except Exception as e:
        # 打印异常堆栈方便调试
        traceback.print_exc()
        # 返回 503 响应和错误信息
        return no_cache_response({"error": "服务暂时不可用", "detail": str(e)}, 503)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)



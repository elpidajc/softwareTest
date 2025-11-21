import time
import requests


def test_reliability():
    start = time.time()
    success, fail = 0, 0
    for i in range(1000):
        try:
            res = requests.post("http://127.0.0.1:5000/order", json={"item": "book", "qty": 1})
            if res.status_code == 200:
                success += 1
            elif res.status_code == 400:
                fail += 1
            else:
                print(f"Unexpected status: {res.status_code}")
        except Exception as e:
            print(f"Request error on iteration {i}: {e}")
            fail += 1
    end = time.time()
    print(f"运行时长: {end - start} 秒")
    print(f"成功次数: {success}, 失败次数: {fail}")


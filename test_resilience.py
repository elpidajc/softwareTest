import requests, time, subprocess


def test_db_failure_recovery():
    subprocess.run(["docker", "stop", "codes-mysql_db-1"])
    time.sleep(5)
    res = requests.post("http://127.0.0.1:5000/order", json={"item": "book", "qty": 1})
    assert res.status_code in (500, 503)  # 返回 500 或 503 均可
    subprocess.run(["docker", "start", "codes-mysql_db-1"])
    time.sleep(5)
    res2 = requests.post("http://127.0.0.1:5000/order", json={"item": "book", "qty": 1})
    assert res2.status_code == 200


if __name__ == "__main__":
    # res2 = requests.post("http://127.0.0.1:5000/order", json={"item": "book", "qty": 1})
    # print(res2.json())
    pass

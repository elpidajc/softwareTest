import requests


def test_sql_injection():
    url = "http://127.0.0.1:5000/login"
    payload = {"username": "admin", "password": "' OR 1=1 -- "}
    res = requests.post(url, data=payload)
    print("响应内容:", res.text)



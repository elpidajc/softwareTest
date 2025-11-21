from locust import HttpUser, task, between
import random
import string


def random_username():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def register(self):
        username = random_username()
        password = "testpassword"
        self.client.post("/register", json={
            "username": username,
            "password": password
        })

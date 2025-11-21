from selenium import webdriver
import time


def test_login_page_chrome():
    driver = webdriver.Chrome()  # 需已安装chromedriver并配置环境变量
    driver.get("http://127.0.0.1:5000/login")
    assert "登录" in driver.page_source
    time.sleep(1)
    driver.quit()


def test_login_page_firefox():
    driver = webdriver.Firefox()  # 需已安装geckodriver并配置环境变量
    driver.get("http://127.0.0.1:5000/login")
    assert "登录" in driver.page_source
    time.sleep(1)
    driver.quit()

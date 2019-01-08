# coding:utf-8
from selenium import webdriver
import pytest
import time

@pytest.fixture(scope="module")
def driver(request):
    d = webdriver.Firefox()
    print("\n module:start firefox")

    def fn():
        d.quit()
    request.addfinalizer(fn)
    return d

@pytest.fixture(scope="function")
def start(driver):
    print("function: open baidu")
    driver.get("https://www.baidu.com")
    time.sleep(1)

def test_01(driver,start):
    print("用例1")
    driver.find_element_by_id("kw").send_keys("hello")
    driver.find_element_by_id("su").click()
    time.sleep(1)
    print(driver.title)
    assert "hello" in driver.title

def test_02(driver,start):
    print("用例2")
    driver.find_element_by_id("kw").send_keys("hello world!")
    driver.find_element_by_id("su").click()
    time.sleep(1)
    print(driver.title)
    assert "hello world!" in driver.title

if __name__ == '__main__':
    pytest.main(["-s","test_1.py"])
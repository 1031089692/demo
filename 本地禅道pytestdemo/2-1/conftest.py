# coding:utf-8

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Firefox()

    def end():
        driver.quit()
    request.addfinalizer(end)  #终结函数
    return driver
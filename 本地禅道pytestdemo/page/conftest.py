# coding:utf-8
import pytest
from selenium import webdriver
from page.loginpage import login

@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Firefox()

    login(driver)

    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver


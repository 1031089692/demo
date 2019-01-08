# coding:utf-8
from selenium import  webdriver
from common.base import Base

url = "http://eledata.superboss.cc/jump.jsp"

loc_name = ("xpath","//input[@name='shopName']")
loc_button = ("xpath","//*[@method='post']/input[3]")
loc_expect = ("xpath","//*[@class='ele_shopName']")
loc_error_expect = ("xpath","//div[@class='sui-container']")

def login(driver,user="isv_TEST2"):
    a = Base(driver)
    driver.get(url)
    a.sendKeys(loc_name,user)
    a.click(loc_button)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    login(driver)
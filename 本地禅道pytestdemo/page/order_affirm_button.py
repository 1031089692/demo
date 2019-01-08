# coding:utf-8
import pytest
from common.base import Base
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

class OrderAffirmButton(Base):
    # 进入订单确认提醒
    Marketing_messages = ("xpath","//*[@id='eleTree']/ul/li[2]/div")
    Order_arrirm = ("xpath","//*[@id='eleTree']/ul/li[2]/ul/li[1]/a")
    # 开关状态为未关闭的时候定位这个button
    order_affirm_left_button = ("xpath","//div[@class='el-switch__label el-switch__label--left']/span")
    # 状态为已关闭时定位这个button
    order_arrirm_right_button = ("xpath","//div[@class='el-switch__label el-switch__label--right']/span")
    Secondary_confirmation = ("xpath","//button[@class='el-button el-button--default el-button--primary']")

    @pytest.fixture(scope="function",autouse=True)
    def start(self,driver):
        print("function: open eledata.superboss.cc")
        driver.get("https://eledata.superboss.cc/index.html?shopId=161460453&login=ele&first=1#/")

    def test_open_button(self,):
        self.click(self.Marketing_messages)
        self.click(self.Order_arrirm)
        button_left_text = self.findElement(self.order_affirm_left_button)
        try:
            if button_left_text.is_displayed() is False:
                self.click(self.order_arrirm_right_button)
            elif button_left_text.is_displayed() is True:
                pass
            else:
                print('定位异常')
        except Exception as e:
            print(e)
        #print(button_left_text.text)
        return button_left_text.text

    def test_close_button(self,):
        self.click(self.Marketing_messages)
        self.click(self.Order_arrirm)
        button_left_text = self.findElement(self.order_affirm_left_button)
        #print(button_left_text.is_displayed())
        try:
            if button_left_text.is_displayed() is False:
                pass
            elif button_left_text.is_displayed() is True:
                self.click(self.order_affirm_left_button)
                self.click(self.Secondary_confirmation)
            else:
                print('定位异常')
        except Exception as e:
            print(e)
        button_right_text = self.findElement(self.order_arrirm_right_button)
        return button_right_text.text

if __name__ == '__main__':
    pytest.main(["-s","order_affirm_button.py"])
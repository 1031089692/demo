# coding:utf-8
# coding:utf-8
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
class Base(object):
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 1

    def findElementnew(self,loctor):
        '''定位到元素，返回元素对象。没定位到，返回timeout异常'''
        if not isinstance(loctor,tuple):
            print('locator参数类型错误，必须传元祖类型:loc=("id","value1")')
        else:
            print("正在定位元素的信息：定位方式->%s,value值->%s"%(loctor[0],loctor[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(Ec.presence_of_all_elements_located(loctor))
            return ele

    def findElement(self,loctor):
        '''
        加入强制等待的原因是因为定位虚拟dom的bug
        '''
        if not isinstance(loctor,tuple):
            print('locator参数类型错误，必须传元祖类型:loc=("id","value1")')
        else:
            try:
                print("正在定位元素的信息：定位方式->%s,value值->%s"%(loctor[0],loctor[1]))
                ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*loctor))
                time.sleep(2)
                return ele
            except:
                return []

    def findElements(self,loctor):
        '''
        driver:游览器实例。 timeout总时长（默认30s）
        poll：poll_frequency：循环去查询的间隙时间（默认0.5s）
        '''
        if not isinstance(loctor,tuple):
            print('locator参数类型错误，必须传元祖类型:loc=("id","value1")')
        else:
            try:
                print("正在定位元素的信息：定位方式->%s,value值->%s"%(loctor[0],loctor[1]))
                ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x:\
                x.find_element(*loctor))
                return ele
            except:
                return []

    def click(self,loctor):
        ele = self.findElement(loctor)
        ele.click()

    def sendKeys(self, loctor, text, is_clear_first=False):
        '''
        is_claer_first默认为False,不清空输入框
        '''
        ele = self.findElement(loctor)
        if is_clear_first:
            ele.clear()     #is_clear_first 在为Ture的时候执行
        ele.send_keys(text)

    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExits(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExits2(self,locator):
        eles = self.findElement(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到的元素个数：%s"%n)
            return True

    def is_title(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(Ec.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(Ec.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(Ec.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''返回bool值,value字符串为空，返回Fasle'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(Ec.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(Ec.alert_is_present())
            return result
        except:
            return False



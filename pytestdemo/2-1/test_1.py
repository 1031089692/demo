# coding:utf-8

import pytest
import time

def test_blog(driver):
    driver.get("http://www.baidu.com")
    time.sleep(3)
    t = driver.title
    print("测试结果：%s"%t)
    assert "百度一下" in t,"失败原因，打开百度失败"

if __name__ == '__main__':
    pytest.main(["-s","test_1.py"])
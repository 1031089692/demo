# coding:utf-8
import pytest

#函数式

def setup_module():
    print("setup_module ：整个y .py  模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module ：整个y .py  模块只执行一次")
    print("比如：所有用例结束后最后关闭游览器")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行---test_two")
    x = 'hello'
    assert hasattr(x,'check')

def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello owrld"
    assert a in b

if __name__ == "__main__":
    pytest.main(["s","case3.py"])
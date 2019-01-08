# coding:utf-8
import pytest

#函数式

def setup_function():
    print("setup_function:每个用例开始前都会执行")

def teardown_function():
    print("teatdown_function:每个用例结束后都会执行")

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
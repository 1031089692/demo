# coding:utf-8

def f():
    return 3

def test_function():
    a = f()
    assert a % 2 ==0,"判断a是否能被2整除，当前a的值为：%s"%a


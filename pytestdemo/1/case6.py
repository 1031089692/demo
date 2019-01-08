# coding:utf-8
import pytest

def setup_module():
    print("set_module:整个.py模块只执行一次")
    print("比如：所有用例开始之前只打开一次游览器")
def teardown_module():
    print("teardown_module:整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭游览器")
def setup_function():
    print("setup_function:每个用例开始前都会执行")
def teardown_function():
    print("setup_function:每个用例结束后都会执行")
def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x
def test_two():
    print("正在执行---test_two")
    x = 'hello'
    assert hasattr(x,'check')
class TestCase():
    def setup_class(self):
        print("setup_class:所有用例执行之前")
    def teardown_class(self):
        print("teardown_class:所有用例执行之后")
    def test_three(self):
        print("正在执行---test_three")
        x = "this"
        assert 'h' in x
    def test_four(self):
        print("正在执行---test_four")
        x = "hello"
        assert hasattr(x,'check')
if __name__ == "__main__":
    pytest.main(["s","case6.py"])
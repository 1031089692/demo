# coding:utf-8
import pytest

#yield可以在遇到报错时，继续运行一下个模块。

@pytest.fixture(scope="module")
def open():
    print("打开游览器，并且打开百度首页")

    yield
    print("执行teardown！")
    print("最后关闭游览器")

def test_s1(open):
    print("用例1：搜索python-1")
    raise NameError

def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["s","test_fix2"])
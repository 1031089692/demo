# coding:utf-8
import pytest

def test_one():
    print("正在执行----test_one")

@pytest.mark.skip(reason="Temporarily unable to test")
def test_two():
    print("正在执行---test_two")

def test_three():
    print("正在执行----test_three")

if __name__ == "__main__":
    pytest.main("['skip_1.py']")
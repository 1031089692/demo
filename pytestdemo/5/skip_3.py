# coding:utf-8

#通过调用来在测试执行或设置期间强制跳过
# import pytest
# def test_function():
#     if not valid_config():
#         pytest.skip("unsupoorted configuration")


#跳过整个模块级别
import pytest

def test_one():
    pytest.skip("--custom-flag is missing,skipping tests",allow_module_level=True)
    print("正在执行----test_one")

def test_two():
    print("正在执行---test_two")

def test_three():
    print("正在执行----test_three")

if __name__ == "__main__":
    pytest.main('skip_3.py')
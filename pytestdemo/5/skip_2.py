# coding:utf-8
import pytest
import sys
#pytest官网例子(python版本低于3.3会被skip，否则不会)
@pytest.mark.skipif(sys.version_info < (3,3),reason="requires python3.3")
def test_function():
    print("正在执行----test_function")

if __name__ == "__main__":
    pytest.main('skip_2.py')

# import pytest
# import sys
# #判断如果是win系统，则skip。
# @pytest.mark.skipif(sys.platform == 'win32',reason="does not run on windows")
# def test_function():
#     print("正在执行----test_function")
#
# if __name__ == "__main__":
#     pytest.main('skip_2.py')
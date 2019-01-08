# coding:utf-8
import pytest

@pytest.fixture (scope= "function")
def  start(request):
    print(  '\ \n n ----- 开始执行  function ----'  )

@pytest.mark.usefixtures( "start")
def  test_a ():
    print("  ------- 用例 a a  执行 -------")

if __name__ == "__main__":
    pytest.main(["s","test_fix6.py"])
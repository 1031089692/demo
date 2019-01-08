# coding:utf-8
import pytest

# 登录函数传参

test_login_data = [("admin", "111111"),("admin", "")]


def login(user,psw):
    # 普通登录函数
    print("登录账号：%s"%user)
    print("登录密码：%s"%psw)
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize("user,psw",test_login_data)
def test_login(user, psw):
    # 登录用例
    result = login(user, psw)
    assert result == True,"失败原因：密码为空"

if __name__ == "__main__":
    pytest.main(["-s","case1.py"])
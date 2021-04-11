# coding utf-8
import pytest

#测试登录数据
test_login_data = [("admin", "111111"), ("admin2","")]

def login(user, pwd):
     #普通登录函数
    print("登录帐号：%s" %user)
    print("登录密码：%s" %pwd)
    if pwd:
        return True
    else:
        return False

@pytest.mark.parametrize("user, pwd", test_login_data)
def test_login(user, pwd):
    #登录用例
    result = login(user, pwd)
    assert result == True, "失败原因：密码不能为空"

if __name__ == "__main__":
    pytest.main(['-s', 'test_01.py'])



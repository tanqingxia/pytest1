#coding utf-8
import pytest

#c测试帐号数据
test_user = ["admin1", "admin2", "admin3"]
test_psw = ["11111", "22222", "3333"]

@pytest.fixture(scope='module')
def input_user(request):
    user = request.param
    print("登录帐号： %s" % user)
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" %psw)
    return psw

@pytest.mark.parametrize("input_user", test_user, indirect=True)
@pytest.mark.parametrize("input_psw", test_psw, indirect=True)
def test_login(input_user,input_psw):
    '''组合模式'''
    a = input_user
    b = input_psw
    print("测试数据a=>%s, b->%s" % (a, b))
    assert b

if __name__ == "__main__":
    pytest.main(['-s', "test_04.py"])

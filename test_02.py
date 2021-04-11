#coding utf-8

import pytest

#测试帐号数据 list中元祖
test_login_data = [("admin","11111"), ("admin2","22222")]
#测试帐号数据 list中字典
test_login_data1 = [{"user":"user1", "pwd": "11111"}, {"user":"user2", "pwd": "11111"}]
@pytest.fixture(scope="module")
def login(request):
    user = request.param
    #print("登录帐号%s" %user)
    print("登录login")
    return user
@pytest.mark.parametrize("login", test_login_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print("测试用例中login的返回值：%s" %a[0])
    assert a != "", "返回%s" %a  #断言成功不返回

@pytest.mark.parametrize("login", test_login_data1, indirect=True)
def test_login2(login):
    '''登录2'''
    a = login
    print("测试用例login返回值：用户名{user},密码：{pwd}".format(**a))

if __name__ == "__main__":
    pytest.main(["-s", "test_02.py"])

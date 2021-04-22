#coding utf-8
import pytest

#canshu = [{"user":"admin", "pwd":"1111"}]
canshu = [{"user":"admin", "pwd":""}]

@pytest.fixture(scope="module")
def login(request):
    user = request.param['user']
    pwd = request.param['pwd']
    print("登录名%s,密码%s" %(user, pwd))

    if pwd:
        return True
    else:
        return False

@pytest.mark.parametrize("login", canshu, indirect=True)
class Test_05:
    def test_01(self, login):
        result = login
        print("用例1：%s" %result)
        assert result == True

    def test_02(self, login):
        result = login
        print("用例2：%s" % result)
        if not result:
            pytest.xfail("登录不成功，标记为xfail")
        assert 1 == 1

    def test_03(self, login):
        result = login
        print("用例2：%s" % result)
        if not result:
            pytest.xfail("登录不成功3，标记为xfail")
        assert 1 == 1


if __name__ == "__main__":
    pytest.main(["-s", "test_05.py"])
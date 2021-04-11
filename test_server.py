# coding utf-8

import pytest

@pytest.mark.webtest
def test_send_http():
    print("webtest")
    pass

def test_something_quick():
    print("111")
    pass

def test_another():
    print("222")
    pass

class TestClass:
    def test_method(self):
        print("333")
        pass

if __name__ == "__main__":
    #pytest.main(["-s", "test_server.py", "-m=webtest"])
    pytest.main(["-v", "test_server.py", "-m='not webtest'"])
    #pytest.main(["-v", "test_server.py::TestClass::test_method"])

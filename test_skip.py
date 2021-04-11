#coding utf-8
import pytest
import sys

#使用装饰器跳过
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    if not 'a':
        print("skip 跳过")
#跳过整个模块
def test_mpdule_skip():
    if not pytest.config.getoption("--custom-flag"):
        pytest.skip("--custom-flag is missing, skipping tests", allow_module_level=True)

###skipif
@pytest.mark.skipif(sys.version_info < (3,6), reason="requires python3.6 or higher")
def test_function():
    print("higher")

if __name__ == "__main__":
    pytest.main(['-s', "test_skip.py"])


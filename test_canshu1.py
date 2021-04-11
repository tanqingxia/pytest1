#coding:utf-8

import pytest
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [3, 5])
@pytest.mark.parametrize("z", [7, 8])
def test_eval(x, y, z):
    print("测试数据组合：x->%s, y->%s, z->%s" % (x, y, z))

if __name__ == "__main__":
    pytest.main(['-s', "test_canshu1.py"])
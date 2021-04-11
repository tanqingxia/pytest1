#coding:utf-8

import pytest

def test_s1(login):
    print("yongli1：xian denglu ")

def test_s2():
    print("s2:bu loging")

if __name__ == "__main__":
    pytest.main(["-s", "test_fix1.py"])
import pytest

def setup_function():
    print("setup_function 每个用例前都会执行")
def teardown_function():
    print("teardown_function 每个用例之后都会执行")
def test_one():
    print("test_one")
def test_two():
    print("test_two")
def setup_module():
    print("只在整个。py模块前执行一次")
def teardown_module():
    print("只在整个。py模块后执行一次")
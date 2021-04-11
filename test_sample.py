#  content of  test_sample.py
import pytest
def func(x):
    return x +1

def test_answer(cmdopt):
   if cmdopt == "type1":
       print("first1")
   elif cmdopt == "type2":
       print("second")
   assert 0

if __name__ == "__main__":
    pytest.main(["-s", "test_case1.py"])
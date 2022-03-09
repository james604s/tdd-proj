# test_no_mark.py

"""
1. :: 標記
pytest udemy_pytest/test_no_mark.py::test_func1
缺點: 一次只能指定一個 Test Function
2. -k 模糊匹配
缺點: 可batch操作, 所有Test Function 需相同Mode
pytest -k func1 udemy_pytest/test_no_mark.py
3. -m pytest.mark 選擇測試時標記的Test Func
pytest -m finished tests/test-function/test_with_mark.py
一个函数可以打多个標記；多个函数也可以打相同的標記。
pytest -m "finished and commit"
pytest -m "finished and not merged"
"""
def test_func1():
    assert 1 == 1

def test_func2():
    assert 1 != 1

# test_with_mark.py

@pytest.mark.finished
def test_func1():
    assert 1 == 1

@pytest.mark.unfinished
def test_func2():
    assert 1 != 1
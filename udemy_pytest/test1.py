

# . 標示測試成功
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

# F 標示測試失敗
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
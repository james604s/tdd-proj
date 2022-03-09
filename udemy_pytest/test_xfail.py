# test_xfail.py

# 如果事先知道Test Func 會失敗, 但不想跳過, 希望得到提示。
# x 預見失敗, 實際失敗。
# X 預見失敗, 實際成功。
@pytest.mark.xfail(gen.__version__ < '0.2.0',
                   reason='not supported until v0.2.0')
def test_api():
    id_1 = gen.unique_id()
    id_2 = gen.unique_id()
    assert id_1 != id_2
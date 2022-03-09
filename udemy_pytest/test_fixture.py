
"""
Fixture是一些函数，pytest 會在執行測試函數之前或之後加載他們。
我们可以利用Fixture做任何事情，其中最常見的可能是DB 初始化連線與關閉。
Pytest 使用 pytest.fixture() 定義Fixture。

Fixture可以直接定義在個Test Script中，
更多時候希望一個Fixture可以在更大程度上重複利用，需要對Fixture集中管理。
Pytest 使用文件 conftest.py 集中管理Fixture。
在複雜的項目中，可以在不同的目錄層級定義 conftest.py，其作用域為其所在的目錄和子目錄。

conftest會自動調用, 可以當plugin理解。
"""
import pytest

@pytest.fixture()
def postcode():
    return '010'


def test_postcode(postcode):
    assert postcode == '010'
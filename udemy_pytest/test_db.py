# test_db.py


"""

很多需要再測試前預處理(Conn DB), 並在測試完清理(Close DB)，
當有大量的重複操作，最佳實踐是使用Fixture來自動化所有預處理和後處理
Pytest 使用 yield 將Fixture分成兩部分，yield 之前的Code属預處理，會在測試前執行；yield 之後為後處理，將在測試後執行。
使用 -s 阻止消息被吞
"""
import pytest

@pytest.fixture()
def db():
    print('Connection successful')

    yield

    print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'
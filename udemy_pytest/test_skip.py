
# test_skip.py
# s 表示skip跳過
import pytest

@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass

#條件是skip
@pytest.mark.skipif(conn.__version__ < '0.2.0',
                    reason='not supported until v0.2.0')
def test_api():
    pass
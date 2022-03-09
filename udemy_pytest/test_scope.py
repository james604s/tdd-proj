

"""

function: 每個Test Function 都會執行一次Fixture
class: 每個Test Class 執行一次 所有Method都可以使用
module: 每個Module 執行一次 所有Module內的Function跟Method都可以使用
session: 一次測試只執行一次, 所有被找到的函數和方法都可用
"""
import pytest

@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass

# test_scope.py
# pytest --setup-show tests/fixture/test_scope.py::test_multi_scope
def test_multi_scope(sess_scope, mod_scope, func_scope):
    pass

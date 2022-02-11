import pytest

#fixture修饰器来标记固定的工厂函数,在其他函数，模块，类或整个工程调用它时会被激活并优先执行,通常会被用于完成预置处理和重复操作。
@pytest.fixture(autouse=True)
def before():
    print('starting...qqqq')

@pytest.mark.parametrize('a',[1,2,3])
def test_01(a, before):
    print('test01')
    assert a == 1

@pytest.mark.parametrize('b',[2,3])
def test_02(b):
    assert b == 2

@pytest.mark.parametrize('a,b',[(2,3),(4,9)])
def test_03(a, b):
    assert a + b == 5

if __name__ == '__main__':
    pytest.main(['test_funcs.py', '-s']) #运行整个文件下符合的执行的所有函数
    # pytest.main(['test_funcs.py::test_03', '-s']) # 运行指定的函数

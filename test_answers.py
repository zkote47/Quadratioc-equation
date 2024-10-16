from main import equation
import pytest


def test_equation1():
    assert equation(1, 4, 3) == [-1.0, -3.0], 'should be [-1, -3]'


# def test_equation2():
#     assert equation(1, 4, 4) == [-2.0, None], 'should be [-2.0, None]'


# def test_equation3():
#     assert equation(1, 4, 4) == [None, None], 'should be [None, None]'

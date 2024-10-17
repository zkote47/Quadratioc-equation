from main import equation_solver
import pytest

# добавь тесты, чтобы проверялись числа с плавающей точкой как на вход, так и на выход, чтобы разница
# для каждого числа в ответе была не больше 0,001% от проверочного значения. Для этого желательно написать
# отдельную функцию check_accuracy для проверки

# ещё добавь тесты других атомарных функций, например для дискриминанта (и заодно проверь, что он когда надо
# кидает эксепшен). Лучше это вынести в отдельный файл.

# есть даже понятие "покрытие тестами", оно должно стремиться к 100%, то есть в идеале каждая атомарная функция
# помимо интеграционных должна быть протестирована

PERCENT_DELTA = 0.001


def check_accuracy(test_answer: [float, float], real_answer: [float, float]) -> bool:
    test_passed = True  # тут будет какое-то выражение для сравнения, и там как-то будет использоваться PERCENT_DELTA
    # а может и несколько выражений
    return test_passed


def test_discriminant():
    assert True


def test_discriminant_square_root():
    assert True


def test_float1():
    test_answer = equation_solver(1.2, 4.5, 2.8)
    real_answer = [-0.787667637441676, -2.96233236255832]
    assert check_accuracy(test_answer, real_answer)


def test_equation1():
    assert equation_solver(1, 4, 3) == [-1.0, -3.0], 'should be [-1, -3]'


def test_equation2():
    assert equation_solver(1, 4, 4) == [-2.0, None], 'should be [-2.0, None]'


def test_equation3():
    assert equation_solver(1, 4, 5) == [None, None], 'should be [None, None]'

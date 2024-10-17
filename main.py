import math
import matplotlib.pyplot as plt

MY_MAGIC_GLOBAL_CONSTANT = 555


def equation_solver(a, b, c) -> [float, float]:
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    # к методу надо писать описание (выше)

    # тут считается дискриминант и его корректность обрабатывается внутри его функции
    discriminant_value = discriminant(a, b, c)

    # вот так вот это можно было сделать через если-то по предварительно посчитанному дискриминанту при условии
    # его проверки на адекватность (больше нуля)
    if discriminant_value > 0:
        # переписано под приём переменных на вход, а не использование глобальных
        x1 = (-b + discriminant_square_root(discriminant_value)) / 2
        x2 = (-b - discriminant_square_root(discriminant_value)) / 2
        return [x1, x2]
    elif discriminant_value == 0:
        return [-b / 2, None]
    else:
        return [None, None]


# вспомогательные функции не должны быть внутри функции, функция должна делать что-то одно.
# их надо выносить наружу и ставить под функцией, которая их использует, в порядке применения

# 1) По возможности надо писать функции так, чтобы они не зависели от глобальных переменных и вообще сводить к
# минимуму глобальные переменные. В данном случае этой функции нужно, чтобы за её пределами были переменные a, b, c.
# Её лучше переписать, чтобы она принимала их на вход и была так называемой ЧИСТОЙ функцией - погугли, что это.

# 2) Именовать функции надо понятными именами без сокращений
def discriminant_square_root(discriminant_value) -> float:
    '''пыталась сделать через исключение, когда D<0, но тогда в остальных случаях прога не работала'''

    # сначала проверяем, не затупил ли дискриминант, вот тут как раз полезно кинуть эксепшен, если он некорректен
    # предполагается, что будет подан дискриминант больше нуля
    if discriminant_value < 0:
        raise (f"Невозможно найти корень из дискриминанта со значением '{discriminant_value}', "
               f"он не может быть меньше нуля")

    # функция переписана под приём трёх параметров на вход
    return math.sqrt(discriminant_value)


def discriminant(a: float, b: float, c: float) -> [float]:
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    # 1) Описание
    # 2) По возможности надо писать функции так, чтобы они не зависели от глобальных переменных и вообще сводить к
    # минимуму глобальные переменные. В данном случае этой функции нужно, чтобы за её пределами были переменные a, b, c.
    # Её лучше переписать, чтобы она принимала их на вход.
    return b ** 2 - 4 * a * c


# хочешь печатать график - без проблем - создай под это функцию, которая принимает на вход твои коэффициенты,
# а не делай это глобально)
def plot_square_function(a: float, b: float, c: float, lower_range: int, upper_range: int):
    '''

    :param a:
    :param b:
    :param c:
    :param lower_range:
    :param upper_range:
    :return:
    '''
    # Добавила график, почему бы и нет
    # по правилам наименований название локальных переменных - с маленькой буквы. И повторюсь -
    # любые названия должны быть читаемыми и понятными без сокращений. нет задачи сделать покороче, есть
    # задача написать читаемый код

    # старайся, чтобы в функциях не было так называемых "волшебных чисел" (или magic number).
    # если хочется заюзать какое-то число в функции - проверь, может имеет смысл передать его как переменную, либо
    # объявить его глобальной константой большими буквами (привёл пример заглушки)

    kek = MY_MAGIC_GLOBAL_CONSTANT

    # функция делает что-то оно, эта функция печатает, всё остальное - в атомарные функции
    x_axis_array, y_axis_array = square_function_arrays(a, b, c, lower_range, upper_range)

    print(x_axis_array)
    print(y_axis_array)

    plt.plot(x_axis_array, y_axis_array, label='y=x**2')
    plt.legend()
    plt.show()


def square_function_arrays(a: float, b: float, c: float, lower_range: int, upper_range: int) -> ([float], [float]):
    '''
    Формирует массивы квадратичной функции
    :param a:
    :param b:
    :param c:
    :param lower_range:
    :param upper_range:
    :return:
    '''
    x_axis_array = []
    y_axis_array = []
    for x in range(lower_range, upper_range):
        # это тоже стоит вынести в атомарную функцию
        y = square_function(a, b, c, x)
        x_axis_array.append(x)
        y_axis_array.append(y)
    return x_axis_array, y_axis_array


def square_function(a: float, b: float, c: float, x: float) -> float:
    '''
    Считает квадратичную функцию
    :param a:
    :param b:
    :param c:
    :param x:
    :return:
    '''
    return a * (x ** 2) + b * x + c


# хорошим стилем является явное обозначение точки входа для выполнения твоего модуля (типа метода main в плюсах,
# шарпах, да где угодно.

if __name__ == "__main__":
    # print('Введите коэффициенты a, b, c:')
    # я проверяю на примерах (1, 4, 3), (1, 4, 4), (1, 4, 5)
    # input - неудобная практика, лучше сразу цифры
    simple_tests = [[1, 4, 3], [1, 4, 4], [1, 4, 5]]
    answers = []

    for element in simple_tests:
        # equation выводит массив, ты тоже должна выводить массив, а не гонять equation вхолостую)
        answer = equation_solver(element[0], element[1], element[2])
        answers.append(answer)
        print(answer)

    plot_square_function(simple_tests[0][0], simple_tests[0][1], simple_tests[0][2], -10, 11)

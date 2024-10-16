import math
import sys


def equation(a, b, c) -> [float, float]:

    def discriminant() -> [float]:
        return b ** 2 - 4 * a * c

    def sqrt_d() -> [float]:
        if discriminant() < 0:
            print([None, None])
            sys.exit()          #   костыль :(
        else:
            return math.sqrt(discriminant())

        '''пыталась сделать через исключение, когда D<0, но тогда в остальных случаях прога не работала'''
        # try:
        #     raise math.sqrt(discriminant())
        # except ValueError:
        #     print("no roots")
        #     sys.exit()

    x1 = (-b + sqrt_d()) / 2
    x2 = (-b - sqrt_d()) / 2

    answer = [x1, x2]
    if x2 == x1:
        answer[1] = None

    print(answer)


# equation(int(input()), int(input()), int(input()))    # можно тестить на ручном вводе
equation(1, 4, 5)

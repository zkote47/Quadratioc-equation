import math
import sys
import matplotlib.pyplot as plt

print('Введите коэффициенты a, b, c:')

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

# я проверяю на примерах (1, 4, 3) , (1, 4, 4), (1, 4, 5)
a, b, c = int(input()), int(input()), int(input())
equation(a=a, b=b, c=c)

# Добавила график, почему бы и нет
Xs = []
Ys = []
for X in range(-10, 10+1):
    Y = a*(X**2) + b * X + c
    Xs.append(X)
    Ys.append(Y)

print(Xs)
print(Ys)

plt.plot(Xs, Ys, label='y=x**2')
plt.legend()
plt.show()


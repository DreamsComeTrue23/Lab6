import math

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


formula = lambda x, n: ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

def sine_x(x, n):
    x_radian = x * (math.pi / 180)

    current_sum = 0
    for i in range(n):
        current_sum += formula(x_radian, i)

    return current_sum

variable = 0.0

def h_func(n):
    global variable
    if n == 1:
        variable += 1
    else:
        h_func(n - 1)
        variable += 1 / n


        

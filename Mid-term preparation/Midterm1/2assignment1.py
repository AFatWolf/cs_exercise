import math
def quadratic_formula(a, b, c):
    D = b * b - 4 * a * c
    sqrt_D = math.sqrt(D)
    return (-b + sqrt_D)/(2*a), (-b - sqrt_D)/(2*a)
print(quadratic_formula(0, 1, 1))
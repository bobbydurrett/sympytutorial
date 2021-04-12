from sympy import *
import matplotlib.pyplot as plt

def spprint(o):
    pprint(o)
    print(' ')

if __name__ == "__main__":

    init_printing(use_unicode=False)

    x = symbols('x')

    spprint(Integral(cos(x)**2, (x, 0, pi)))


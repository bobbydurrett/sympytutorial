# https://docs.sympy.org/latest/tutorial/calculus.html

from sympy import *
from myprint import spprint

x, y, z = symbols('x y z')
init_printing(use_unicode=False)

# derivatives

spprint(diff(cos(x), x))
spprint(diff(exp(x**2), x))


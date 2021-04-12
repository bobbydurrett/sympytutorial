# https://docs.sympy.org/latest/tutorial/printing.html

from sympy import *

x = symbols('x')

init_printing(use_unicode=False)

pprint(Integral(sqrt(1/x), x))

init_printing(use_unicode=True)

pprint(Integral(sqrt(1/x), x))


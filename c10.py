# https://docs.sympy.org/latest/tutorial/solvers.html

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=False)
from myprint import *

spprint(Eq(x, y))

spprint(solveset(Eq(x**2, 1), x))
spprint(solveset(Eq(x**2 - 1, 0), x))

# assumes equation is x**2 - 1 =0 

spprint(solveset(x**2 - 1, x))

s = solveset(x**2 - 1, x)

print(type(s))

for e in s:
    pprint(e)

spprint(solveset(x**2 - x, x))
spprint(solveset(x - x, x, domain=S.Reals))
spprint(solveset(sin(x) - 1, x, domain=S.Reals))

print(latex(solveset(sin(x) - 1, x, domain=S.Reals)))








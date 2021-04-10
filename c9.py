# https://docs.sympy.org/latest/tutorial/calculus.html

from sympy import *
from myprint import spprint

x, y, z = symbols('x y z')
init_printing(use_unicode=False)

# derivatives

spprint(diff(cos(x), x))
spprint(diff(exp(x**2), x))

# derivative 3 times

spprint(diff(x**4, x, x, x))
spprint(diff(x**4, x, 3))

# many variables?

expr = exp(x*y*z)

spprint(expr)

spprint(diff(expr, x, y, y, z, z, z, z))

spprint(diff(expr, x, y, 2, z, 4))

spprint(diff(expr, x, y, y, z, 4))

# diff method

spprint(expr.diff(x, y, y, z, 4))

# "unevaluated" derivative - interesting

deriv = Derivative(expr, x, y, y, z, 4)
spprint(deriv)

# evaluate with .doit - wonder how that works with other things

spprint(deriv.doit())

# not sure what this is - nth derivative with respect to x?

m, n, a, b = symbols('m n a b')
expr = (a*x + b)**m
spprint(expr.diff((x, n)))



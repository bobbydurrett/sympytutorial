# https://docs.sympy.org/latest/tutorial/calculus.html

from sympy import *
from myprint import spprint, lprint

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

#integrals

# indefinate

spprint(integrate(cos(x), x))

# definate

spprint(integrate(exp(-x), (x, 0, oo)))

# multiple

spprint(integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))

# unable to compute

expr = integrate(x**x, x)
spprint(expr)
spprint(expr.doit())

# unevaluated

expr = Integral(log(x)**2, x)
spprint(expr)
spprint(expr.doit())

# more complex?

integ = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -
        exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
spprint(integ)

spprint(integ.doit())

integ = Integral(sin(x**2), x)
spprint(integ)
spprint(integ.doit())

integ = Integral(x**y*exp(-x), (x, 0, oo))
spprint(integ)
spprint(integ.doit())

# could not lprint this one. Bummer.





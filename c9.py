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

# limits

spprint(limit(sin(x)/x, x, 0))

# things that cannot be done by subs oo/oo = nan

expr = x**2/exp(x)
spprint(expr)
spprint(expr.subs(x, oo))
spprint(limit(expr, x, oo))

# unevaluated

expr = Limit((cos(x) - 1)/x, x, 0)
spprint(expr)
spprint(expr.doit())

# + or - side of limit
# I guess you do not know if x is
# positive or negative
# maybe can say that when defining symbol

spprint(limit(1/x, x, 0, '+'))
spprint(limit(1/x, x, 0, '-'))

# series - not sure about this
# not related to CS big O

expr = exp(sin(x))
spprint(expr.series(x, 0, 4))

spprint(x + x**3 + x**6 + O(x**4))

spprint(x*O(1))

# how do I enter formalas to print and do not get them
# immediately simplified?

spprint(expr.series(x, 0, 4).removeO())

# another thing I do not understand

f, g = symbols('f g', cls=Function)
spprint(differentiate_finite(f(x)*g(x)))

f = Function('f')
dfdx = f(x).diff(x)
spprint(dfdx.as_finite_difference())

f = Function('f')
spprint(f)
spprint(f(x))
d2fdx2 = f(x).diff(x, 2)
spprint(d2fdx2)
h = Symbol('h')
spprint(d2fdx2.as_finite_difference([-3*h,-h,2*h]))

spprint(finite_diff_weights(2, [-3, -1, 2], 0)[-1][-1])

x_list = [-3, 1, 2]
spprint(x_list)

y_list = symbols('a b c')
spprint(y_list)

spprint(apply_finite_diff(1, x_list, y_list, 0))

# way to get 2*x/x without evaluating
# there is no Div apparently

y = Mul(2*x,1/x, evaluate=False)

# unsimplified

spprint(y)

# simplified

spprint(y.doit())

# I guess there is Add, Mul, Pow




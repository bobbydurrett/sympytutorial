from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=False)

pprint(diff(sin(x)*exp(x), x))

pprint(integrate(exp(x)*sin(x) + exp(x)*cos(x), x))

pprint(integrate(sin(x**2), (x, -oo, oo)))

pprint(limit(sin(x)/x, x, 0))

y = Function('y')
pprint(dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))

pprint(Matrix([[1, 2], [2, 2]]).eigenvals())

pprint(besselj(nu, z).rewrite(jn))

print(latex(Integral(cos(x)**2, (x, 0, pi))))

from myprint import lprint

lprint(Integral(cos(x)**2, (x, 0, pi)))




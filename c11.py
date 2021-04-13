# https://docs.sympy.org/latest/tutorial/solvers.html

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=False)
from myprint import *
import myprint

spprint(Eq(x, y))

spprint(solveset(Eq(x**2, 1), x))
spprint(solveset(Eq(x**2 - 1, 0), x))
spprint(solveset(x**2 - 1, x))

spprint(solveset(x**2 - x, x))
spprint(solveset(x - x, x, domain=S.Reals))
spprint(solveset(sin(x) - 1, x, domain=S.Reals))

spprint(solveset(exp(x), x))     # No solution exists
spprint(solveset(cos(x) - x, x))  # Not able to find solution


spprint(linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z)))
spprint(linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z)))

M = Matrix(((1, 1, 1, 1), (1, 1, 2, 3)))
system = A, b = M[:, :-1], M[:, -1]
spprint(linsolve(system, x, y, z))

a, b, c, d = symbols('a, b, c, d', real=True)
spprint(nonlinsolve([a**2 + a, a - b], [a, b]))
spprint(nonlinsolve([x*y - 1, x - 2], x, y))
spprint(nonlinsolve([x**2 + 1, y**2 + 1], [x, y]))

from sympy import sqrt
system = [x**2 - 2*y**2 -2, x*y - 2]
vars = [x, y]
spprint(nonlinsolve(system, vars))

system = [exp(x) - sin(y), 1/y - 3]
spprint(nonlinsolve(system, vars))

spprint(nonlinsolve([x*y, x*y - x], [x, y]))

system = [a**2 + a*c, a - b]
spprint(nonlinsolve(system, [a, b]))

spprint(solve([x**2 - y**2/exp(x)], [x, y], dict=True))

spprint(solve([sin(x + y), cos(x - y)], [x, y]))

spprint(solveset(x**3 - 6*x**2 + 9*x, x))

spprint(roots(x**3 - 6*x**2 + 9*x, x))

spprint(solve(x*exp(x) - 1, x ))

# diff eq

f, g = symbols('f g', cls=Function)

spprint(f(x))

spprint(f(x).diff(x))

diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))

spprint(diffeq)

spprint(dsolve(diffeq, f(x)))

spprint(dsolve(f(x).diff(x)*(1 - sin(f(x))) - 1, f(x)))

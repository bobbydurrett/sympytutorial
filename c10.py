from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=False)
from myprint import *
import myprint

myprint.tex_file = "c10.tex"

startl()

addlt("https://docs.sympy.org/latest/tutorial/solvers.html")

addlm(Eq(x, y))

addlm(solveset(Eq(x**2, 1), x))
addlm(solveset(Eq(x**2 - 1, 0), x))

addlt("assumes equation is x**2 - 1 =0")

addlm(solveset(x**2 - 1, x))

s = solveset(x**2 - 1, x)

addlt(str(type(s)))

for e in s:
    addlm(e)

addlm(solveset(x**2 - x, x))
addlm(solveset(x - x, x, domain=S.Reals))
addlm(solveset(sin(x) - 1, x, domain=S.Reals))

endl()




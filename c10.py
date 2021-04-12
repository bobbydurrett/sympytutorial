from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=False)
from myprint import *

startl("c10.tex")

addlt("c10.tex","https://docs.sympy.org/latest/tutorial/solvers.html")

addlm("c10.tex",Eq(x, y))

addlm("c10.tex",solveset(Eq(x**2, 1), x))
addlm("c10.tex",solveset(Eq(x**2 - 1, 0), x))

addlt("c10.tex","assumes equation is x**2 - 1 =0")

addlm("c10.tex",solveset(x**2 - 1, x))

s = solveset(x**2 - 1, x)

addlt("c10.tex",str(type(s)))

for e in s:
    addlm("c10.tex",e)

addlm("c10.tex",solveset(x**2 - x, x))
addlm("c10.tex",solveset(x - x, x, domain=S.Reals))
addlm("c10.tex",solveset(sin(x) - 1, x, domain=S.Reals))

endl("c10.tex")




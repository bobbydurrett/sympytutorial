# print c13 latex examples

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=False)
from myprint import *
import myprint

myprint.tex_file = "c13latex.tex"

startl()

addlt("https://docs.sympy.org/latest/tutorial/manipulation.html")

# latex

from sympy import latex

uexpr = UnevaluatedExpr(S.One*5/7)*UnevaluatedExpr(S.One*3/4)

addlm(uexpr)

addlm(uexpr.doit())

endl()








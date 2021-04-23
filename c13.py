# https://docs.sympy.org/latest/tutorial/manipulation.html

from sympy import *
init_printing(use_unicode=False)
from myprint import spprint

x, y, z = symbols('x y z')

expr = x**2 + x*y
print(srepr(expr))


x = symbols('x')
print(srepr(x))
x = Symbol('x')
print(srepr(x))

print(srepr(x**2))
print(' ')

spprint(Pow(x, 2))


print(type(2))

print(type(sympify(2)))

print(srepr(x*y))
print(' ')

spprint(Mul(x, y))

spprint(Add(Pow(x, 2), Mul(x, y)))


expr = sin(x*y)/2 - x**2 + 1/y

spprint(expr)

print(srepr(expr))

# no subtraction (very weird)

print(srepr(x - y))

# no division (ditto)

expr = x/y
spprint(expr)
print(srepr(expr))

# rational number

expr = sin(x*y)/2
spprint(expr)
print(srepr(expr))

# order

spprint(1 + x)

# func

expr = Add(x, x)

print(expr.func)

spprint(expr)

print(Integer(2).func)
print(Integer(0).func)
print(Integer(-1).func)

print(isinstance(Integer(2),Integer))
print(isinstance(Integer(0),Integer))
print(isinstance(Integer(-1),Integer))

# args

expr = 3*y**2*x
print(expr.func)
print(expr.args)

# reconstruct from func and args

spprint(expr.func(*expr.args))

print(expr == expr.func(*expr.args))

# args are sorted

expr = y**2*3*x

spprint(expr)
print(expr.args)

# can index

print(' ')
spprint(expr.args[2])

print(expr.args[2].args)

print(y.args)

print(Integer(2).args)

print(type(Integer(2).args))

def pre(expr):
    print(expr)
    for arg in expr.args:
        pre(arg)

expr = x*y + 1

spprint(expr)

pre(expr)

# built in

for arg in preorder_traversal(expr):
    print(arg)


from sympy import Add
from sympy.abc import x, y, z

spprint(x + x)

spprint(Add(x, x))

spprint(Add(x, x, evaluate=False))

from sympy import sympify

spprint(sympify("x + x", evaluate=False))

# evaluate False doesnt prevent later evaluation 

expr = Add(x, x, evaluate=False)

spprint(expr)

spprint(expr + x)

# unevaluated expression

from sympy import UnevaluatedExpr
expr = x + UnevaluatedExpr(x)

spprint(expr)

spprint(x + expr)

# doit forces evaluation

spprint((x + expr).doit())

#other

from sympy import *
from sympy.abc import x, y, z
uexpr = UnevaluatedExpr(S.One*5/7)*UnevaluatedExpr(S.One*3/4)

spprint(uexpr)

spprint(x*UnevaluatedExpr(1/x))

# x + x gets evaluated before being passed to
# UnevaluatedExpr

expr1 = UnevaluatedExpr(x + x)

spprint(expr1)

# but 'x + x' is just a string
# so it is not evaluated before sympify gets it

expr2 = sympify('x + x', evaluate=False)

spprint(expr2)

# sympify keeps x + x from being evaluated on way in
# UnevaluatedExpr keeps x + x from being evaluated when adding y

spprint(UnevaluatedExpr(sympify("x + x", evaluate=False)) + y)

# latex

from sympy import latex

uexpr = UnevaluatedExpr(S.One*5/7)*UnevaluatedExpr(S.One*3/4)

print(latex(uexpr))

print(latex(uexpr.doit()))







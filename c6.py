# https://docs.sympy.org/latest/tutorial/basic_operations.html

from sympy import *
x, y, z = symbols("x y z")

expr = cos(x) + 1
print(expr)
print(expr.subs(x, y))

print(expr.subs(x, 0))

expr = x**y
print(expr)
expr = expr.subs(y, x**y)
print(expr)
expr = expr.subs(y, x**x)
print(expr)

expr = sin(2*x) + cos(2*x)
print(expr)
print(type(expr))
print(expand_trig(expr))
print(expr.subs(sin(2*x), 2*sin(x)*cos(x)))

# "SymPy expressions are immutable"

expr = cos(x)
print(expr)
print(expr.subs(x, 0))
print(expr)
print(x)

expr = x**3 + 4*x*y - z
print(expr)
print(expr.subs([(x, 2), (y, 4), (z, 0)]))

expr = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
print(expr)
replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
print(replacements)
print(expr.subs(replacements))

# why not just do a simple loop?

replacements=[]

for i in range(5):
    if i % 2 == 0:
        replacements.append((x**i, y**i))
        
print(replacements)
print(expr.subs(replacements))
       
str_expr = "x**2 + 3*x - 1/2"
print(type(str_expr))
print(str_expr)
expr = sympify(str_expr)
print(type(expr))
print(expr)
print(expr.subs(x, 2))

expr = sqrt(8)
print(expr)
print(expr.evalf())

# substitute variable for number and
# evaluate to float

expr = cos(2*x)
print(expr)
print(expr.evalf(subs={x: 2.4}))

import numpy 
a = numpy.arange(10) 
expr = sin(x)
print(expr)
f = lambdify(x, expr, "numpy") 
print(f(a))
print(type(f))

f = lambdify(x, expr, "math")
print(f(0.1))

def mysin(x):
    """
    My sine. Note that this is only accurate for small x.
    """
    return x
    
f = lambdify(x, expr, {"sin":mysin})
print(f(0.1))




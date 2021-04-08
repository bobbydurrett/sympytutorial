from sympy import symbols,expand,factor
x, y = symbols('x y')
expr = x + 2*y
print(expr)
print(expr + 1)
print(expr - x)
print(x*expr)

expanded_expr = expand(x*expr)
print(expanded_expr)
print(factor(expanded_expr))



from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=False)

# simplify - not specific type of simplification

pprint(simplify(sin(x)**2 + cos(x)**2))

pprint(simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

pprint(simplify(gamma(x)/gamma(x - 2)))

pprint(simplify(x**2 + 2*x + 1))

# expand - expand polynomial to canonical form ax^2+bx+c etc.

pprint(expand((x + 1)**2))

pprint(expand((x + 2)*(x - 3)))

pprint(expand((x + 1)*(x - 2) - (x - 1)*x))

# factor - factors a polynomial

pprint(factor(x**3 - x**2 + x - 1))

pprint(factor(x**2*z + 4*x*y*z + 4*y**2*z))

# returns list of factors

pprint(factor_list(x**2*z + 4*x*y*z + 4*y**2*z))

# non-polynomials

pprint(expand((cos(x) + sin(x))**2))

pprint(factor(cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2))

# collect - based on a variable (i.e. x)
# gather the coefficients into a term
# multiplied by a power of x.

expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
pprint(expr)

collected_expr = collect(expr, x)
pprint(collected_expr)

# coeff gives coefficient of the given
# power of x - x^2 in this example

pprint(collected_expr.coeff(x, 2))

# cancel - arrange as fraction?

pprint(cancel((x**2 + 2*x + 1)/(x**2 + x)))

expr = 1/x + (3*x/2 - 2)/(x - 4)
pprint(expr)

pprint(cancel(expr))

expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
pprint(expr)

pprint(cancel(expr))

# factors numerator in this example

pprint(factor(expr))

# apart - seems to split into multiple fractional terms
# opposite of cancel kind of?

expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)

pprint(expr)
print(' ')

pprint(apart(expr))
print(' ')

pprint(cancel(apart(expr)))
print(' ')

# trig simp - like simplify for general
# there are specific simps later

pprint(acos(x))
print(' ')
pprint(cos(acos(x)))
print(' ')
pprint(asin(1))
print(' ')

pprint(trigsimp(sin(x)**2 + cos(x)**2))
print(' ')
pprint(trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4))
print(' ')
pprint(trigsimp(sin(x)*tan(x)/sec(x)))
print(' ')

pprint(trigsimp(cosh(x)**2 + sinh(x)**2))
print(' ')
pprint(trigsimp(sinh(x)/tanh(x)))
print(' ')

# expand_trig kind of like expand

def spprint(o):
    pprint(o)
    print(' ')

spprint(expand_trig(sin(x + y)))
spprint(expand_trig(tan(2*x)))

# trigsimp opposite of expand_trig kinda

spprint(trigsimp(expand_trig(sin(x + y))))

# powers - can state things about the numbers
# real, positive, or by default complex

x, y = symbols('x y', positive=True)
a, b = symbols('a b', real=True)
z, t, c = symbols('z t c')

spprint(powsimp(x**a*x**b))

spprint(powsimp(x**a*y**a))

# z, t, c might be complex

spprint(powsimp(t**c*z**c))

# force simp

spprint(powsimp(t**c*z**c, force=True))

spprint((z*t)**2)

spprint(sqrt(x*y))

# simp doesn't work because of automatic splitting

spprint(powsimp(z**2*t**2))
spprint(powsimp(sqrt(x)*sqrt(y)))

# expanding the base or exponent

spprint(expand_power_exp(x**(a + b)))

spprint(expand_power_base((x*y)**a))

# same doesn't work with complex but can force

spprint(expand_power_base((z*t)**c))

spprint(expand_power_base((z*t)**c, force=True))

# doesn't work with number powers like above

spprint(x**2*x**3)
spprint(expand_power_exp(x**5))

# simplified nested powers 
# can force when not appropriate

spprint(powdenest((x**a)**b))
spprint(powdenest((z**a)**b))
spprint(powdenest((z**a)**b, force=True))

# exponentials and logs

# log(x) = ln(x) log base 2 of x I think

spprint(ln(x))

x, y = symbols('x y', positive=True)
n = symbols('n', real=True)

spprint(expand_log(log(x*y)))
spprint(expand_log(log(x/y)))
spprint(expand_log(log(x**2)))
spprint(expand_log(log(x**n)))
spprint(expand_log(log(z*t)))


# force

spprint(expand_log(log(z**2)))
spprint(expand_log(log(z**2), force=True))

# logcombine kind of revers of expand_log

spprint(logcombine(log(x) + log(y)))
spprint(logcombine(n*log(x)))
spprint(logcombine(n*log(z)))
spprint(logcombine(n*log(z), force=True))


# "special" functions

x, y, z = symbols('x y z')
k, m, n = symbols('k m n')

spprint(factorial(n))

spprint(binomial(n, k))

spprint(binomial(5, 2))

spprint(gamma(z))

spprint(hyper([1, 2], [3], z))

# rewrite an expression in terms of a function

spprint(tan(x).rewrite(sin))
spprint(factorial(x).rewrite(gamma))

# get rid of hyper

spprint(hyperexpand(hyper([1, 1], [2], z)))

expr = meijerg([[1],[1]], [[1],[]], -z)
spprint(expr)
spprint(hyperexpand(expr))

# simplifiy combinatorials - binomial, etc.

n, k = symbols('n k', integer = True)
spprint(combsimp(factorial(n)/factorial(n - 3)))
spprint(combsimp(binomial(n+1, k+1)/binomial(n, k)))

# simplify gamma whatever that is. :)

spprint(gammasimp(gamma(x)*gamma(1 - x)))

# continued fraction example
# i think this is an example of using sympy and simplification

def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1/expr
    return l[0] + expr
    
spprint(list_to_frac([x, y, z]))

# result is sympy fraction

spprint(list_to_frac([1, 2, 3, 4]))

# get continued fraction

syms = symbols('a0:5')
spprint(syms)
a0, a1, a2, a3, a4 = syms
frac = list_to_frac(syms)
spprint(frac)

# put into standard form

frac = cancel(frac)
spprint(frac)

# put back into original form

l = []
frac = apart(frac, a0)
spprint(frac)
l.append(a0)
frac = 1/(frac - a0)
spprint(frac)

frac = apart(frac, a1)
spprint(frac)
l.append(a1)
frac = 1/(frac - a1)
frac = apart(frac, a2)
spprint(frac)
l.append(a2)
frac = 1/(frac - a2)
frac = apart(frac, a3)
spprint(frac)
l.append(a3)
frac = 1/(frac - a3)
frac = apart(frac, a4)
spprint(frac)
l.append(a4)
spprint(list_to_frac(l))





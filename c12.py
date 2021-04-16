# https://docs.sympy.org/latest/tutorial/matrices.html

from sympy import *
init_printing(use_unicode=False)
from myprint import spprint

spprint(Matrix([[1, -1], [3, 4], [0, 2]]))

spprint(Matrix([1, 2, 3]))

M = Matrix([[1, 2, 3], [3, 2, 1]])
N = Matrix([0, 1, 1])

spprint(M)
spprint(N)
spprint(M*N)

# shape

M = Matrix([[1, 2, 3], [-2, 0, 4]])
spprint(M)

# cannot find shape
#spprint(shape(M))

# rows and columns

spprint(M.row(0))
spprint(M.col(-1))

M.col_del(0)
spprint(M)

M.row_del(1)
spprint(M)

M = M.row_insert(1, Matrix([[0, 4]]))
spprint(M)

M = M.col_insert(0, Matrix([1, -2]))
spprint(M)

# math et al

M = Matrix([[1, 3], [-2, 3]])
N = Matrix([[0, 3], [0, 7]])
spprint(M + N)
spprint(M*N)
spprint(3*M)
spprint(M**2)
spprint(M**-1)

# this gets error:
# sympy.matrices.common.NonInvertibleMatrixError: Matrix det == 0; not invertible.
#spprint(N**-1)

# transpose

M = Matrix([[1, 2, 3], [4, 5, 6]])
spprint(M)

spprint(M.T)

# constructors

spprint(eye(3))

spprint(eye(4))

spprint(zeros(2, 3))

spprint(ones(3, 2))

spprint(diag(1, 2, 3))

spprint(diag(-1, ones(2, 2), Matrix([5, 7, 5])))

# advanced

M = Matrix([[1, 0, 1], [2, -1, 3], [4, 3, 2]])
spprint(M)

spprint(M.det())

M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
spprint(M)

spprint(M.rref())

M = Matrix([[1, 2, 3, 0, 0], [4, 10, 0, 0, 1]])

spprint(M)

spprint(M.nullspace())

M = Matrix([[1, 1, 2], [2 ,1 , 3], [3 , 1, 4]])

spprint(M)

spprint(M.columnspace())

M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])

spprint(M)

spprint(M.eigenvals())

spprint(M.eigenvects())

# diagonalize

spprint(M)

P, D = M.diagonalize()

spprint(P)

spprint(D)

spprint(P*D*P**-1)

print(P*D*P**-1 == M)

lamda = symbols('lamda')

p = M.charpoly(lamda)

spprint(p)

spprint(factor(p.as_expr()))

# zero testing

from sympy import *
q = Symbol("q", positive = True)
m = Matrix([
[-2*cosh(q/3),      exp(-q),            1],
[      exp(q), -2*cosh(q/3),            1],
[           1,            1, -2*cosh(q/3)]])

spprint(m.nullspace())


import warnings
def my_iszero(x):
    try:
        result = x.is_zero
    except AttributeError:
        result = None

    # Warnings if evaluated into None
    if result is None:
        warnings.warn("Zero testing of {} evaluated into None".format(x))
    return result

spprint(m.nullspace(iszerofunc=my_iszero))

def my_iszero(x):
    try:
        result = x.rewrite(exp).simplify().is_zero
    except AttributeError:
        result = None

    # Warnings if evaluated into None
    if result is None:
        warnings.warn("Zero testing of {} evaluated into None".format(x))
    return result

spprint(m.nullspace(iszerofunc=my_iszero))




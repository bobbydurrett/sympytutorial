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







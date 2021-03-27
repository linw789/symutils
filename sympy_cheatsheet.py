from sympy import *
from symutils import *

init_printing()

# Print equations
A = Matrix([
    [1, 1, 2, 2, 1],
    [2, 2, 1, 1, 1],
    [3, 3, 3, 3, 2],
    [1, 1, -1, -1, 0]
])
pprint(Eq(S('A'), A, evaluate=False))

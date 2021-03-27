from sympy import Matrix, symbols, eye

def gen_symbols_1d(elem, num):
    """
    Generate a sequence of symbols that have the same literal string with an
    incrementally bigger number as subscript. The subscript starts from 1.

    elem: str
        The symbol string.
    num: int
        The maximum subscript number.
    """
    symbs = []
    for i in range(1, num + 1):
        symbs.append(symbols(elem + str(i)))
    return symbs

def gen_mat(elem, row_num, col_num):
    """
    Generate a matrix, each element of which is represented by the same literal 
    string with a 2-digit number subscript. The first digit represents the row 
    number, the second column number.

    elem: str
        The element symbol string.
    row_num: int
        The number of rows of the matrix to be generated.
    col_num: int
        The number of columns of the matrix to be generated.
    """
    rows = []
    for r in range(1, row_num + 1):
        row = []
        for c in range(1, col_num + 1):
            row.append(symbols(elem + str(r) + str(c)))
        rows.append(row)
    return Matrix(rows)

def elementary_matrix_swapping(dim, row_a, row_b):
    """
    Generate an elementary matrix that swaps the rows of the matrix it's right 
    multiplied with.

    dim: int
        The dimension of the resulting square matrix.
    row_a: int
        One of the rows to be swapped.
    row_b: int
        One of the rows to be swapped.
    """
    assert row_a >= 0 and row_a < dim, "row number out of bound"
    assert row_b >= 0 and row_b < dim, "row number out of bound"
    e = eye(dim)
    e[row_a, row_a] = 0
    e[row_b, row_b] = 0
    e[row_a, row_b] = 1
    e[row_b, row_a] = 1

    return e

def elementary_matrix_multiplication(dim, row_n, c):
    """
    Generate an elementary matrix that multiplies one of a matrix's row by a
    constant.

    dim: int
        The dimension of the resulting square matrix.
    row_n: int
        The row to be modified.
    c: int
        The constant to multiply the row with.
    """
    assert row_n >= 0 and row_n < dim, "row number out of bound"
    e = eye(dim)
    e[row_n, row_n] = c

    return e;

def elementary_matrix_addition(dim, row_a, row_b, c):
    """
    Generate an elementary matrix that adds to a row of a matrix some multiples 
    of another row.

    dim: int
        The dimension of the resulting square matrix.
    row_a: int
        The row to be modified.
    row_b: int
        The row to be multiplied with a constant and added to another row.
    c: int
        The constant.
    """
    assert row_a >= 0 and row_a < dim, "row number out of bound"
    assert row_b >= 0 and row_b < dim, "row number out of bound"
    e = eye(dim)
    e[row_a, row_b] = c

    return e


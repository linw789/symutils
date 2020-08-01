from sympy import Matrix, symbols

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

#!/usr/bin/python3
"""
2-matrix_divided module.

Provides a function matrix_divided(matrix, div) which returns
 a new matrix with all elements divided by div, rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list of list of int/float): input matrix.
        div (int/float): divisor.

    Raises:
        TypeError: if matrix is not a matrix (list of lists of
                   integers/floats).
        TypeError: if rows of the matrix are not the same size.
        TypeError: if div is not an int or float.
        ZeroDivisionError: if div is 0.

    Returns:
        list of list of floats: new matrix.
    """
    # Validate matrix
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(elem / div, 2) for elem in row])

    return new_matrix

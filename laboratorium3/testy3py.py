import numpy
import pytest

licznik = 1
counter = 1

def creating_matrix(rows, columns):
    global matrix_2_before
    global matrix_1_before
    global counter
    matrix = numpy.empty((rows,columns))
    
    for z in range(0, columns):
        for g in range(0, rows):
            print(f"Podaj element {g+1} x {z+1} macierzy")
            matrix[g][z] = int(input())

    matrix = cutting_matrix(matrix, rows, columns)
    if counter == 1:
        matrix_1_before = matrix
    elif counter == 2:
        matrix_2_before = matrix
    if rows > columns:
        matrix = det_times_matrix(matrix, columns, columns)
    elif columns >= rows:
        matrix = det_times_matrix(matrix, rows, rows)
    counter = counter + 1
    return matrix

def det_matrix(matrix):
    return numpy.linalg.det(matrix)

def det_times_matrix(matrix, rows, columns):
    final_matrix = numpy.empty((rows, columns))
    det = det_matrix(matrix)
    for z in range(0, rows):
        for g in range(0, columns):
            final_matrix[z][g] = matrix[z][g] * det
    return final_matrix

def matrix_multiplication(rows_1, rows_2, columns_2, matrix1, matrix2):
    final_matrix = numpy.empty((rows_1, columns_2))
    for z in range(0, rows_1):
        for g in range(0, columns_2):
            value = 0
            for c in range(0, rows_2):
                value = value + (matrix1[z][c] * matrix2[c][g])
            final_matrix[z][g] = value
    return final_matrix

def cutting_matrix(matrix, rows, columns):
    global licznik
    global columns_n_1
    global columns_n_2
    global rows_m_1
    global rows_m_2

    if rows > columns:
        final_matrix = numpy.empty((columns, columns))
        if licznik == 1:
            rows_m_1 = columns_n_1
        elif licznik == 2:
            rows_m_2 = columns_n_2
        for z in range(0, columns):
            for g in range(0, columns):
                final_matrix[z][g] = matrix[z][g]
    elif columns > rows:
        final_matrix = numpy.empty((rows, rows))
        if licznik == 1:
            columns_n_1 = rows_m_1
        elif licznik == 2:
            columns_n_2 = rows_m_2
        for z in range(0, rows):
            for g in range(0, rows):
                final_matrix[z][g] = matrix[z][g]
    else:
        final_matrix = matrix
    licznik = licznik + 1
    return final_matrix

# Pytest Test Cases

def test_multiplication():
    assert numpy.array_equal(matrix_multiplication(2, 2, 2, [[2, 2], [2, 2]], [[2, 2], [2, 2]]), [[8, 8], [8, 8]])

def test_multiplication2():
    assert numpy.array_equal(matrix_multiplication(3, 3, 3, [[2, 2, 2], [2, 2, 2], [2, 2, 2]],[[2, 2, 2], [2, 2, 2], [2, 2, 2]]), [[12, 12, 12], [12, 12, 12], [12, 12, 12]])

def test_raise_det():
    with pytest.raises(numpy.linalg.LinAlgError):
        det_matrix([2, 2])

def test_det():
    assert det_matrix([[2, 0], [0, 2]]) == 4

def test_det1():
    assert det_matrix([[4, 0, 0], [0, 4, 0], [0, 0, 4]]) == 64
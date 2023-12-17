import numpy
import unittest

licznik = 1
counter = 1

def creating_matrix(rows, columns):
    global matrix_2_before
    global matrix_1_before
    global counter
    matrix = numpy.empty((rows,columns)) #funkcja numpy tworzaca macierz m x n za pomoca zagniezdzenia tablic
    
    for z in range(0,columns):
        
        for g in range(0,rows):
            
            print("Podaj element %d" %(g+1), "x %d macierzy" %(z+1))
            
            matrix[g][z] = int(input())

    matrix = cutting_matrix(matrix, rows, columns)
    if (counter == 1):
        matrix_1_before = matrix
    elif (counter == 2):
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
    for z in range(0,rows):
        for g in range(0, columns):
            final_matrix[z][g] = matrix[z][g] * det


    return final_matrix



#https://imgur.com/a/dIP958c 
def matrix_multiplication(rows_1, rows_2, columns_2, matrix1, matrix2): #opcjonalnie zamiast rows_2 moze byc columns_1    
    final_matrix = numpy.empty((rows_1,columns_2))
    for z in range(0,rows_1):
        for g in range(0,columns_2):
            value = 0
            for c in range(0,rows_2): #moze byc columns 1
                value = value + (matrix1[z][c]*matrix2[c][g])
            final_matrix[z][g] = value

    return final_matrix

def cutting_matrix(matrix, rows, columns):
    global licznik
    global columns_n_1
    global columns_n_2
    global rows_m_1
    global rows_m_2

    if (rows>columns):
        
        final_matrix = numpy.empty((columns, columns))
        
        
        
        if (licznik == 1):
            rows_m_1 = columns_n_1
        elif (licznik == 2):
            rows_m_2 = columns_n_2
        
        for z in range(0,columns):
            for g in range(0,columns):
                final_matrix[z][g] = matrix[z][g]
        
    elif (columns>rows):
        
        final_matrix = numpy.empty((rows, rows))
        
        
        
        if (licznik == 1):
            columns_n_1 = rows_m_1
        elif (licznik == 2):
            columns_n_2 = rows_m_2

        for z in range(0,rows):
            for g in range(0,rows):
                final_matrix[z][g] = matrix[z][g]
    else:
        final_matrix = matrix #bez tego nie dziala???
    licznik = licznik + 1
                
    return final_matrix

print("Podaj wymiar pierwszej macierzy m x n")

rows_m_1 = int(input("m: "))
columns_n_1 = int(input("n: "))
matrix_1_before = numpy.empty((rows_m_1,columns_n_1))
matrix_1 = creating_matrix(rows_m_1, columns_n_1)

print("Podaj wymiar drugiej macierzy m x n")

rows_m_2 = int(input("m: "))
columns_n_2 = int(input("n: "))



matrix_2_before = numpy.empty((rows_m_2,columns_n_1))
matrix_2 = creating_matrix(rows_m_2, columns_n_2)





if (rows_m_2 == columns_n_1):
    print("Mnozymy dwie macierze ze soba kazda z nich pomnozona przez sume ich wyznacznikow")
    print("")
    print("Pierwsza macierz i jej Det:", det_matrix(matrix_1_before) )
    print(matrix_1)
    print("") 
    print("Druga macierz", det_matrix(matrix_2_before))
    print(matrix_2)
    print("")
    print("Wynik:")
    print(matrix_multiplication(rows_m_1, rows_m_2, columns_n_2, matrix_1, matrix_2))
    


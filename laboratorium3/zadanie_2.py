import numpy
print("Podaj wymiar pierwszej macierzy m x n")

rows_m_1 = int(input("m: "))
columns_n_1 = int(input("n: "))

def creating_matrix(rows, columns):
    
    matrix = numpy.empty((rows,columns)) #funkcja numpy tworzaca macierz m x n za pomoca zagniezdzenia tablic
    
    for z in range(0,columns):
        
        for g in range(0,rows):
            
            print("Podaj element %d" %(g+1), "x %d macierzy" %(z+1))
            
            matrix[g][z] = int(input())


    return matrix

def det_matrix(matrix):
    return numpy.linalg.det(matrix)
    
def det_times_matrix(matrix, rows, columns):
    final_matrix = numpy.empty(rows, columns)
    det = det_matrix(matrix)
    for z in range(0,rows):
        for g in range(0, columns):
            matrix[z][g] = matrix[z][g] * det


    return final_matrix


def matrix_multiplication(rows_1, rows_2, columns_2, matrix1, matrix2): #opcjonalnie zamiast rows_2 moze byc columns_1
    final_matrix = numpy.empty((rows_1,columns_2))
    
    
    for z in range(0,rows_1):
        for g in range(0,columns_2):
                for c in range(0,rows_2): #moze byc columns 1
                    value = value + (matrix1[z][c]*matrix2[c][g])
                final_matrix[z][g] = value


    
    
    
    return final_matrix



matrix_1 = creating_matrix(rows_m_1, columns_n_1)
print("Podaj wymiar drugiej macierzy m x n")

rows_m_2 = int(input("m: "))
columns_n_2 = int(input("n: "))
matrix_2 = creating_matrix(rows_m_2, columns_n_2)

#if (rows_m_1 == columns_n_2 and rows_m_2 == columns_n_1):

    
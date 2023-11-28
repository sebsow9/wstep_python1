import random
import matplotlib.pyplot

print("Podaj rozmiary tablicy N x M x O: ")

N = int(input("N: "))
M = int(input("M: "))
O = int(input("O: "))

def creating_matrix(x, y, z):
    return [[[random.randint(1,10000) for _ in range(x)] for _ in range(y)] for _ in range(z)]

matrix = str(creating_matrix(N, M, O))


with open('example.txt', 'w' ) as file: 
    file.write(matrix)

with open('example.txt', 'r') as file:
    content = file.read()


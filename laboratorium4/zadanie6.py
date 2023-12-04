import random
import numpy as np

print("Podaj rozmiary tablicy N x M x O: ")

N = int(input("N: "))
M = int(input("M: "))
O = int(input("O: "))

def creating_matrix(x, y, z):
    return [[[random.randint(1,10000) for _ in range(x)] for _ in range(y)] for _ in range(z)]

matrix = str(creating_matrix(N, M, O))


with open('example.txt', 'w' ) as file: 
    file.write(matrix)

import matplotlib.pyplot as plt


with open('example.txt', 'r') as file:
    content = eval(file.read())


flat_data = [item for sublist1 in content for sublist2 in sublist1 for item in sublist2 ]

bin_edges = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

plt.hist(flat_data, bins=bin_edges, color='g', edgecolor='black', linewidth=1.3)
plt.title('Histogram of Data')
plt.xticks(range(0, 10001, 1000))
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

hist, _ = np.histogram(flat_data, bins=bin_edges)


for i, count in enumerate(hist):
    bin_range = f"[{bin_edges[i]}-{bin_edges[i+1]}]"
    bars = "=" * count
    print(f"{bin_range.ljust(12)} {bars}")




import numpy as np
import pytest
from zadanie6 import creating_matrix  

def test_content():
    N, M, O = 3, 4, 5  
    matrix = creating_matrix(N, M, O)
    with open('example.txt', 'w') as file:
        file.write(str(matrix))

    with open('example.txt', 'r') as file:
        content = eval(file.read())
    
    assert matrix == content

def test_content1():
    N, M, O = 3, 4, 5  
    result = creating_matrix(N, M, O)
    with open('example1.txt', 'w') as file:
        file.write(str(result))

    with open('example1.txt', 'r') as file:
        content = file.read()

    assert content == str(result)

def test_histogram():
    N, M, O = 3, 4, 5 
    matrix = creating_matrix(N, M, O)
    flat_data = [item for sublist1 in matrix for sublist2 in sublist1 for item in sublist2]
    bin_edges = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    
    hist, _ = np.histogram(flat_data, bins=bin_edges)
    assert len(hist) == len(bin_edges) - 1

def test_creating():
    with pytest.raises(TypeError):
        creating_matrix()

def test_type():
    N, M, O = 3, 4, 5  
    result = creating_matrix(N, M, O)
    assert isinstance(result, list)
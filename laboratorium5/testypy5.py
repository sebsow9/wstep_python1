from zadanie2klasy import Chessboard
import pytest

 
@pytest.fixture
def chessboard2():
    return Chessboard(2)

def test_queens(chessboard2):
    assert chessboard2.N_queens == len(chessboard2.table_of_positions)

def test_checking_row(chessboard2):
    chessboard2.row_table = [1, 1]
    chessboard2.column_table = [1, 2]
    assert chessboard2.row_column() is True

def test_checking_column(chessboard2):
    chessboard2.row_table = [2, 1]
    chessboard2.column_table = [1, 2]
    assert chessboard2.row_column() is not True

def test_checking_row2(chessboard2):
    chessboard2.row_table = [2, 1]
    chessboard2.column_table = [1, 2]
    assert chessboard2.row_column() is not True

def test_checking_diagonal(chessboard2):
    chessboard2.table_of_positions = [(1, 1), (66, 66)]
    assert chessboard2.diagonal() is True

def test_checking_diagonal2(chessboard2):
    chessboard2.table_of_positions = [(1, 1), (25, 66)]
    assert chessboard2.diagonal() is not True
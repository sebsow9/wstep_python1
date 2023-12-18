import pytest
import math

liczby = [0, 1, 2, 3]

def equation(epsilon, liczby):
    
    for z in range(liczby[0], liczby[3]):
            wynik = liczby[z]*liczby[z] - 2
            if (wynik < 0):
                szukana_dolna = float(liczby[z])
            elif (wynik > 0):
                szukana_gorna = float(liczby[z])

    srodek = float(szukana_dolna + szukana_gorna)/2
    wynik_rownania = float(srodek*srodek) - 2
    while (abs(wynik_rownania) > epsilon):
        srodek = float(szukana_dolna + szukana_gorna)/2
        wynik_rownania = float(srodek*srodek) - 2
        if (wynik_rownania < 0):
            szukana_dolna = srodek
        else:
            szukana_gorna = srodek
    return srodek

def test_equation1():
    result = pow(2, 1/2)
    epsilon = 0.1
    liczby = [0, 1, 2, 3]
    assert math.isclose(result, equation(epsilon, liczby), abs_tol=epsilon)

def test_equation2():
    result = pow(2, 1/2)
    epsilon = 0.001
    liczby = [0, 1, 2, 3]
    assert math.isclose(result, equation(epsilon, liczby), abs_tol=epsilon)

def test_equation3():
    result = pow(2, 1/2)
    epsilon = 0.00001
    liczby = [0, 1, 2, 3]
    assert math.isclose(result, equation(epsilon, liczby), abs_tol=epsilon)

def test_raise():
    epsilon = 0.001
    liczby = [0, 1, 2, 3] #zeby powstal blad zeby zmienic te tabele
    with pytest.raises(IndexError):
        equation(epsilon, liczby)

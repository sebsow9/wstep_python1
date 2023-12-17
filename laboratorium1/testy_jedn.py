import unittest
liczby = [0, 1, 2, 3]
epsilon = float(input("Podaj epsilon (zakres bledu): "))
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
    


class TestRownania(unittest.TestCase):
    def setUp(self):
        self.result = pow(2, 1/2)
    def test_equation1(self):
        self.assertAlmostEqual(self.result, equation(0.1, liczby),  delta = epsilon)
    def test_equation2(self):
        self.assertAlmostEqual(self.result, equation(0.001, liczby),  delta = epsilon)
    def test_equation3(self):
        self.assertAlmostEqual(self.result, equation(0.00001, liczby),  delta = epsilon)
    def test_raise(self):
        self.assertRaises(IndexError, equation, epsilon, [0,1,2,3])
        
        


unittest.main()


         
        

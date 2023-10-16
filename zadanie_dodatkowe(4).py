liczby = [0, 1, 2, 3]

epsilon = float(input("Podaj epsilon (zakres bledu): "))
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
    
print("Wynik rownania to: %f" %srodek, "lub -%f" %srodek)
        
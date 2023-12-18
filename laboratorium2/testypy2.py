import pytest
ilosc_pierwszych = input("Wprowadz ile ma byc liczb pierwszych (jako liczbe naturalna): ")

#uzyc -s

#sprawdzanie czy uzytkownik podal liczbe naturalna dodatnia
def czy_litera(zmienna):
    if ('a' <= zmienna <= 'z' ):
        return True
    else:
        return False

def czy_cyfra_wieksza_od_zera(cyfra):
    cyfra = int(cyfra)
    if (cyfra <=0 ):
        return True
    else:
        return False

while (czy_litera(ilosc_pierwszych) or czy_cyfra_wieksza_od_zera(ilosc_pierwszych)):
    ilosc_pierwszych = input("Wprowadzona została niepoprawna wartosc, podaj jeszcze raz: ")

ilosc_pierwszych = int(ilosc_pierwszych)


slownik_pierwszych_dwojkowych = {}
slownik_pierwszych_osemkowych = {}
slownik_pierwszych_szesnastkowych = {}
zmienna = 3

count = 0

#funkcja szukajaca liczb pierwszych na podstawie wlasnosci, ze wystarczy sprawdzic do dzielnikow zaokraglonego w gore pierwiastka kwadratowego liczby
def czy_pierwsza(sprawdzana_liczba):
    for z in range(2, int(pow(sprawdzana_liczba, 1/2)+1)):
        x = sprawdzana_liczba % z
        if (x == 0):
            return False
    return True 

#prosta funkcja do zapytania uzytkownika w jaki system zamienic liczbe
def jaki_system(liczba_pierwsza):
    print("Na jaki system powinna zostac zmieniona liczba (%d) ?" %liczba_pierwsza)
    print("a. dwojkowy b. osemkowy c. szesnastkowy")
    #sprawdzanie czy wprowadzona zostala odpowiednia rzecz


    system = str(input())
    while (system != "a" and system != "b" and system != "c"):
        system = str(input("Podaj a, b lub c: "))
    return system 

#zmiana liczby w dwojkowa i wyciagniecie liczby znakow potrzebnych do jej zaprezentowania
def system_dwojkowy(liczba_pierwsza):
    reprezentacja_dwojkowa = bin(liczba_pierwsza).replace("0b", "")
    dlugosc_liczby = len(reprezentacja_dwojkowa)
    return dlugosc_liczby


#zmiana liczby w osemkowa i wyciagniecie liczby znakow potrzebnych do jej zaprezentowania
def system_osemkowy(liczba_pierwsza):
    reprezentacja_osemkowa = oct(liczba_pierwsza).replace("0o", "")
    dlugosc_liczby = len(reprezentacja_osemkowa)
    return dlugosc_liczby

#zmiana liczby w szesnastkowa i wyciagniecie liczby znakow potrzebnych do jej zaprezentowania
def system_szesnastkowy(liczba_pierwsza):
    reprezentacja_szesnatkowa = hex(liczba_pierwsza).replace("0x", "")
    dlugosc_liczby = len(reprezentacja_szesnatkowa)
    return dlugosc_liczby


while (ilosc_pierwszych != count): #dopoki nie znajdziemy n liczb pierwszych proszonych przez uzytkownika to petla dziala
    if (czy_pierwsza(zmienna) == True): #na koncu petlki jest iteracja zmiennej ktora sprawdzamy za kazda kolejna petla while i funkcja czy_pierwsza
        count = count + 1
        y = jaki_system(zmienna)
        if (y == "a"):
            slownik_pierwszych_dwojkowych[zmienna] = system_dwojkowy(zmienna)
        elif (y == "b"):
            slownik_pierwszych_osemkowych[zmienna] = system_osemkowy(zmienna)
        elif (y == "c"):
            slownik_pierwszych_szesnastkowych[zmienna] = system_szesnastkowy(zmienna)


    zmienna = zmienna + 1

#wartosci ze slownikow w tablice
wartosci_dwojkowe = slownik_pierwszych_dwojkowych.values()
wartosci_osemkowe = slownik_pierwszych_osemkowych.values()
wartosci_szesnastkowe = slownik_pierwszych_szesnastkowych.values()


#definiuje funkcje zliczajaca i wprowadzajaca w slownik ilosci konretnych dlugosci na podstawie tablicy wartosci_.....

def ile_znakow(tablica):
    słownik = {}
    for x in tablica:
        if x in słownik:
            słownik[x] += 1
        else:
            słownik[x] = 1
    return słownik

ilosc_dlugosci_dwojkowy = ile_znakow(wartosci_dwojkowe)
ilosc_dlugosci_osemkowe = ile_znakow(wartosci_osemkowe)
ilosc_dlugosci_szesnastkowe = ile_znakow(wartosci_szesnastkowe)


print("Legenda do tekstu ponizej: {ilosc znakow potrzebnych do zamiany : ilosc takich liczb, ilosc znakow potrzebnych do zamiany : ilosc takich liczb, ...}")
print("%s w liczbach zamienionych na dwojkowy " %ilosc_dlugosci_dwojkowy)
print("%s w liczbach zamienionych na osemkowy" %ilosc_dlugosci_osemkowe)
print("%s w liczbach zamienionych na szesnatkowy" %ilosc_dlugosci_szesnastkowe)


def test_counter1():
    assert ile_znakow([2, 3, 3, 3]) == {2: 1, 3: 3}

def test_counter2():
    assert ile_znakow([2, 3, 3, 3, 4, 4, 5]) == {2: 1, 3: 3, 4: 2, 5: 1}

def test_binary_change():
    assert system_dwojkowy(3) == 2

def test_octo_change1():
    assert system_osemkowy(7) == 1

def test_prime():
    assert not czy_pierwsza(4)
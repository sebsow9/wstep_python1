
ilosc_pierwszych = int(input("Wprowadz ile ma byc liczb pierwszych"))
#dodac sprawdzanie czy to liczba
slownik_pierwszych_dwojkowych = {}
slownik_pierwszych_osemkowych = {}
slownik_pierwszych_szesnastkowych = {}
zmienna = 3

count = 0

#funkcja szukajaca liczb pierwszych
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

#tworzymy set list u gory by pozbyc sie duplikatow
#set_wartosci_dwojkowe = list(set(wartosci_dwojkowe))
#set_wartosci_osemkowe = list(set(wartosci_osemkowe))
#set_wartosci_szesnastkowe = list(set(wartosci_szesnastkowe))

#zliczamy ile elementow ma nasza tablica stworzona z setu
#dlugosc_set_dwojkowe = len(set_wartosci_dwojkowe)
#dlugosc_set_osemkowe = len(set_wartosci_osemkowe)
#dlugosc_set_szesnastkow = len(set_wartosci_szesnastkowe)

#definiuje funkcje zliczajaca i wprowadzajaca w liste konkretne elementy

#def ile_znakow(tablica):

    








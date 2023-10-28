tryb = "T"
obrot = 1
import random

#przyjalem konwencje wyswietlania napisu ERROR przy wprowadzeniu danych typu 
#pierwiastek z ujemnej liczby itd. zamiast dlugich komunikatow

while ( tryb != "N" and tryb == "T" ): 
    if (obrot == 1):
        print("Kalkulator wykonuje polecenia:")
        print("'+' dodawanie dwoch liczb" )
        print("'-' odejmowanie pierwszej liczby od drugiej")
        print("'*' mnozenie dwoch liczb")
        print("'/' dzielenie pierwszej liczby przez druga")
        print("'#' pierwiastek pierwszej liczby stopnia drugiej liczby")
        print("'^' potega pierwszej liczby stopnia drugiej liczby")
        print("'x' losowa liczba z zakresu dwoch liczb")
        print("Wprowadz dwie liczby zatwierdzajac kazda klawiszem 'ENTER'")    
    elif (obrot > 1):
        print("Wprowadz nowe dane:")
    liczba_1 = int(input())
    liczba_2 = int(input()) 
    znak = str(input("Podaj znak aby wykonac polecenie mu odpowiadajace i zatwierdz klawiszem ' ENTER ': "))
    if (znak == "+"):
        wynik = liczba_1 + liczba_2
        print("Wynik dodawania: %d" %wynik)
    elif (znak == "-"):
        wynik = liczba_1 - liczba_2
        print("Wynik odejmowania: %d" %wynik)
    elif (znak == "*"):
        wynik = liczba_1*liczba_2
        print("Wynik mnozenia: %d" %wynik)
    elif (znak == "/"):
        if (liczba_2 == 0):
            print("ERROR (division by 0)")
        else:
            wynik = float(liczba_1 / liczba_2)
            print("Wynik dzielienia to %.3f" %wynik)
    elif (znak == "#"):
        if (liczba_1 < 0):
            print("ERROR")
        else:
            wynik = float(pow(liczba_1, 1/liczba_2))
            print("Wynik pierwiastkowania: %.4f" %wynik)
    elif (znak == "^"):
        wynik = float(pow(liczba_1, liczba_2))
        print("Wynik potegowania: %.2f" %wynik)
    elif (znak == "x"):
        if (liczba_1 < liczba_2):
            wynik = random.randint(liczba_1, liczba_2)
        else:
            wynik = random.randint(liczba_2, liczba_1)
        print("Losowa liczba to: %d" %wynik)
    print("Czy chcesz wprowadzic nowe dane odpowiedz tak : 'T' lub nie 'N'")
    tryb = str(input())

    
    obrot = obrot + 1

    
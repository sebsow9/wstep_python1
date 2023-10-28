import random
x = int(input("Podaj rozmiar choinki: "))


pomocnicza_2 = 2
bombka = "o"
pomocnicza = x
zmienna_gwiazdek = "*"
spacje = ""
spacje_2 = ""
for y in range(1, x+1):
    
    for f in range(1, pomocnicza):
        spacje = spacje + " "
        
    
    pomocnicza = pomocnicza - 1
    if (y == 1):
        print(spacje, end="")
        print("X")
    elif (y>1):
        print(spacje, end="")
        for e in range(1, pomocnicza_2):
            zmienna = random.randint(1, pomocnicza_2 - 1)
            #wywieszanie bombek pozostawiam losowosci,
            #nigdy nie wiadomo jakie ktos ma preferencje do rozwieszania bombek
            #wiec losowoscia przy nieskonczonej liczbie prob pokryjemy
            #wszystkie mozliwe rozwieszenia bombek :)))))
            if (zmienna == e):
                print("o", end="")
            else:
                print("*", end="")
        print("")
    pomocnicza_2 = pomocnicza_2 + 2
    spacje = ""
    
for g in range(1, x-1):
        spacje_2 = spacje_2 + " "
print(spacje_2, "U")
    
    

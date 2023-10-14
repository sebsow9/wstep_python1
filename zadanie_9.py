rodzaj_operacji = ""
saldo = 500
#zakladamy ze cos tam ktos ma w tym banku

while (rodzaj_operacji != "d" and rodzaj_operacji != "D")  :
    
    print("Co chcesz zrobic? A.Wpłata B.Wypłata C.Sprawdź saldo D.Wyjdź")
    
    rodzaj_operacji = str(input())
    
    if (rodzaj_operacji == "a" or rodzaj_operacji == "A"):
        print("Ile chcesz wplacic?")
        wplata = int(input())
        while (wplata < 0):
            print("Nieprawidlowa kwota, podaj jeszcze raz:")
            wplata = int(input())
        saldo = saldo + wplata
        
        print("Wplacono: %d" %wplata, "Saldo wynosi: %d" %saldo)
    
    elif (rodzaj_operacji == "b" or rodzaj_operacji == "B"):
        
        print("Ile chcesz wyplacic?")
        
        wyplata = int(input())
        
        while (wyplata > saldo or wyplata < 0):
             if (wyplata < 0):
                 print ("Nieprawidlowa kwota, podaj jeszcze raz: ")
                 wyplata = int(input())
             else:
                 print("Za male saldo = %d, prosze podac inna kwote: " %saldo)
                 wyplata = int(input())               
            
        saldo = saldo - wyplata 
        
        print("Wyplacono %d" %wyplata, "Saldo po operacji: %d" %saldo)    
    
    elif (rodzaj_operacji == "c" or rodzaj_operacji == "C"):
        
        print("Saldo: %d" %saldo)

rodzaj_operacji = ""
saldo = 500
#zakladamy ze cos tam ktos ma w tym banku
pin = "1234"
proby = 3
wyplata = 0
while (rodzaj_operacji != "d" and rodzaj_operacji != "D")  :
    
    print("Co chcesz zrobic? A.Wpłata B.Wypłata C.Sprawdź saldo D.Wyjdź")
    
    rodzaj_operacji = str(input())
    
    if (rodzaj_operacji == "a" or rodzaj_operacji == "A"):
        
        kontrola_pin = str(input("Podaj 4 cyfrowy pin:  "))
        if (kontrola_pin != pin):
            while (kontrola_pin != pin and proby > 0):
                kontrola_pin = str(input("Bledny pin, podaj jeszcze raz (pozostale proby: %d):  " %proby))
                proby = proby - 1
                if (proby == 0):
                    print("Wykorzystano wszystkie proby, wychodze z programu")
                    exit()
                elif (kontrola_pin == pin):
                    print("Ile chcesz wplacic?")
                    wplata = int(input())
                    while (wplata < 0):
                        print("Nieprawidlowa kwota, podaj jeszcze raz:")
                        wplata = int(input())
                    saldo = saldo + wplata
                    proby = 3
                    print("Wplacono: %d" %wplata, "Saldo wynosi: %d" %saldo)
                    pass

            
            
                 

        elif (kontrola_pin == pin):
            print("Ile chcesz wplacic?")
            wplata = int(input())
            while (wplata < 0):
                print("Nieprawidlowa kwota, podaj jeszcze raz:")
                wplata = int(input())
            saldo = saldo + wplata
        
            print("Wplacono: %d" %wplata, "Saldo wynosi: %d" %saldo)
    
    elif (rodzaj_operacji == "b" or rodzaj_operacji == "B"):
        kontrola_pin = str(input("Podaj 4 cyfrowy pin:  "))
        if (kontrola_pin != pin):
            while (kontrola_pin != pin and proby > 0):
                kontrola_pin = str(input("Bledny pin, podaj jeszcze raz (pozostale proby: %d):  " %proby))
                proby = proby - 1
                if (proby == 0):
                    print("Wykorzystano wszystkie proby, wychodze z programu")
                    exit()
                elif (kontrola_pin == pin):
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
                    proby = 3
                    print("Wyplacono %d" %wyplata, "Saldo po operacji: %d" %saldo)
                    pass
        
        
        elif (kontrola_pin == pin):
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
        kontrola_pin = str(input("Podaj 4 cyfrowy pin:  "))
        if (kontrola_pin != pin):
            while (kontrola_pin != pin and proby > 0):
                kontrola_pin = str(input("Bledny pin, podaj jeszcze raz (pozostale proby: %d):  " %proby))
                proby = proby - 1
                if (proby == 0):
                    print("Wykorzystano wszystkie proby, wychodze z programu")
                    exit()
                elif (kontrola_pin == pin):
                    print("Saldo wynosi: %d" %saldo)
                    proby = 3
                    pass
        elif (kontrola_pin == pin):            
            print("Saldo: %d" %saldo)

zakres_1 = int(input("wprowadz pierwsza liczbe: "))
zakres_2 = int(input("wprowadz druga liczbe: "))

if (zakres_1 < 0 and zakres_2 > 0):
    zakres = zakres_2 - zakres_1
elif (zakres_2 < 0 and zakres_1 > 0):
    zakres = zakres_1 - zakres_2    
elif (zakres_2 < 0 and zakres_1 < 0):
    if (zakres_2 < zakres_1):
        zakres = (zakres_2 - zakres_1)*(-1)
    else:
        zakres = zakres_2 - zakres_1
else:
    if (zakres_1 > zakres_2):
        zakres = zakres_1 - zakres_2
    else:
        zakres = zakres_2 - zakres_1


#zakladam ze nasza liczba srednia jest liczba w polowie mojego "zakresu" tzn.
#ze po dodaniu polowy przezemnie przyznanego "zakresu" do liczby otrzymujemy liczbe srednia np.
# zakres od 2-10 to srednia to 6 a dla 1-10 byloby to 5,5

if (zakres < 20 and zakres > 0 ):
    if (zakres_1 < zakres_2):
        for x in range(zakres_1, zakres_2):
            print(x, "\n")
        print(zakres_2)    
    elif (zakres_2 < zakres_1):
        for y in range(zakres_2, zakres_1):
           print(y, "\n")
        print(zakres_1)
if (zakres > 19):
    if (zakres%2 == 0):
        polowa_1 = int(zakres/2)
        if (zakres_1 < zakres_2):
            gorna_granica_1 = zakres_1 + polowa_1
            dolna_granica_2 = zakres_2 - polowa_1
            for x in range(gorna_granica_1 - 3, gorna_granica_1):
                print(x)
            for y in range(dolna_granica_2 + 1, dolna_granica_2 + 4):
                print(y)
            
        else:
            gorna_granica_2 = zakres_2 + polowa_1
            dolna_granica_1 = zakres_1 - polowa_1
            for x in range(gorna_granica_2 - 3, gorna_granica_2):
                print(x)
            for y in range(dolna_granica_1 + 1, dolna_granica_1 + 4):
                print(y)
    else:
        polowa_2 = int((zakres + 1)/2)
        if (zakres_1 < zakres_2):
            granica_1 = zakres_1 + polowa_2
            for x in range(granica_1 - 3, granica_1 + 3):
                print(x)
        else:
            granica_2 = zakres_2 + polowa_2
            for y in range(granica_2 - 3, granica_2 + 3):
                print(y)
else:
    print("zakres jest rowny zero, brak liczb do pokazania")


            




     
        

#pobieranie zmiennych

x = int(input("Podaj pierwsza liczbe: "))

y = int(input("Podaj druga liczbe: "))

#warunek wiekszosci od zera dwoch liczb
if (x<0 and y<0):
    print("koncze program z powodu dwoch liczb ujemnych")
    exit()
elif (x<0 and y>0):
    x = x*(-1)
elif (x>0 and y<0):
    y = y*(-1)



#obliczenia arytmetyczne
suma = x + y
roznica = x - y 
iloczyn = x*y
iloraz = float(x/y)
pierwx = float(pow(x, 1/2))
pierwy = float(pow(y, 1/2))
kwadratx = pow(x, 2)
kwadraty = pow(y, 2)

#wypisanie wynikow na ekran

print("Suma x+y=%d" %suma, "roznica x-y=%d" %roznica,)
if (iloczyn == 10):
    print("iloczyn x*y=%d Yay!" %iloczyn, "iloraz x/y=%f" %iloraz)
else:
    print("iloczyn x*y=%d" %iloczyn, "iloraz x/y=%f" %iloraz)
print("pierwiastek kwadratowy x=%f" %pierwx, "i y=%f" %pierwy)
print("druga potega x=%d" %kwadratx,"i y=%d" %kwadraty)


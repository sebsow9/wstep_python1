import random
import matplotlib.pyplot as plt
import numpy as np
N_queens = int(input("Podaj ilość hetmanow: "))

tableofpositions = [(random.randint(1,8), random.randint(1,8)) for _ in range(N_queens)]
rowtable = []
columntable =[]

print(tableofpositions)



def draw_chessboard():
    fig, ax = plt.subplots() 

    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0: #wspolrzedne kwadratow jak w macierzy
                color = 'black'     
            else: 
                color = 'white'
            square = plt.Rectangle((i, j), 1, 1, facecolor=color, edgecolor='black') #pierwszy nawias to wspolrzedne drugi to szerokosc i wysokosc
            
            ax.add_patch(square)
            
            for g in tableofpositions:
                
                zmienna1 = int(str(g[0]))
                zmienna2 = int(str(g[1]))
                            
                if zmienna1 == j+1 and zmienna2 == i+1:
                    queen = plt.Rectangle((i+0.25, j+0.25), 0.5, 0.5, facecolor= 'pink', edgecolor='black')
                    ax.add_patch(queen)

    #limity osi musza sie zgadzac z iloscia kwadratow do nich wlozonych
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    
    
        
    


    #dla upiekszenia wyrownujemy rysunek do kwadratu
    ax.set_aspect('equal', adjustable='box')

    plt.show()

for z in tableofpositions:
    
    rowtable = rowtable + [z[0]]
    
    columntable = columntable +[z[1]]

def row_column(table, table2):
    
    for g in range(len(table)): 
        
        for f in range(len(table)): #tablica bez elemntu g, wiec sprawdzamy kazdy element po kolei oprocz g
            
            if table[f] == table[g] and f!=g: #rows check
                return True
    
    for a in range(len(table2)):
        
        for b in range(len(table2)): #tablica bez elemntu a, wiec sprawdzamy kazdy element po kolei oprocz a
            
            if table2[b] == table2[a] and b!=a: #columns check
                return True       
        


if row_column(rowtable, columntable) == True:
    
    print("Szachują się")

else:
    
    print("Nie szachują się")





draw_chessboard()
import random
import matplotlib.pyplot as plt

N_queens = int(input("Podaj ilość hetmanow: "))

tableofpositions = [(random.randint(1,8), random.randint(1,8)) for _ in range(N_queens)]

#zmienna = int(str(tableofpositions[0])[3:4])

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
                
                #argument1 = zmienna1[0]
                #argument2 = zmienna2[0]
                
                
               
                if zmienna1 == j+1 and zmienna2 == i+1:
                    queen = plt.Rectangle((i+0.25, j+0.25), 0.5, 0.5, facecolor= 'blue', edgecolor='black')
                    ax.add_patch(queen)

    #limity osi musza sie zgadzac z iloscia kwadratow do nich wlozonych
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    

    #dla upiekszenia wyrownujemy rysunek do kwadratu
    ax.set_aspect('equal', adjustable='box')

    plt.show()

draw_chessboard()
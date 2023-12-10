import random
import matplotlib.pyplot as plt

N_queens = int(input("Podaj ilość hetmanow: "))


Queen_who_sees1 = (0, 0) 
Queen_who_sees2 = (0, 0)
parameter = ""

tableofpositions = [(random.randint(1,8), random.randint(1,8)) for _ in range(N_queens)]
rowtable = []
columntable =[]

print(tableofpositions)



def draw_chessboard():
    global Queen_who_sees1, Queen_who_sees2, parameter, x_1, x_2, y_1, y_2
    fig, fig2 = plt.subplots() 

    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0: #wspolrzedne kwadratow jak w macierzy
                color = 'black'     
            else: 
                color = 'white'
            square = plt.Rectangle((i, j), 1, 1, facecolor=color, edgecolor='black', linewidth = 0.1) #pierwszy nawias to wspolrzedne drugi to szerokosc i wysokosc
            
            fig2.add_patch(square)
            
            for g in tableofpositions:
                
                zmienna1 = int(str(g[0]))
                zmienna2 = int(str(g[1]))
                            
                if zmienna1 == j+1 and zmienna2 == i+1:
                    queen = plt.Rectangle((i+0.15, j+0.15), 0.7, 0.7, facecolor= 'blue', edgecolor='black', linewidth = 0.1)
                    fig2.add_patch(queen)
    
    if parameter == "row":
        helping = abs(x_1 - x_2)
        
        if x_1 > x_2:
            
            for _ in range(helping-1):
                x_1 = x_1 - 1
                helpingsquare = plt.Rectangle((x_1 - 1, y_1 - 0.75), 1, 0.5, facecolor = 'red', edgecolor = 'black', linewidth = 0 )
                fig2.add_patch(helpingsquare)
        else:
            for _ in range(helping-1):
                x_2 = x_2 - 1
                helpingsquare = plt.Rectangle((x_2 - 1, y_1 - 0.75), 1, 0.5, facecolor = 'red', edgecolor = 'black', linewidth = 0 )
                fig2.add_patch(helpingsquare)

    elif parameter == "column":
        helping = abs(y_1 - y_2)
        
        if y_1 > y_2:
            
            for _ in range(helping-1):
                y_1 = y_1 - 1
                helpingsquare = plt.Rectangle((x_1 - 0.75, y_1 - 1), 0.5, 1, facecolor = 'red', edgecolor = 'black', linewidth = 0 )
                fig2.add_patch(helpingsquare)
        else:
            for _ in range(helping-1):
                y_2 = y_2 - 1
                helpingsquare = plt.Rectangle((x_1 - 0.75, y_2 - 1), 0.5, 1, facecolor = 'red', edgecolor = 'black', linewidth = 0 )
                fig2.add_patch(helpingsquare)
    
    
    
    #limity osi musza sie zgadzac z iloscia kwadratow do nich wlozonych
    fig2.set_xlim(0, 8)
    fig2.set_ylim(0, 8)
    
    
        
    


    #dla upiekszenia wyrownujemy rysunek do kwadratu
    fig2.set_aspect('equal', adjustable='box')

    
    plt.savefig('example.pdf')
    

for z in tableofpositions:
    
    rowtable = rowtable + [z[0]]
    
    columntable = columntable + [z[1]]

def row_column(table, table2, big_table):
    global Queen_who_sees1, Queen_who_sees2, parameter

    for g in range(len(table)): 
        
        for f in range(len(table)): #iteracja po elemntach rodzielona zeby sprawdzac indeksy
            
            if table[f] == table[g] and f!=g: #rows check
                Queen_who_sees2 = big_table[f]
                Queen_who_sees1 = big_table[g]
                parameter = "row"   #???????????????
                return True
    
    for a in range(len(table2)):
        
        for b in range(len(table2)): 
            
            if table2[b] == table2[a] and b!=a: #columns check
                Queen_who_sees1 = big_table[b]
                Queen_who_sees2 = big_table[a]
                parameter = "column"
                return True
                   
        



def diagonal(table):
    global Queen_who_sees1, Queen_who_sees2, parameter
    for Queen in table:
        temporary_row = Queen[0]
        temporary_column = Queen[1]
        
        for Queen_to_check in table:
            while temporary_column < 9 and temporary_row > 0: #prawy dol przekatnej \ 
                if temporary_row == Queen_to_check[0] and temporary_column == Queen_to_check[1] and Queen != Queen_to_check:
                    
                    Queen_who_sees1 = Queen
                    Queen_who_sees2 = Queen_to_check
                    parameter = "prawydol"
                    
                    return True
                temporary_row = temporary_row - 1
                temporary_column = temporary_column + 1
                
                
            temporary_column = Queen[1]
            temporary_row = Queen[0]
            while temporary_column > 0 and temporary_row > 0: #lewy dol przekatnej /
                if temporary_row == Queen_to_check[0] and temporary_column == Queen_to_check[1] and Queen != Queen_to_check:
                    
                    Queen_who_sees1 = Queen
                    Queen_who_sees2 = Queen_to_check
                    parameter = "lewydol"
                    
                    return True
                temporary_row = temporary_row - 1
                temporary_column = temporary_column - 1
                

            temporary_column = Queen[1]
            temporary_row = Queen[0]
            while temporary_column < 9 and temporary_row < 9: #101 #prawa gora przekatnej /
                if temporary_row == Queen_to_check[0] and temporary_column == Queen_to_check[1] and Queen != Queen_to_check:
                    
                    Queen_who_sees1 = Queen
                    Queen_who_sees2 = Queen_to_check
                    parameter = "prawagora"
                    
                    return True
                temporary_row = temporary_row + 1
                temporary_column = temporary_column + 1
                

            temporary_column = Queen[1]
            temporary_row = Queen[0]
            while temporary_column > 0   and temporary_row < 9: #101: #lewa gora przekatnej \ 
                if temporary_row == Queen_to_check[0] and temporary_column == Queen_to_check[1] and Queen != Queen_to_check: #table.index(Queen) != table.index(Queen_to_check)
                    Queen_who_sees1 = Queen
                    Queen_who_sees2 = Queen_to_check
                    parameter = "lewagora"
                    
                    
                    return True
                temporary_row = temporary_row + 1
                temporary_column = temporary_column - 1
                

            
                
                

if row_column(rowtable, columntable, tableofpositions) == True:
    
    print("Szachują się")

elif diagonal(tableofpositions) == True:
    
    print("Szachują się")

else:
    
    print("Nie szachują się")



y_1, x_1 = Queen_who_sees1
print(f"{y_1}, {x_1}")
#x_1 = Queen_who_sees1[1]
y_2, x_2 = Queen_who_sees2
print(f"{y_2}, {x_2}")
#x_2 = Queen_who_sees2[1]



draw_chessboard()
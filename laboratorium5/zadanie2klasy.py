import random
import matplotlib.pyplot as plt

class Chessboard:
    def __init__(self, n_queens):
        self.N_queens = n_queens
        self.queen_who_sees1 = (0, 0)
        self.queen_who_sees2 = (0, 0)
        self.parameter = ""
        self.table_of_positions = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(n_queens)]
        self.row_table = []
        self.column_table = []
        self.fig2 = None

    def draw_chessboard(self):
        fig, self.fig2 = plt.subplots()

        for i in range(100):
            for j in range(100):
                color = 'black' if (i + j) % 2 == 0 else 'white'
                square = plt.Rectangle((i, j), 1, 1, facecolor=color, edgecolor='black', linewidth=0.1)
                self.fig2.add_patch(square)

                for g in self.table_of_positions:
                    zmienna1 = int(str(g[0]))
                    zmienna2 = int(str(g[1]))

                    if zmienna1 == j + 1 and zmienna2 == i + 1:
                        queen = plt.Rectangle((i + 0.15, j + 0.15), 0.7, 0.7, facecolor='blue', edgecolor='black',
                                              linewidth=0.1)
                        self.fig2.add_patch(queen)

        if self.parameter == "row":
            self.highlight_row(self.queen_who_sees1[1], self.queen_who_sees1[0], self.queen_who_sees2[1])
        elif self.parameter == "column":
            self.highlight_column(self.queen_who_sees1[1], self.queen_who_sees1[0], self.queen_who_sees2[0])
        elif self.parameter in ["prawydol", "lewydol", "prawagora", "lewagora"]:
            self.highlight_diagonal(self.queen_who_sees1, self.queen_who_sees2, self.parameter)

        self.fig2.set_xlim(0, 100)
        self.fig2.set_ylim(0, 100)
        self.fig2.set_aspect('equal', adjustable='box')

        plt.savefig('example.pdf')
        plt.show()

    def highlight_row(self, x1, y1, x2):
        helping = abs(x1 - x2)
        direction = 1 if x1 > x2 else -1  
        for _ in range(helping - 2):
            x1 = x1 - direction
            helpingsquare = plt.Rectangle((x1 - 1.5 * direction, y1 - 0.75), 1, 0.5, facecolor='red', edgecolor='black',linewidth=0)
            self.fig2.add_patch(helpingsquare)

    def highlight_column(self, x1, y1, y2):
        helping = abs(y1 - y2)
        direction = 1 if y1 > y2 else -1  
        for _ in range(helping - 2):
            y1 = y1 - direction
            helpingsquare = plt.Rectangle((x1 - 0.75, y1 - 1.5 * direction), 0.5, 1, facecolor='red', edgecolor='black',linewidth=0)
            self.fig2.add_patch(helpingsquare)

    def highlight_diagonal(self, queen_who_sees1, queen_who_sees2, parameter):
        x1, y1 = queen_who_sees1
        x2, y2 = queen_who_sees2

        helping = abs(x1 - x2)

        if parameter == "prawydol":
            for _ in range(helping - 1):
                helpingsquare = plt.Rectangle((x1, y1 - 2), 1, 1, facecolor='red', edgecolor='black', linewidth=0.1)
                self.fig2.add_patch(helpingsquare)
                x1 = x1 + 1
                y1 = y1 - 1
        elif parameter == "lewydol":
            for _ in range(helping - 1):
                x1 = x1 - 1
                y1 = y1 - 1
                helpingsquare = plt.Rectangle((x1 - 1, y1 - 1), 1, 1, facecolor='red', edgecolor='black', linewidth=0.1)
                self.fig2.add_patch(helpingsquare)
        elif parameter == "prawagora":
            for _ in range(helping - 1):
                helpingsquare = plt.Rectangle((x1, y1), 1, 1, facecolor='red', edgecolor='black', linewidth=0.1)
                self.fig2.add_patch(helpingsquare)
                x1 = x1 + 1
                y1 = y1 + 1
        elif parameter == "lewagora":
            for _ in range(helping - 1):
                x1 = x1 - 1
                y1 = y1 + 1
                helpingsquare = plt.Rectangle((x1 - 1, y1 + 1), 1, 1, facecolor='red', edgecolor='black', linewidth=0.1)
                self.fig2.add_patch(helpingsquare)

    def row_column(self):
        for g in range(len(self.row_table)):
            for f in range(len(self.row_table)):
                if self.row_table[f] == self.row_table[g] and f != g:
                    self.queen_who_sees2 = self.table_of_positions[f]
                    self.queen_who_sees1 = self.table_of_positions[g]
                    self.parameter = "row"
                    return True

        for a in range(len(self.column_table)):
            for b in range(len(self.column_table)):
                if self.column_table[b] == self.column_table[a] and b != a:
                    self.queen_who_sees1 = self.table_of_positions[b]
                    self.queen_who_sees2 = self.table_of_positions[a]
                    self.parameter = "column"
                    return True

    def diagonal(self):
        for queen in self.table_of_positions:
            temporary_row = queen[0]
            temporary_column = queen[1]

            for queen_to_check in self.table_of_positions:
                while temporary_column < 101 and temporary_row > 0:  # prawy dol przekątnej \
                    if temporary_row == queen_to_check[0] and temporary_column == queen_to_check[1] and queen != \
                            queen_to_check:
                        self.queen_who_sees1 = queen
                        self.queen_who_sees2 = queen_to_check
                        self.parameter = "prawydol"
                        return True
                    temporary_row = temporary_row - 1
                    temporary_column = temporary_column + 1

                temporary_column = queen[1]
                temporary_row = queen[0]
                while temporary_column > 0 and temporary_row > 0:  # lewy dol przekątnej /
                    if temporary_row == queen_to_check[0] and temporary_column == queen_to_check[1] and queen != \
                            queen_to_check:
                        self.queen_who_sees1 = queen
                        self.queen_who_sees2 = queen_to_check
                        self.parameter = "lewydol"
                        return True
                    temporary_row = temporary_row - 1
                    temporary_column = temporary_column - 1

                temporary_column = queen[1]
                temporary_row = queen[0]
                while temporary_column < 101 and temporary_row < 101:  # 101 #prawa gora przekatnej /
                    if temporary_row == queen_to_check[0] and temporary_column == queen_to_check[1] and queen != \
                            queen_to_check:
                        self.queen_who_sees1 = queen
                        self.queen_who_sees2 = queen_to_check
                        self.parameter = "prawagora"
                        return True
                    temporary_row = temporary_row + 1
                    temporary_column = temporary_column + 1

                temporary_column = queen[1]
                temporary_row = queen[0]
                while temporary_column > 0 and temporary_row < 101:  # 101: #lewa gora przekatnej \
                    if temporary_row == queen_to_check[0] and temporary_column == queen_to_check[1] and queen != \
                            queen_to_check:  
                        self.queen_who_sees1 = queen
                        self.queen_who_sees2 = queen_to_check
                        self.parameter = "lewagora"
                        return True
                    temporary_row = temporary_row + 1
                    temporary_column = temporary_column - 1

        return False


if __name__ == "__main__":
    N_queens = int(input("Podaj ilość hetmanow: "))
    chessboard = Chessboard(N_queens)
    chessboard.row_table = chessboard.row_table + [z[0] for z in chessboard.table_of_positions]
    chessboard.column_table = chessboard.column_table + [z[1] for z in chessboard.table_of_positions]

    if chessboard.row_column() or chessboard.diagonal():
        print("Szachują się")
    else:
        print("Nie szachują się")

    chessboard.draw_chessboard()
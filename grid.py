import random

class Grid:
    '''The grid of the minesweaper'''
    __DIR_4 = [1, 0, -1, 0, 1] # 4 dirctions
    __DIR_8 = [1, 1, 0, -1, -1, 0, 1, -1, 1] # 8 dirctions

    def __init__(self, size):
        self.__size = size; # size of the grid
        self.__data = [[0 for i in range(size)]for j in range(size)] # data = -1 -> mine, data >= 0 -> how much mines near by it
        self.__status = [[0 for i in range(size)]for j in range(size)] # = 0 -> unvisited, = 1 -> visited, = -1 -> flagged
        self.__count = 0 # count how much points are visited

    def __str__(self):
        output = ""
        cur = 0
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                cur = self.__status[i][j]
                if cur == 0: # unvisited
                    output += " *"
                elif cur == 1: # visited
                    output += f" {self.__data[i][j]}"
                else: # flagged
                    output += " !"
                # output += "{:3d}".format(self.__data[i][j])
            output += "\n"
        return output
    
    @staticmethod
    def out_of_bound(x, y, size):
        return x < 0 or x >= size or y < 0 or y >= size

    def generate_mine_pos(self, row, col, num_mine):
        '''Generate the positions of mines'''
        size = self.__size

        # Don't generate any mines in the eight points around the first click and itself
        unable_have_mine = [row * size + col] 
        for i in range(0, 8):
            x = row + self.__DIR_8[i]; y = col + self.__DIR_8[i+1]
            if Grid.out_of_bound(x, y, size): continue
            unable_have_mine.append(x * size + y)

        # Generate the positions of mines
        able_have_mine = set(range(0, size * size)).difference(set(unable_have_mine))
        m = random.sample(able_have_mine, num_mine)
        for i in m:
            self.__data[i // size][i % size] = -1

    def set_data(self):
        '''Setting the data, counting how much mines are there near by for each position in O(n^2) time'''

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if self.__data[i][j] == -1: continue # it's a mine
                for k in range(0, 8):
                    x = i + self.__DIR_8[k]; y = j + self.__DIR_8[k+1]
                    if Grid.out_of_bound(x, y, self.__size): continue
                    if self.__data[x][y] == -1: # it is a mine
                        self.__data[i][j] += 1

    def add_flag(self, x, y):
        '''add a flag on (x, y)'''
        self.__status[x][y] = -1

    def remove_flag(self, x, y):
        '''remove the flag on (x, y)'''
        self.__status[x][y] = 0

    def clickable(self, x, y):
        '''chick if (x, y) are not clicked or flagged'''
        return self.__status[x][y] == 0
    
    def is_mine(self, x, y):
        '''check if (x, y) has a mine'''
        return self.__data[x][y] == -1
    
    def update_status(self, x, y):
        '''Once clicked, update the status of points which are near by the clicked point. Have done it by DFS'''
        if Grid.out_of_bound(x, y, self.__size) or self.__status[x][y] != 0: return 

        self.__status[x][y] = 1
        self.__count += 1
        
        if self.__data[x][y] != 0: return # if data[x][y] != 0(i.e., there is a mine near by), stop updating

        for i in range(0, 4):
            self.update_status(x + self.__DIR_4[i], y + self.__DIR_4[i+1])

    def win(self, num_mine):
        '''check if all the points do not have mine are all clicked, if yes, player win the game'''
        return self.__size ** 2 - num_mine == self.__count

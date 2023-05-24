from grid import Grid

class MineSweaper:
    __SIZE = 9
    __NUM_MINE = 10
    
    def __init__(self):
        self.__grid = Grid(self.__SIZE)

    def __str__(self):
        return str(self.__grid)
    
    def set_grid(self):
        self.__grid.generate_mine_pos(5, 5, self.__NUM_MINE)
        self.__grid.set_data()

    def add_flag(self, x, y):
        ''' #TODO
        if (x, y) already has flag: 
            print error message
            return  
        ''' 
        self.__grid.add_flag(x, y)

    def remove_flag(self, x, y):
        self.__grid.remove_flag(x, y)
    
    def click(self, x, y):
        if not self.__grid.clickable(x, y):
            # TODO print error message
            return False
        
        ''' #TODO
        if input format is not correct:
            print error message
            return false
        '''
        if self.__grid.is_mine(x, y):
            # TODO print game over message
            return False
        
        self.__grid.update_status(x, y)

        return True



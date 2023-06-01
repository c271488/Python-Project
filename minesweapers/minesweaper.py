from .grid import Grid
from .gui import GUI

class MineSweaper(GUI):
    __SIZE = 9
    __NUM_MINE = 10

    def __init__(self):
        super().__init__(self.__SIZE)
        self.__grid = Grid(self.__SIZE)
        self.__first_click = True

    def __str__(self):
        return str(self.__grid)

    def set_grid(self, x, y):
        '''setup the grid after the first click'''
        self.__grid.generate_mine_pos(x, y, self.__NUM_MINE)
        self.__grid.set_data()

    def win(self):
        return self.__grid.win(self.__NUM_MINE)

    def left_click(self, x, y):
        '''Click event, update the status and check if player win or lose'''
        def left_click_event(event):
            if not self.__grid.clickable(x, y): return

            # if player lose
            if self.__grid.is_mine(x, y):  
                self.show_messagebox("You Lose","Game Over")
                self.close_window()

            # first click, generate the grid
            if self.__first_click:
                self.set_grid(x, y)
                self.__first_click = False
            
            # update the grid, get the updated points
            update_pos = self.__grid.update_status(x, y, [])
            
            # update buttons
            for px, py, status, data in update_pos:
                self.update_button_status(px, py, status, data)

            #if players win
            if self.win():
                self.show_messagebox("You Win","Congratulations")
                self.close_window()

        return left_click_event

    def right_click(self, x, y):
        '''Flag event, flagged or unflagged (x, y)'''
        def right_click_event(event):
            if not self.__grid.flaggable(x, y): return
            status = self.__grid.switch_flag_status(x, y)
            self.update_button_status(x, y, status, 0)
     
        return right_click_event

    def run(self):
        self.window.mainloop()

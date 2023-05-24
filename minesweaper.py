# from grid import Grid

# class MineSweaper:
#     __SIZE = 9
#     __NUM_MINE = 10
    
#     def __init__(self):
#         self.__grid = Grid(self.__SIZE)

#     def __str__(self):
#         return str(self.__grid)
    
#     def set_grid(self):
#         self.__grid.generate_mine_pos(5, 5, self.__NUM_MINE)
#         self.__grid.set_data()

#     def add_flag(self, x, y):
#         ''' #TODO
#         if (x, y) already has flag: 
#             print error message
#             return  
#         ''' 
#         self.__grid.add_flag(x, y)

#     def remove_flag(self, x, y):
#         self.__grid.remove_flag(x, y)
    
#     def click(self, x, y):
#         if not self.__grid.clickable(x, y):
#             # TODO print error message
#             return False
        
#         ''' #TODO
#         if input format is not correct:
#             print error message
#             return false
#         '''
#         if self.__grid.is_mine(x, y):
#             # TODO print game over message
#             return False
        
#         self.__grid.update_status(x, y)

#         return True

#####################################################


import tkinter as tk

# click_left_factory and click_right_factory =>GPT
class GUI:
    def __init__(self, n):
        self.window = tk.Tk()
        self.window.title('Minesweeper')#標題
        self.window.geometry('400x400')#大小
        self.button_grid=[]#二微陣列，存按鈕
        self.generate_button_grid(n)
        self.window.mainloop()#執行視窗

    def generate_button_grid(self,n):
        for i in range(n):
            self.button_grid.append([])
            for j in range(n):
                button = tk.Button(self.window, text=f"{i},{j}") #text:按鈕上的文字
                button.grid(row=i, column=j) #設置button位置
                button.bind("<Button-1>", self.click_left_factory(i, j))  # 左键點擊事件 row:i  col:j
                button.bind("<Button-3>", self.click_right_factory(i, j)) # 右键點擊事件 row:i  col:j
                self.button_grid[i].append(button)

 
    def click_left_factory(self, row, col): #按右鍵
        def click_left(event):#___a
            print(f"左键點擊，按钮位置：列={row}, 行={col}")
            self.refresh_grid(row,col) #更新地圖，可移到其他地方
        return click_left#___b
    #我以為把___a和___b兩行刪掉不影響結果，但會出錯

    def click_right_factory(self, row, col):#同上
        def click_right(event):
            print(f"右键點擊，按钮位置：列={row}, 行={col}")
            self.refresh_grid(row,col)
        return click_right

    def refresh_grid(self,row,col):#刷新地圖
        self.button_grid[row][col].config(text = 'click')

a = GUI(9)

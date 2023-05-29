from tkinter import messagebox
import tkinter as tk

class GUI:

    def __init__(self, n):
        self.window = tk.Tk()
        self.window.title('Minesweeper') # form title
        self.window.geometry('340x370')  # form size
        self.button_grid=[]              # 2d array for storing buttons
        self.generate_button_grid(n)

    def generate_button_grid(self, n):
        '''generate the buttons'''
        for i in range(n):
            self.button_grid.append([])
            for j in range(n):
                button = tk.Button(self.window, height=2, width=4, bg="#D7D7D7") # bg = background yor
                button.grid(row=i, column=j)                                     # set the positon of button
                button.bind("<Button-1>", self.left_click(i, j))                 # left click event
                button.bind("<Button-3>", self.right_click(i, j))                # right click event
                self.button_grid[i].append(button)

 
    def left_click(self, x, y):
        '''Event while left click a button'''
        def left_click_event(event):
            print(f"left click at ({x}, {y})") # for debug
        return left_click_event

    def right_click(self, x, y):
        '''Event while right click a button'''
        def right_click_event(event):
            print(f"right click at ({x}, {y})") # for debug
        return right_click_event

    def update_button_status(self, x, y, status, data):
        '''Update a button's config'''
        if status == 0: # unvisited
            text = ""
        elif status == 1: # visited
            text = f"{data}" if data != 0 else ""
            self.button_grid[x][y].config(state=tk.DISABLED, bg="#E7E7E7", fg="blue")
        else: # flagged
            text = "!"
        self.button_grid[x][y].config(text = text, font="sans 9 bold", fg="red")

    def show_messagebox(self, title, message):
        '''show the win/lose message'''
        messagebox.showinfo(title, message)
        
    def close_window(self):
        self.window.destroy()
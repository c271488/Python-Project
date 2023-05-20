'''
*代表未知
!代表插旗子
數字代表周圍炸彈的數量
'''

import random

class Game:
    
    def __init__(self):
        #9x9 10顆地雷
        self.size=9
        self.num_bombs=10
        self.bombs=[]#炸彈位置
        self.maze=[["*"for i in range(self.size)]for j in range(self.size)]#地圖
        self.visited=[[False for i in range(self.size)]for j in range(self.size)]#格子是否被翻開
        self.flag=[]#插旗位置
        self.opened=0 #開啟的格子數量
        print("遊戲開始")
        print("row代表橫軸，從0開始")
        print('col代表縱軸，從0開始')
        
    def start(self):
        self.print_maze()
        n=input("請輸入座標:row,col: ")
        return n

    def set_bombs(self,row,col):
        n=row*self.size+col  #設置炸彈時跳過開始的格子，用random產生數字，再轉成9x9的格式
        b=random.sample(list(range(0,n))+list(range(n+1,self.size**2)),self.num_bombs)
        
        # print(b)
        for i in b:
            self.bombs.append([i//self.size,i%self.size])
        # self.bombs=[[5, 8], [2, 7], [6, 3], [8, 1]]

    def print_maze(self):
        for i in self.maze:
            print(" ".join(i)) #印地圖

    def set_flag(self,row,col):
        if self.maze[row][col]!="*":
            print("無法插旗")
            return
        self.flag.append([row,col])
        self.maze[row][col]="!"

    def cancel_flag(self,row,col):
        if self.maze[row][col]!="!":
            print("該格無插旗")
            return
        self.flag.remove([row,col])
        self.maze[row][col]="*"

    def show_menu(self):#先用字串讀
        print("1:點擊")
        print("2:插旗")
        print("3:取消插旗")
        print("4:離開")
        n=input("請輸入操作模式：")
        return n
    
    def input_coordinate(self):#先用字串讀
        n=input("請輸入row,col: ")
        return n
    
    def check_coordinate(self,row,col):
        if (row<0 or row>=self.size or col<0 or col>=self.size):
            print("輸入座標錯誤")
            return True
        elif self.visited[row][col]==True:#該格是否已開啟
            print("無法點擊該格")
        return False
    
    def click(self,row,col):
        if [row,col] in self.bombs:
            print("Game Over!")
            return False #先檢測爆炸
        
        self.visited[row][col]=True#代表該格已開啟
        self.opened+=1  #開啟格子+1
        cnt=0 #附近炸彈數量
        directions=[[row-1,col],[row+1,col],[row,col-1],[row,col+1],[row-1,col-1],[row-1,col+1],[row+1,col-1],[row+1,col+1]]
        for i in directions: #檢查附近炸彈數量
            if i[0]>=0 and i[0]<self.size and i[1]>=0 and i[1]<self.size:# and self.visited[i[0]][i[1]]==False: #是否在範圍內
                if i in self.bombs:
                    cnt+=1

        if cnt==0: #附近沒炸彈
            for i in directions:
                if i[0]>=0 and i[0]<self.size and i[1]>=0 and i[1]<self.size and self.visited[i[0]][i[1]]==False:
                    # self.visited[i[0]][i[1]]=True
                    # self.opened+=1
                    self.click(i[0],i[1]) #自動往附近找(DFS)
        
        self.maze[row][col]=str(cnt)#更新地圖，數字改用字串存，印出時比較方便
        return True #True => 沒爆炸

    def check_clear(self): #檢查過關
        # if len(self.bombs)==len(self.flag):
        #     for i in self.bombs:
        #         if i not in self.flag:
        #             break
        #         return True
        # return False
        if self.opened==self.size**2-self.num_bombs: #剩餘格子數量=炸彈數量
            print("恭喜過關")
            return True
        return False
        #True:通關    False:為通關

a=Game()
while 1: #輸入一開始的座標
    try:
        startRow,startCol=map(int,a.start().split(','))
        if a.check_coordinate(startRow,startCol):continue
    except ValueError:
        print('輸入錯誤，請重新輸入')
        continue
    break

a.set_bombs(startRow,startCol)#先開始後再設置炸彈
print(a.bombs)
a.click(startRow,startCol)

while 1:
    try:
        if a.check_clear(): #True:通關    False:為通關
            break
        a.print_maze()
        #
        #先用字串讀進來，再檢查格式，非int用try檢查，int數值用if檢查
        option=int(a.show_menu())
        if option==1:
            row,col=map(int,a.input_coordinate().split(',')) #split把逗號分開
            if a.check_coordinate(row,col):#檢查座標是否在範圍內
                continue

            # row-=1;col-=1 
            if not a.click(row,col):  #Game over
                break
        elif option==2:
            row,col=map(int,a.input_coordinate().split(','))
            if a.check_coordinate(row,col):continue
            # row-=1;col-=1
            a.set_flag(row,col)
        elif option==3:
            row,col=map(int,a.input_coordinate().split(','))
            if a.check_coordinate(row,col):continue
            # row-=1;col-=1
            a.cancel_flag(row,col)
        elif option==4:
            break
        else:
            print('輸入錯誤，請重新輸入')
    except ValueError:
        print('輸入錯誤，請重新輸入')
        continue




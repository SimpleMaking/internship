from tkinter import messagebox
from tkinter import *
import random
from init_window import *
COUNT_OF_POS = 100
HEIGHT = 10
WIDTH = 10

class App(Tk):
         
        def __init__(self, pointer_of_human_player):
            super().__init__()
            self.pointer_of_human_player = pointer_of_human_player
            self.resizable(width=False, height=False)
            self.title("Крестики-нолики наоборот")
            self.defeat_ = False
            self.field = []
            self.cross_count = 0 
            self.show()
            self.mainloop()
        
        
        def can_win(self, a1,a2,a3,smb):
            res = False
            if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
                a3['text'] = 'O'
                res = True
            if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
                a2['text'] = 'O'
                res = True
            if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
                a1['text'] = 'O'
                res = True
            return res

        def computer_move(self):
            for n in range(10):
                if self.can_win(self.field[n][0], self.field[n][1], self.field[n][2], 'O'):
                    return
                if self.can_win(self.field[0][n], self.field[1][n], self.field[2][n], 'O'):
                    return
            if self.can_win(self.field[0][0], self.field[1][1], self.field[2][2], 'O'):
                return
            if self.can_win(self.field[2][0], self.field[1][1], self.field[0][2], 'O'):
                return
            for n in range(10):
                if self.can_win(self.field[n][0], self.field[n][1], self.field[n][2], 'X'):
                    return
                if self.can_win(self.field[0][n], self.field[1][n], self.field[2][n], 'X'):
                    return
            if self.can_win(self.field[0][0], self.field[1][1], self.field[2][2], 'X'):
                return
            if self.can_win(self.field[2][0], self.field[1][1], self.field[0][2], 'X'):
                return
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                if self.field[row][col]['text'] == ' ' and self.pointer_of_human_player == 1:
                    self.field[row][col]['text'] = 'O'
                    self.cross_count += 1
                    break
                elif self.field[row][col]['text'] == ' ' and self.pointer_of_human_player == 2:
                    self.field[row][col]['text'] = 'X'
                    self.cross_count += 1
                    break
        
        
        def defeat_check(self):
            line_of_defeat = list()
            for y in range(6):
                for x in range(6):
                    line_of_defeat = list()
                    ch = self.field[y][x]['text']
                    line_of_defeat.append(self.field[y][x])
                    defeat = True
                    for i in range(1, 5):
                        if self.field[y + i][x + i]['text'] != ch:
                            defeat = False
                            line_of_defeat = list()
                            break
                        elif self.field[y + i][x + i]['text'] != ' ':
                            line_of_defeat.append(self.field[y + i][x + i])
                            
                    if defeat:
                        if ch == 'X':
                            for value in line_of_defeat:
                                value['background'] = 'yellow'
                            messagebox.showinfo("Оповещение", "Крестики проиграли, а нолики выиграли!")
                            self.destroy()
                            return True
                        elif ch == 'O':
                            for value in line_of_defeat:
                                value['background'] = 'yellow'
                            messagebox.showinfo("Оповещение", "Нолики проиграли, а крестики выиграли!")
                            self.destroy()
                            return True
                        
            line_of_defeat = list()          
            for y in range(4, 10):
                for x in range(6):
                    line_of_defeat = list()
                    ch = self.field[y][x]['text']
                    line_of_defeat.append(self.field[y][x])
                    defeat = True
                    for i in range(1, 5):
                        if self.field[y - i][x + i]['text'] != ch:
                            defeat = False
                            line_of_defeat = list()
                            break
                        elif self.field[y - i][x + i]['text'] != ' ':
                            line_of_defeat.append(self.field[y - i][x + i])
                            
                    if defeat:
                        if ch == 'X':
                            for value in line_of_defeat:
                                value['background'] = 'yellow'
                            messagebox.showinfo("Оповещение", "Крестики проиграли, а нолики выиграли!")
                            self.destroy()
                            return True
                        elif ch == 'O':
                            for value in line_of_defeat:
                                value['background'] = 'yellow'
                            messagebox.showinfo("Оповещение", "Нолики проиграли, а крестики выиграли!")
                            self.destroy()
                            return True

            return False
        '''
        def check_win(self, smb):
            for n in range(10):
                self.check_line(self.field[n][0], self.field[n][1], self.field[n][2], smb)
                self.check_line(self.field[0][n], self.field[1][n], self.field[2][n], smb)
            self.check_line(self.field[0][0], self.field[1][1], self.field[2][2], smb)
            self.check_line(self.field[2][0], self.field[1][1], self.field[0][2], smb)

        def check_line(self, a1,a2,a3,smb):
            if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
                a1['background'] = a2['background'] = a3['background'] = 'yellow'
                self.game_run = False
        '''
        
        def new_game(self):
            for row in range(10):
                for col in range(10):
                    self.field[row][col]['text'] = ' '
                    self.field[row][col]['background'] = 'lavender'
 
            self.defeat_ = False
            self.cross_count = 0
    
    
        def click(self, row, col):
            
            if self.cross_count >= 100:
                messagebox.showinfo("Оповещение", "Боевая ничья!")
                self.destroy()
                return
            if self.pointer_of_human_player == 1:
                if self.defeat_ != True and self.field[row][col]['text'] == ' ':
                    self.field[row][col]['text'] = 'X'
                    self.cross_count += 1
                    self.defeat_ = self.defeat_check()
                    if self.defeat_ != True and self.cross_count < 100:
                        self.computer_move()
                        self.defeat_ = self.defeat_check()
            else:
                if self.defeat_ != True and self.field[row][col]['text'] == ' ':
                    self.field[row][col]['text'] = 'O'
                    self.cross_count += 1
                    self.defeat_ = self.defeat_check()
                    if self.defeat_ != True and self.cross_count < 100:
                        self.computer_move()
                        self.defeat_ = self.defeat_check()
                  
                           
        def show(self):
            for row in range(10):
                line = []
                for col in range(10):
                    button = Button(self, text=' ', width=2, height=1, font=('Verdana', 20, 'bold'), background='lavender', command=lambda row=row, col=col: self.click(row,col))
                    button.grid(row=row, column=col, sticky='nsew')
                    line.append(button)
                self.field.append(line)
                
            if self.pointer_of_human_player == 2:
                self.computer_move()
                self.defeat_ = self.defeat_check()
            #self.new_button = Button(self, text='new game', command=self.new_game)
            #self.new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
            
if __name__ == "__main__":
    start_window = init_win()
    App(start_window.pointer_of_human_player)

        
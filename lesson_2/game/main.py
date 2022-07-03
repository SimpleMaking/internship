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
            self.iconbitmap('image.ico')
            if self.pointer_of_human_player == 1:
                self.title(f"Крестики-нолики наоборот. Вы крестики")
            else:
                self.title(f"Крестики-нолики наоборот. Вы нолики")
                
            self.defeat_ = False
            self.field = []
            self.count_of_steps = 0 
            self.show()
            self.mainloop()
        
        
        def gen_value_of_point(self):
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                if self.field[row][col]['text'] == ' ' and self.pointer_of_human_player == 1:
                    self.field[row][col]['text'] = 'O'
                    self.count_of_steps += 1
                    break
                elif self.field[row][col]['text'] == ' ' and self.pointer_of_human_player == 2:
                    self.field[row][col]['text'] = 'X'
                    self.count_of_steps += 1
                    break
                
                
        def check_for_computer_moving_diags(self, symbol):
            for y in range(6):
                for x in range(6):
                    cords = list()
                    counter = 0
                    for i in range(0, 5):
                        cords.append((y + i, x + i))
                    
                    for value in cords:
                        if self.field[value[0]][value[1]]['text'] == symbol:
                            counter += 1
                    if counter > 1 and self.count_of_steps < 95:
                        row = random.randint(0, 9)
                        col = random.randint(0, 9)
                        while True:
                            for value in cords:
                                if (row != value[0] and col != value[1]) and self.field[row][col]['text'] == ' ':
                                    self.field[row][col]['text'] = symbol 
                                    self.count_of_steps += 1
                                    return True  
                            row = random.randint(0, 9)
                            col = random.randint(0, 9) 
                    counter = 0
                              
            for y in range(4, 10):
                for x in range(6):
                    cords = list()
                    counter = 0
                    for i in range(0, 5):
                        cords.append((y - i, x + i))
                    
                    for value in cords:
                        if self.field[value[0]][value[1]]['text'] == symbol:
                            counter += 1
                    if counter > 1 and self.count_of_steps < 95:
                        row = random.randint(0, 9)
                        col = random.randint(0, 9)
                        while True:
                            for value in cords:
                                if (row != value[0] and col != value[1]) and self.field[row][col]['text'] == ' ':
                                    self.field[row][col]['text'] = symbol 
                                    self.count_of_steps += 1
                                    return True  
                            row = random.randint(0, 9)
                            col = random.randint(0, 9)
                    counter = 0 
                
            return False
                 
                 
        def check_for_computer_moving_90_hor_and_vert(self, symbol):
            for y in range(10):
                for x in range(6):
                    cords = list()
                    counter = 0
                    for i in range(0, 5):
                        cords.append((y, x + i))
                    
                    for value in cords:
                        if self.field[value[0]][value[1]]['text'] == symbol:
                            counter += 1
                    if counter > 1 and self.count_of_steps < 95:
                        row = random.randint(0, 9)
                        col = random.randint(0, 9)
                        while True:
                            for value in cords:
                                if (row != value[0] and col != value[1]) and self.field[row][col]['text'] == ' ':
                                    self.field[row][col]['text'] = symbol 
                                    self.count_of_steps += 1
                                    return True  
                            row = random.randint(0, 9)
                            col = random.randint(0, 9) 
                    counter = 0
                           
            for x in range(10):
                for y in range(6):
                    cords = list()
                    counter = 0
                    for i in range(0, 5):
                        cords.append((y + i, x))
                    
                    for value in cords:
                        if self.field[value[0]][value[1]]['text'] == symbol:
                            counter += 1
                    if counter > 1 and self.count_of_steps < 95:
                        row = random.randint(0, 9)
                        col = random.randint(0, 9)
                        while True:
                            for value in cords:
                                if (row != value[0] and col != value[1]) and self.field[row][col]['text'] == ' ':
                                    self.field[row][col]['text'] = symbol 
                                    self.count_of_steps += 1
                                    return True  
                            row = random.randint(0, 9)
                            col = random.randint(0, 9)
                    counter = 0 
                    
            return False
        
        
        def computer_moving(self):
           
            if self.pointer_of_human_player == 1:
                if self.check_for_computer_moving_diags('O') or self.check_for_computer_moving_90_hor_and_vert('O'):
                    return
                elif self.check_for_computer_moving_diags('O') != True and self.check_for_computer_moving_90_hor_and_vert('O') != True:
                    self.gen_value_of_point()
                   
            else:
                if self.check_for_computer_moving_diags('X') or self.check_for_computer_moving_90_hor_and_vert('X'):
                    return
                elif self.check_for_computer_moving_diags('X') != True and self.check_for_computer_moving_90_hor_and_vert('X') != True:
                    self.gen_value_of_point()
                    
        
        def defeat_check_90_hor_and_vert(self):
            line_of_defeat = list()
            for y in range(10):
                for x in range(6):
                    line_of_defeat = list()
                    ch = self.field[y][x]['text']
                    line_of_defeat.append(self.field[y][x])
                    defeat = True
                    for i in range(1, 5):
                        if self.field[y][x + i]['text'] != ch:
                            defeat = False
                            line_of_defeat = list()
                            break
                        elif self.field[y][x + i]['text'] != ' ':
                            line_of_defeat.append(self.field[y][x + i])
                            
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
            for x in range(10):
                for y in range(6):
                    line_of_defeat = list()
                    ch = self.field[y][x]['text']
                    line_of_defeat.append(self.field[y][x])
                    defeat = True
                    for i in range(1, 5):
                        if self.field[y + i][x]['text'] != ch:
                            defeat = False
                            line_of_defeat = list()
                            break
                        elif self.field[y + i][x]['text'] != ' ':
                            line_of_defeat.append(self.field[y + i][x])
                            
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
        
        
        def defeat_check_diags(self):
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
            if self.defeat_check_90_hor_and_vert():
                return True
          
            return False
     
      
        def click(self, row, col):
            
            if self.count_of_steps >= COUNT_OF_POS:
                messagebox.showinfo("Оповещение", "Боевая ничья!")
                self.destroy()
                return
            if self.pointer_of_human_player == 1:
                if self.defeat_ != True and self.field[row][col]['text'] == ' ':
                    self.field[row][col]['text'] = 'X'
                    self.count_of_steps += 1
                    self.defeat_ = self.defeat_check_diags()
                    if self.defeat_ != True and self.count_of_steps < 100:
                        self.computer_moving()
                        self.defeat_ = self.defeat_check_diags()
            else:
                if self.defeat_ != True and self.field[row][col]['text'] == ' ':
                    self.field[row][col]['text'] = 'O'
                    self.count_of_steps += 1
                    self.defeat_ = self.defeat_check_diags()
                    if self.defeat_ != True and self.count_of_steps < 100:
                        self.computer_moving()
                        self.defeat_ = self.defeat_check_diags()
                  
                           
        def show(self):
            for row in range(WIDTH):
                line = []
                for col in range(HEIGHT):
                    button = Button(self, text=' ', width=2, height=1, font=('Verdana', 20, 'bold'), background='lavender', command=lambda row=row, col=col: self.click(row,col))
                    button.grid(row=row, column=col, sticky='nsew')
                    line.append(button)
                self.field.append(line)
                
            if self.pointer_of_human_player == 2:
                self.computer_moving()
                self.defeat_ = self.defeat_check_diags()
         
            
if __name__ == "__main__":
    start_window = init_win()
    App(start_window.pointer_of_human_player)

        
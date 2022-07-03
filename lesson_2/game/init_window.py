from tkinter import *


class init_win(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200+450+180")
        self.resizable(width=False, height=False)
        self.iconbitmap('image.ico')
        self.title("Крестики-нолики наоборот")
        self.pointer_of_human_player = 1
        self.but_1 = Button(self, text="play with X", font=('Verdana', 10, 'bold'), command=lambda: self.get_data(1))
        self.but_2 = Button(self, text="play with O", font=('Verdana', 10, 'bold'), command=lambda: self.get_data(2))
        self.but_1.place(x=40, y=60)
        self.but_2.place(x=160, y=60)
        self.mainloop()
    
    def get_data(self, check):
        if check == 1:
            self.pointer_of_human_player = 1
            self.destroy()
        else:
            self.pointer_of_human_player = 2
            self.destroy()

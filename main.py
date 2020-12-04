import random
from tkinter import *


def close(event):
    quit()


def move(event):
    global pos_column, pos_row, k

    if pos_column < count_column - 1 and pos_column > 0:
        pos_column += random.choice([-1, 0, 1])
    elif pos_column == count_column - 1:
        pos_column += random.choice([-1, 0])
    elif pos_column == 0:
        pos_column += random.choice([0, 1])

    if pos_row < count_row - 1 and pos_row > 0: 
        pos_row += random.choice([-1, 1])
    elif pos_row == count_row - 1:
        pos_row += random.choice([-1])
    elif pos_row == 0:
        pos_row += random.choice([1])
    
    if k < 3:
        k += 1
    else:
        button['text'] = 'Click me!\n' + random.choice(emoji)
        

    button.grid(row=pos_row, column=pos_column, stick='nswe')

k = 0

# Parametrs window.
pixel = 60
count_column = 4
count_row = 4

# Parameters button.
pos_row = 2
pos_column = 2
emoji = ['', ')', ':)', ';)', '(', ':(', ';(', '/0_o\\']

# Window.
root = Tk()
root.title('Dextereous button')
root['bg'] = '#fbf1da'

# Settings grid.
for i in range(count_column):
    root.grid_columnconfigure(i, minsize=pixel) 
[root.grid_rowconfigure(i, minsize=pixel) for i in range(count_row)]

button = Button(
    root,
    text='Click me!',
    bg='#7d50e7',
)

button.bind('<ButtonRelease-1>', close)
button.bind('<Enter>', move)
button.grid(row=pos_row, column=pos_column, stick='nswe')
root.mainloop()

import random
from tkinter import *


# pos button.
x = 5
y = 5

def move(event):
    global x, y
    # Check x.
    if x < width - 1 and x > 0:
        x += random.choice([-1,0,1])
    elif x >= width - 1:
        x += random.choice([-1,0])
    elif x <= 0:
        x += random.choice([0,1])
    
    # Check y.
    if y < height - 1 and y > 0:
        y += random.choice([-1,0,1])
    elif y >= height - 1:
        y += random.choice([-1,0])
    elif y <= 0:
        y += random.choice([0,1])

    root.title(f'{x=} {y=}')
    button.grid(column=x, row=y, stick='nswe')


# Settings window.
root = Tk()
root['bg'] = '#c0c0c0'
root.title('Dextereous button')
width = 10
height = 10

# Create grid.
[root.grid_columnconfigure(i, minsize=80) for i in range(width)]
[root.grid_rowconfigure(i, minsize=60) for i in range(height)]

# Create button.
button = Button(
    root,
    text='Click me!',
    bg='#7a51e1',
    fg='#000000',
)

button.grid(column=x, row=y, stick='nswe')
button.bind('<Motion>', move)
button.bind('<Double-Button-1>', lambda event: quit())

root.mainloop()

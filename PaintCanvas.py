from tkinter import *
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfilename as saveAs
import PIL
from PIL import Image, ImageDraw

am = Tk()
am.geometry('600x600')
am.title('AM Paint')
am.resizable(height=False, width=False)

b_color = 'Black'
b_type = StringVar()
b_type.set('round')

def painting(e):
    x1, y1 = e.x-1, e.y-1
    x2, y2 = e.x, e.y
    br = b_type.get()
    c1.create_line(x1, y1, x2, y2, fill=b_color, width=10, capstyle=br)
    draw.line((x1, y1, x2, y2), fill=b_color, width=10)

def change_color():
    global b_color
    b_color = colorchooser.askcolor(color=b_color)[1]

def erase():
    global b_color
    b_color = 'white'

def clear_screen():
    c1.delete(ALL)

def save():
    filename=saveAs(title="Save image as...",defaultextension="*.*",filetype=(("PNG images","*.png"),("JPEG images","*.jpg"),("GIF images","*.gif")))
    image1.save(filename)

c1 = Canvas(am, width=500, height=400, bg='white')
c1.pack(side='bottom', fill='both')
c1.bind('<B1-Motion>', painting)
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)

t = LabelFrame(am, text='Tools', font=('Helvetica', 12, 'bold'))
t.pack(side='top', fill='both', expand='yes')

l1 = Label(t, text='Brush Type', relief='raised', width=14, font=('sans', 10, 'bold'))
l1.place(x=20, y=4)

m1 = OptionMenu(t, b_type, 'round', 'butt', 'projecting')
m1.config(font=('sans', 10, 'bold'))
m1.place(x=20, y=26)

b1 = Button(t, text='Brush Color', font=('sans', 10, 'bold'), command=change_color)
b1.place(x=170, y=14)

b2 = Button(t, text='Eraser', font=('sans', 10, 'bold'), command=erase)
b2.place(x=290, y=14)

b3 = Button(t, text='Clear Screen', font=('sans', 10, 'bold'), command=clear_screen)
b3.place(x=380, y=14)

save = Button(t, text="Save image", font=('sans', 10, 'bold'), command=save)
save.place(x=480, y=14)

am.mainloop()
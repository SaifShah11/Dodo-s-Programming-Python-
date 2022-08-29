from tkinter import *
import numpy as np

#-------------------------- Functions

def add():
    
    x=x_num.get()
    y=y_num.get()

    print(x+y)

def multi():

    x=x_num.get()
    y=y_num.get()

    print(x*y)

def clear():

    x_num.set('')
    y_num.set('')    

#-------------------------- Main Window

win=Tk()
win.minsize(500,300)
win.maxsize(1920,1080)
win.config(bg='black')
win.title('Calculator Program')

#-------------------------- Variables

x_num = DoubleVar()
y_num = DoubleVar()

#-------------------------- Enter Number 01

lab_1=Label(win, text='ENTER FIRST NUMBER',
            font=('Times New Roman',12),


            fg='red',
            bg='black')

lab_1.grid(row=1, column=1)

#-------------------------- Entry Widget 01

lab_2=Entry(win,font=('Times New Roman',10),

            textvariable = x_num)

lab_2.grid(row=1, column=2, padx=50)

#-------------------------- Enter Number 02

lab_3=Label(win, text='ENTER SECOND NUMBER',
            font=('Times New Roman',12),

            fg='red',
            bg='black')

lab_3.grid(row=2, column=1)

#-------------------------- Entry Widget 02

lab_4=Entry(win,font=('Times New Roman',10),

            textvariable = y_num)

lab_4.grid(row=2, column=2, padx=50)

#-------------------------- Addition Button

lab_5=Button(win, text='ADDITION',
            font=('Times New Roman',10,),

            command = add,


            fg='red',
            bg='black')

lab_5.grid(row=3, column=2, padx=50, pady=10)

#-------------------------- Multiplication Button

lab_6=Button(win, text='MULTIPLICATION',
            font=('Times New Roman',10,),

            command = multi,


            fg='red',
            bg='black')

lab_6.grid(row=4, column=2, padx=50)

#-------------------------- Reset Button

lab_7=Button(win, text='RESET',
            font=('Times New Roman',10,),

            command = clear,


            fg='red',
            bg='black')

lab_7.grid(row=5, column=2, padx=50, pady=10)

#-------------------------- Running Window
win.mainloop()



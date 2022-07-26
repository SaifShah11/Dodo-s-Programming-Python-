from tkinter import *

#--------------------------------------(Window)
win=Tk()

win.minsize(500,300)
win.maxsize(1920,1080)

win.title('Calorie-Nutrition Tracker')
win.config(bg='#3b0131')

image=PhotoImage(file='D:\\University\\Summer 2022\\Introduction To Computing\\Python\\Practice Programming\\Calorie Application\\Logo.png')
win.iconphoto(True,image)

#--------------------------------------(Variables)

gender=StringVar()
age=IntVar()
weight=IntVar()
height=IntVar()

#--------------------------------------- (Title)

lab_1=Label(win,text='Your Healthy Journey Begins Here!',
            font=('Open Sans',20),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black')

            
lab_1.pack()

#--------------------------------------- (Enter Gender)

lab_2=Label(win,text='1. Enter your Gender',
            font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black')

lab_2.place(x=279,y=130,

            width=300, height=50)

lab_21=Entry(win)

lab_21.place(x=670, y=130,

             width=150,height=30)

#---------------------------------------- (Enter Age)

lab_3=Label(win,text='2. Enter your Age',
            font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black')

lab_3.place(x=279,y=200,

            width=300, height=50)

lab_31=Entry(win)

lab_31.place(x=670, y=200,

             width=150,height=30)

#---------------------------------------- (Enter Weight)

lab_4=Label(win,text='3. Enter your Weight in Kgs',
            font=('Times New Roman',15),
            padx=50, pady=10,

            fg='#02fae1',
            bg='black')

lab_4.place(x=279,y=270,

            width=300, height=50,)

lab_41=Entry(win)

lab_41.place(x=670, y=270,
             
             width=150,height=30)

#--------------------------------------- (Enter Height)

lab_5=Label(win,text='4. Enter your Height in Centimeters',
            font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black')

lab_5.place(x=279,y=340,

            width=300, height=50)

lab_51=Entry(win)

lab_51.place(x=670, y=340,
             
             width=150,height=30)


#--------------------------------------- (Submit Button)

lab_6=Button(win,text=' Submit ',
            font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black',

            activeforeground='green',
            activebackground='#3b0131')

lab_6.place(x=670,y=410,

            width=150,height=50)




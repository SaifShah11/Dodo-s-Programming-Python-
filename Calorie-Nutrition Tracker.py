    from tkinter import *

#-------------------------------------- (BMR Function)
def BMR():

    M='MALE'.casefold()
    F='FEMALE'.casefold()    

    gender=gender_var.get()

    age=age_var.get()

    weight=weight_var.get()

    height=height_var.get()

     #Calories Based on Assumption of Rest Only

    if gender == M:
        print('BMR (Male) =', 10*weight + 6.25*height - 5*age + 5, 'Kcal')# Mifflin-St Jeor Equation

    elif gender == F:
        print('BMR (Female)=', 10*weight + 6.25*height - 5*age - 161,'Kcal')# Mifflin-St Jeor Equation
    else:
        print('Incorrect Gender Input')

    print()

#-------------------------------------- (Show function)

def show():

    lab_9.insert()
    
#-------------------------------------- (Reset function)

def clear():

    gender_var.set('')
    age_var.set('')
    weight_var.set('')
    height_var.set('')
    
#-------------------------------------- (Window)

win=Tk()

win.minsize(500,300)
win.maxsize(1920,1080)

win.title('Calorie-Nutrition Tracker')
win.config(bg='#3b0131')

image=PhotoImage(file='D:\\University\\Summer 2022\\Introduction To Computing\\Python\\Practice Programming\\Calorie Application\\Logo.png')
win.iconphoto(True,image)

#-------------------------------------- (Variables)

gender_var=StringVar()
age_var=IntVar()
weight_var=IntVar()
height_var=IntVar()

#--------------------------------------- (Title)

lab_1=Label(win,text='Your Healthy Journey Begins Here!',
            font=('Open Sans',30),
            padx=25, pady=10)

win.wm_attributes('-transparentcolor', '#02fae1')
            
lab_1.pack()


#--------------------------------------- (Enter Gender)

lab_2=Label(win,text='1. Enter your Gender',
            font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black')

lab_2.place(x=279,y=130,

            width=300, height=50)

lab_21=Entry(win, font=('Times New Roman',15),

             textvariable=gender_var)

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

lab_31=Entry(win, font=('Times New Roman',15),

             textvariable=age_var)

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

lab_41=Entry(win, font=('Times New Roman',15),

             textvariable=weight_var)

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

lab_51=Entry(win, font=('Times New Roman',15),

             textvariable=height_var)

lab_51.place(x=670, y=340,
             
             width=150,height=30)


#--------------------------------------- (Submit Button)

lab_6=Button(win,text=' Submit ',
            font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black',

            activeforeground='white',
            activebackground='#3b0131',

            command = BMR)

lab_6.place(x=670,y=410,

            width=150,height=50)

#--------------------------------------- (Clear Button)

lab_7=Button(win, text= 'Reset',

             font=('Times New Roman',15),
            padx=25, pady=10,

            fg='#02fae1',
            bg='black',

            activeforeground='white',
            activebackground='#3b0131',

             command = clear)

lab_7.place(x=825,y=410,

            width=150,height=50)


#--------------------------------------- (Show Button)

lab_8=Button(win, text= 'Show',
             font=('times new roman',15),
             padx=25, pady=10,

            fg='#02fae1',
            bg='black',

            activeforeground='white',
            activebackground='#3b0131',

            command = show)

lab_8.place(x=980, y=410,

            width=150, height=50)

#--------------------------------------- (Output Box)

lab_9=Entry(win, font=('times new roman', 15))

lab_9.place(x=300, y=400,

            width=250, height=150)


#--------------------------------------- (Keeps window active)

win.mainloop()






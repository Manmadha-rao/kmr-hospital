from Tkinter import *
import sqlite3

mainwindow= Tk()
mainwindow.iconbitmap("")
mainwindow.title("KMR Hospital")
mainwindow.geometry("780x580")
mainwindow.resizable(False, False)


def save():
    """name = str(name_input1.get())

    if name == str(name_input1.get()):
        print (name)
    elif name != str(name_input1.get()):
        print ('en')

    else:
        print ('en')"""
    try:
        name = str(name_input1.get())
        print (name)
    except:
        print ('en')


    try:
        age=int(name_input2.get())
        print(age)
    except ValueError:
        print('enter the valid age')





lable=Label(mainwindow, text='Enter the Patient Details', font=('arial', 15), bg='red')
lable.grid(row=0, column=1, padx=100, pady=10)

lable1=Label(mainwindow, text='Name: *', font=('arial', 12))
lable1.grid(row=1, column=0,pady=30)
name_input1=Entry(mainwindow, width=20, font=('arial', 10))
name_input1.grid(row=1, column=1, sticky=W)

lable2=Label(mainwindow, text='Age: *', font=('arial', 12))
lable2.grid(row=1, column=1, sticky=E, padx=10)
name_input2= Entry(mainwindow ,width=7)
name_input2.grid(row=1, column=2, sticky=W)



lable3=Label(mainwindow, text='Ph No: *', font=('arial',12))
lable3.grid(row=2, column=0)
name_input3=Entry(mainwindow, width=22)
name_input3.grid(row=2, column=1, sticky=W)

lable4=Label(mainwindow, text='Gender: *', font=('arial', 12))
lable4.grid(row=2, column=1, sticky=E, padx=10)
"""name_input4= Entry(mainwindow, width=6, font=('arial', 10))
name_input4.grid(row=2, column=2, sticky=W)"""

def select(event):
    mylable=Label(mainwindow, text=clicked.get()).place(x=648,y=149)

options = ["   male","female", " others"]
clicked = StringVar()
clicked.set(options[2])
Drop = OptionMenu(mainwindow, clicked, *options, command=select)
Drop.grid(row=2, column=2, sticky=W)

lable5=Label(mainwindow, text='Address: *', font=('arial', 12))
lable5.grid(row=3, column=0, pady=30)
name_input5=Entry(mainwindow, width=50, font=('arial', 10))
name_input5.grid(row=3, column=1, sticky=W)


lable6=Label(mainwindow, text='Postal Pin: *', font=('arial', 12))
lable6.grid(row=4, column=0)
name_input6=Entry(mainwindow, width=22)
name_input6.grid(row=4, column=1, sticky=W)


lable7=Label(mainwindow, text='Health card No:', font=('arial', 12))
lable7.grid(row=5, column=0, pady=30, padx=10)
name_input7= Entry(mainwindow, width=20, font=('arial', 10))
name_input7.grid(row=5, column=1, sticky=W)


lable8=Label(mainwindow, text='Id No(If any): *', font=('arial', 12))
lable8.grid(row=6, column=0, sticky=E, padx=10)
name_input8= Entry(mainwindow, width=20, font=('arial', 10))
name_input8.grid(row=6, column=1, sticky=W)

lable9=Label(mainwindow, text='Blood group:', font=('arial', 12))
lable9.grid(row=4, column=1, sticky=E, padx=20)
name_input9=Entry(mainwindow, width=7)
name_input9.grid(row=4, column=2)

lable10=Label(mainwindow, text='Reference:', font=('arial', 12))
lable10.grid(row=5, column=1, sticky=E, padx=20)
name_input10=Entry(mainwindow, width=25)
name_input10.place(x=500, y=382)



button=Button(mainwindow, text='Register', font=('arial', 12), fg='blue', padx=10, pady=10,command=save)
button.place(x=342, y=450)


mainwindow.mainloop()



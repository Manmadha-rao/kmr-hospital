from Tkinter import *
from PIL import Image, ImageTk

mw = Tk()
mw.title('KMR Hospital')



#creating frame for hospital icon

frame = LabelFrame(mw)
frame.pack()
img = ImageTk.PhotoImage(Image.open("images/kmr.jpg"))
im = Label(frame, image=img).pack()

#creating navicon and buttons inside

def navi():
    sign_in = Tk()
    sign_in.iconbitmap("images/index.png")
    sign_in.title("KMR Hospital")
    sign_in.geometry("400x250+800+100")
    sign_in.resizable(False, False)

    lable=Label(sign_in, text='only Employee use', font=('ariel', 14), bg='orange')
    lable.place(x=110, y=15)

    lable1=Label(sign_in, text="User_name !", font=('ariel', 10))
    lable1.place(x=25, y=80)
    user_input=Entry(sign_in, width=25)
    user_input.place(x=140, y=80)

    lable1=Label(sign_in, text="Password !", font=('ariel', 10))
    lable1.place(x=38, y=130)
    user_input = Entry(sign_in, width=25)
    user_input.place(x=140, y=130)

    button = Button(sign_in, text='Sign_in', font=('ariel', 12), fg='blue')
    button.place(x=100, y=190)


    button1 = Button(sign_in, text='Sign_up', font=('ariel', 12), fg='blue',command=chi)
    button1.place(x=220, y=190)
    
nav = ImageTk.PhotoImage(Image.open("images/na.png"))
navbutton = Button(frame, padx=15, pady=4, image=nav, bg='#171716',command=navi)
navbutton.place(x=1205, y=10)


#creating frame and buttons for mainmenu

frame1=LabelFrame(mw)
frame1.pack()

button1 = Button(frame1, padx=130, pady=5, bg="#f5f3ed", font=(25),text='Our Services',fg="#050ced")
button1.grid(row=0)

button2 = Button(frame1, padx=120, pady=5, bg="#f5f3ed", font=(25),text='Appointment',fg="#050ced")
button2.grid(row=0,column=1)

button3 = Button(frame1, padx=102, pady=5, bg="#f5f3ed", font=(25),text='Our Success',fg="#050ced")
button3.grid(row=0,column=2)

button4 = Button(frame1, padx=70, pady=5, bg="#f5f3ed", font=(25),text='Updated NEWS',fg="#050ced")
button4.grid(row=0,column=3)


#for image view
image_view=LabelFrame(mw)
image_view.pack(side=LEFT)

img1=ImageTk.PhotoImage(Image.open("images/imageview/chi1.png"))
img2=ImageTk.PhotoImage(Image.open("images/imageview/chi2.jpg"))
img3=ImageTk.PhotoImage(Image.open("images/imageview/chi.png"))

im = Label(image_view)
im.pack()


#creating function for images moving automatically      
x=1
def move():
    global x
    if x==4:
        x=1
    if x==1:
        im.config(image=img1)
    elif x==2:
        im.config(image=img2)
    elif x==3:
        im.config(image=img3)
    x+=1
    mw.after(2000,move)
move()
    

#sliders

text_frame = LabelFrame(mw)
text_frame.pack(fill=BOTH,expand=1)


scroll = Scrollbar(text_frame, orient=VERTICAL, width=30)
scroll.pack(side=RIGHT, fill=Y, padx=5)


def chi():
    
    emp = Tk()
    emp.title("KMR Hospital")
    emp.geometry("780x500+427+100")
    emp.resizable(False, False)

    lable=Label(emp, text='Enter the Employee Details', font=('arial', 15), bg="green")
    lable.place(x=250, y=20)

    lable1=Label(emp, text='Name: *', font=('arial', 12))
    lable1.place(x=136, y=100)
    input1 = Entry(emp, width=20, font=('arial', 10))
    input1.place(x=250, y=102)


    lable2=Label(emp, text='Data of Birth: *', font=('arial', 12))
    lable2.place(x=480, y=100)
    input2 = Entry(emp, width=10)
    input2.place(x=630, y=102)

    lable3 = Label(emp, text='Employee Id no !: *', font=('arial', 12))
    lable3.place(x=40, y=170)
    input3 = Entry(emp, width=22)
    input3.place(x=250, y=172)

    lable4 = Label(emp, text='Data of Joining: *', font=('arial', 12))
    lable4.place(x=462, y=170)
    input4 = Entry(emp, width=10)
    input4.place(x=630, y=172)


    lable5 = Label(emp, text='Aadhaar no !: *', font=('arial', 12))
    lable5.place(x=77, y=240)
    input5 = Entry(emp, width=22)
    input5.place(x=250, y=242)


   
    lable5 = Label(emp, text='Create Password !: *', font=('arial', 12))
    lable5.place(x=28, y=300)
    input5 = Entry(emp, width=22)
    input5.place(x=250, y=300) 

    lable5 = Label(emp, text='Designation: *', font=('arial', 12))
    lable5.place(x=490, y=240)
    
    def select(event):
        mylable=Label(emp, text=clicked.get(),font=('',10)).place(x=632, y=280)

    options = ["   Staff","Docter"]
    clicked = StringVar()
    clicked.set(options[0])
    Drop = OptionMenu(emp, clicked, *options, command=select)
    Drop.place(x=630, y=235)


    button = Button(emp, text='Sign_up',font=('ariel',12), fg='blue')
    button.place(x=350, y=400)


    """lis=["Staff","Docter"]
    clicked = StringVar()
    clicked.set('Staff')
    options.config(font=('',14))
    options = OptionMenu(emp, clicked,*lis)
    
    options.place(x=630, y=235)"""
    

    
    
mw.mainloop()

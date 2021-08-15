from Tkinter import *
from subprocess import call
from PIL import Image, ImageTk
import sqlite3


mw = Tk()
mw.geometry("1270x630+0+0")
mw.title('KMR Hospital')
mw.iconbitmap("images/uni.ico")


#creating frame for hospital icon

frame = LabelFrame(mw)
frame.pack()
img = ImageTk.PhotoImage(Image.open("images/kmr.jpg"))
im = Label(frame, image=img).pack()

#creating navicon and buttons inside

def navi():
    sign_in = Tk()
    sign_in.iconbitmap("images/uni.ico")
    sign_in.title("KMR Hospital")
    sign_in.geometry("400x260+800+80")
    sign_in.resizable(False, False)
    
    lable=Label(sign_in, text='only Employee use', font=('ariel', 14), bg='orange')
    lable.place(x=110, y=15)
    
    
    
    lable1=Label(sign_in, text="User_name !", font=('ariel', 10))
    lable1.place(x=25, y=80)
    user_input=Entry(sign_in, width=25)
    user_input.place(x=140, y=80)

    lable1=Label(sign_in, text="Password !", font=('ariel', 10))
    lable1.place(x=38, y=130)
    user_input1 = Entry(sign_in, width=25)
    user_input1.place(x=140, y=130)
    user_input1.config(show="*")

    
    print_records =''
    def ok():
        user_name=user_input.get()
        password=user_input1.get()
        
        
        if (user_name==""and password==""):
            print("","Blank not allowed")
            return False

        elif(user_name=="kmr"and password=="admin"):
            print("","Login SuccessfullY")
            sign_in.destroy()
            #call(["python","patient details.py"])
            call(["python","second_window.py"])
            
            return True

        else:
            print("","Incorrect Username and password")
            return True
           
    """lable2=Label(sign_in, text=ok)
    lable2.place(x=30,y=250)"""
    
    button = Button(sign_in, text='Log_in', font=('ariel', 12), fg='blue',command=ok)
    button.place(x=170, y=190)

    
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

text_hd=Label(text_frame, text="COVID-19 vaccines",fg="white" ,bg='#07b7e3',font=('atial',14)).place(x=170,y=10)
text_hd1=Label(text_frame, text="Equitable access to safe and effective vaccines is critical to ending \n the COVID-19 pandemic, so it is hugely encouraging to see so \n many vaccines proving and going into development. WHO is \n working tirelessly with partners to develop, manufacture \n and deploy safe and effective vaccines.",font=('atial',10))
text_hd1.place(x=20,y=55)

text_hd1=Label(text_frame, text="Safe and effective vaccines are a game-changing tool but for the \n foreseeable future we must continue wearing masks, cleaning \n our hands, ensuring good ventilation indoors, physically \n distancing and avoiding crowds.",font=('atial',10))
text_hd1.place(x=20,y=165)

text_hd1=Label(text_frame, text="Being vaccinated does not mean that we can throw caution to the \n wind and put ourselves and others at risk, particularly because \n research is still ongoing into how much vaccines protect \n not only against disease but also against infection and \n transmission.",font=('atial',10))
text_hd1.place(x=20,y=260)

scroll = Scrollbar(text_frame, orient=VERTICAL, width=30)
scroll.pack(side=RIGHT, fill=Y, padx=5)


mw.mainloop()








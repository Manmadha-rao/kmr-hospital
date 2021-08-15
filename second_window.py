from Tkinter import *

import sqlite3
mw = Tk()
mw.geometry("660x150+550+5")
mw.title('KMR Hospital')
mw.iconbitmap("images/uni.ico")

conn = sqlite3.connect("kmrhospital.db")

cur=conn.cursor()
#cur.execute("""Create table EmployeeDetails(
            #'Name' text,
            #'DOB' integer,
            #'Employee Id no' text,
            #'Date of Joining' integer,
            #'Aadhaar no' integer,
            #'Designation' text)""")

conn.commit()
cur.close()
    
def chi():
    emp = Tk()
    emp.title("KMR Hospital")
    emp.iconbitmap("images/uni.ico")
    emp.geometry("780x480+10+10")
    emp.resizable(False, False)

    lable=Label(emp, text='Enter the Employee Details', font=('arial', 15), bg="green")
    lable.place(x=250, y=20)
    
    lable1=Label(emp, text='Name: *', font=('arial', 12))
    lable1.place(x=136, y=100)
    input1 = Entry(emp, width=20, font=('arial', 10))
    input1.place(x=250, y=102)


    lable2=Label(emp, text='Date of Birth: *', font=('arial', 12))
    lable2.place(x=480, y=100)
    input2 = Entry(emp, width=10)
    input2.place(x=630, y=102)


    lable3 = Label(emp, text='Employee Id no !: *', font=('arial', 12))
    lable3.place(x=40, y=170)
    input3 = Entry(emp, width=22)
    input3.place(x=250, y=172)


    lable4 = Label(emp, text='Date of Joining: *', font=('arial', 12))
    lable4.place(x=462, y=170)
    input4 = Entry(emp, width=10)
    input4.place(x=630, y=172)

    lable5 = Label(emp, text='Aadhaar no !: *', font=('arial', 12))
    lable5.place(x=77, y=240)
    input5 = Entry(emp, width=22)
    input5.place(x=250, y=242)

    lable6 = Label(emp, text='Designation: *', font=('arial', 12))
    lable6.place(x=490, y=240)
    input6 = Entry(emp, width=10)
    input6.place(x=630, y=240)
    lable=Label(emp, text="enter above docter/staff").place(x=500,y=270)


    def sign_up():
        conn = sqlite3.connect("kmrhospital.db")

        cur=conn.cursor()
    
        cur.execute("insert into EmployeeDetails values(:Name,:DOB,:Employee_Idno,:Date_ofJoining,:Aadhaar_no,:Designation)",{
                    'Name':input1.get(),
                    'DOB':input2.get(),
                    'Employee_Idno':input3.get(),
                    'Date_ofJoining':input4.get(),
                    'Aadhaar_no':input5.get(),
                    'Designation':input6.get()
                    })

        conn.commit()
        conn.close()
        input1.delete(0,END)
        input2.delete(0,END)
        input3.delete(0,END)
        input4.delete(0,END)
        input5.delete(0,END)
        input6.delete(0,END)


    def viewdetails():

       conn = sqlite3.connect("kmrhospital.db")
       cur=conn.cursor()

       cur.execute("select *,oid from EmployeeDetails")
       rec=cur.fetchall()
       print(rec)
       print_records=''
       for r in rec[-1]:
           print_records += str(r) + "\n\n"

       rao=Tk()
       rao.geometry("410x480+800+5")
       rao.title('KMR Hospital')
       rao.iconbitmap("images/uni.ico")
       la=Label(rao,text=print_records)
       la.place(x=250,y=80)
 

       la1=Label(rao,text="Employee Details",font=('arial', 15)).place(x=100,y=30)

       la=Label(rao,text="Name  :---").place(x=114,y=80)
       la=Label(rao,text="Date of Birth  :---").place(x=70,y=120)
       la=Label(rao,text="Employee Id no  :---").place(x=50,y=160)
       la=Label(rao,text="Date of Joining  :---").place(x=51,y=200)
       la=Label(rao,text="Aadhaar no  :---").place(x=75,y=240)
       la=Label(rao,text="Designation  :---").place(x=72,y=280)
       la=Label(rao,text="Serial No  :---").place(x=87,y=320)

       butt=Button(rao,text="OK",font=("arial",14),fg="blue",command=rao.destroy).place(x=200,y=400)
       rao.mainloop()

       conn.commit()
       conn.close()
    

    button2 = Button(emp, text='Register',font=('ariel',12), fg='blue',command=sign_up)
    button2.place(x=280, y=400)

    button1 = Button(emp, text='View Details',font=('ariel',12), fg='blue',command=viewdetails)
    button1.place(x=400, y=400)
    labl=Label(emp, text='Press the view details button after save ')
    labl.place(x=400,y=440)  
    
button1 = Button(mw, text='Enter the Employee Details',font=('ariel',14), fg='blue',command=chi)
button1.place(x=50, y=50)

#creating a table for patient details

conn = sqlite3.connect("kmrhospital.db")

cur=conn.cursor()
#cur.execute("""Create table PatientDetails(
            #'Name' text,
            #'Age' integer,
            #'Ph No' text,
            #'Gender' integer,
            #'Address' text,
            #'Postal Pin' integer,
            #'Health card No' integer,'Id No' text,
            #'Blood group' text,'Reference' text)""")

conn.commit()
cur.close()

def patient():
    mainwindow = Tk()
    mainwindow.title("KMR Hospital")
    mainwindow.iconbitmap("images/uni.ico")
    mainwindow.geometry("780x580+10+10")
    mainwindow.resizable(False, False)

    lable=Label(mainwindow, text='Enter the Patient Details', font=('arial', 15), bg='red')
    lable.place(x=250, y=30)

    lable1=Label(mainwindow, text='Name: *', font=('arial', 12))
    lable1.place(x=85, y=100)
    name_input1=Entry(mainwindow, width=20, font=('arial', 10))
    name_input1.place(x=180,y=105)

    lable2=Label(mainwindow, text='Age: *', font=('arial', 12))
    lable2.place(x=450,y=100)
    name_input2= Entry(mainwindow ,width=7)
    name_input2.place(x=550,y=105)
    lable2=Label(mainwindow, text='years')
    lable2.place(x=630,y=100)

    lable3=Label(mainwindow, text='Ph No: *', font=('arial',12))
    lable3.place(x=85,y=160)
    name_input3=Entry(mainwindow, width=22)
    name_input3.place(x=180,y=165)

    lable4=Label(mainwindow, text='Gender: *', font=('arial', 12))
    lable4.place(x=450,y=160)
    name_input4= Entry(mainwindow, width=6, font=('arial', 10))
    name_input4.place(x=550,y=165)
    
    lable5=Label(mainwindow, text='Address: *', font=('arial', 12))
    lable5.place(x=70,y=220)
    name_input5=Entry(mainwindow, width=52, font=('arial', 10))
    name_input5.place(x=180, y=225)


    lable6=Label(mainwindow, text='Postal Pin: *', font=('arial', 12))
    lable6.place(x=60,y=280)
    name_input6=Entry(mainwindow, width=22)
    name_input6.place(x=180,y=285)


    lable7=Label(mainwindow, text='Health card No:', font=('arial', 12))
    lable7.place(x=30,y=340)
    name_input7= Entry(mainwindow, width=20, font=('arial', 10))
    name_input7.place(x=180,y=345)

    
    lable8=Label(mainwindow, text='Id No(If any): *', font=('arial', 12))
    lable8.place(x=40,y=400)
    name_input8= Entry(mainwindow, width=20, font=('arial', 10))
    name_input8.place(x=180,y=405)

    lable9=Label(mainwindow, text='Blood group:', font=('arial', 12))
    lable9.place(x=420,y=340)
    name_input9=Entry(mainwindow, width=7)
    name_input9.place(x=550,y=345)

    lable10=Label(mainwindow, text='Reference:', font=('arial', 12))
    lable10.place(x=420,y=400)
    name_input10=Entry(mainwindow, width=20)
    name_input10.place(x=545, y=405)

    """lable10=Label(mainwindow, text='Reference:', font=('arial', 12))
    lable10.place(x=60,y=460)
    name_input10=Entry(mainwindow, width=22)
    name_input10.place(x=180, y=465)"""


    def save():

        conn = sqlite3.connect("kmrhospital.db")

        cur=conn.cursor()
    
        cur.execute("insert into PatientDetails values(:Name,:age,:Ph_No,:Gender,:Address,:Postal_Pin,:Healthcard_No,:Id_No,:Blood_group,:Reference)",{
                    'Name':name_input1.get(),
                    'age':name_input2.get(),
                    'Ph_No':name_input3.get(),
                    'Gender':name_input4.get(),
                    'Address':name_input5.get(),
                    'Postal_Pin':name_input6.get(),
                    'Healthcard_No':name_input7.get(),
                    'Id_No':name_input8.get(),
                    'Blood_group':name_input9.get(),
                    'Reference':name_input10.get()
                    })

        conn.commit()
        conn.close()
        name_input1.delete(0,END)
        name_input2.delete(0,END)
        name_input3.delete(0,END)
        name_input4.delete(0,END)
        name_input5.delete(0,END)
        name_input6.delete(0,END)
        name_input7.delete(0,END)
        name_input8.delete(0,END)
        name_input9.delete(0,END)
        name_input10.delete(0,END)

    def view():

       conn = sqlite3.connect("kmrhospital.db")
       cur=conn.cursor()

       cur.execute("select *,oid from PatientDetails")
       rec=cur.fetchall()
       print(rec)
       print_records=''
       for r in rec[-1]:
           print_records += str(r) + "\n\n"

       rao=Tk()
       rao.geometry("780x600+10+5")
       rao.title('KMR Hospital')
       rao.iconbitmap("images/uni.ico")
       la=Label(rao,text=print_records)
       la.place(x=250,y=80)

       la1=Label(rao,text="Employee Details",font=('arial', 15)).place(x=200,y=30)

       la=Label(rao,text="Name  :---").place(x=140,y=80)
       la=Label(rao,text="Age  :---").place(x=152,y=120)
       la=Label(rao,text="Phone No  :---").place(x=115,y=160)
       la=Label(rao,text="Gender  :---").place(x=132,y=200)
       la=Label(rao,text="Address  :---").place(x=126,y=240)
       la=Label(rao,text="Postal Pin  :---").place(x=115,y=280)
       la=Label(rao,text="Health card No  :---").place(x=77,y=320)
       la=Label(rao,text="Id No(If any)  :---").place(x=95,y=360)
       la=Label(rao,text="Blood group  :---").place(x=94,y=400)
       la=Label(rao,text="Reference  :---").place(x=113,y=440)
       la=Label(rao,text="Serial No  :---").place(x=117,y=480)

       butt=Button(rao,text="OK",font=("arial",14),fg="blue",command=rao.destroy).place(x=350,y=520)
       

       rao.mainloop()

       conn.commit()
       conn.close()

    button1 = Button(mainwindow, text='Save',font=('ariel',14), fg='blue',command=save)
    button1.place(x=300, y=480)

    button1 = Button(mainwindow, text='View',font=('ariel',14), fg='blue',command=view)
    button1.place(x=400, y=480)
    labl=Label(mainwindow, text='Press the view button after save ')
    labl.place(x=400,y=540)    


    

button1 = Button(mw, text='Enter the Patient Details',font=('ariel',14), fg='blue',command=patient)
button1.place(x=350, y=50)



mw.mainloop()


















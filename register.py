from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector

#==============================================registration page==========================================

win = Tk()
win.title("Registration page")
win.geometry("1500x800")
f1=Frame(win,bg="cyan3",padx=20,pady=50,borderwidth=33,relief=SUNKEN)
f1.grid(row=1,column=5)

# ===========================================functions=======================================================================================================

#=================================================heading=======================================================================================================
Label(win,bg="cyan3",fg="crimson",text="Welcome",font=("Times 30 bold italic"),borderwidth=30,relief=SUNKEN,padx=70,pady=15).grid(row=0,column=4)
Label(win,bg="cyan3",fg="crimson",text="Cafe",font=("Times 30 bold italic"),borderwidth=30,relief=SUNKEN,padx=70,pady=15).grid(row=0,column=7)
#========================================= text for our form =========================================================================================
heading=Label(f1,bg="cyan3",text="Welcome To Our Cafe",font=("Times 30 bold italic"),fg="black").grid(row=0,column=4)
name =Label(f1,text="Username:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
Phone =Label(f1,text="Phone:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
# Gender =Label(f1,text="Gender:",bg="cyan3",fg="white",font=("Times 20 bold italic"))
Email =Label(f1,text="Email:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
Password =Label(f1,text="Password:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
# Password.config(show="*")
ConfirmPassword =Label(f1,text="Confirm Password:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
# ConfirmPassword.config(show="*")
Payment =Label(f1,text="Payment Mode:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
#================================== packing text for our form==============================================================================
name.grid(row=1,column=3)
Phone.grid(row=2,column=3)
# Gender.grid(row=3,column=3)
Email.grid(row=3,column=3)
Password.grid(row=4,column=3)
ConfirmPassword.grid(row=5,column=3)
Payment.grid(row=6,column=3)
#=============================== tkinter variables for storing entries====================================
namevalue = StringVar() #deta base
Phonevalue = StringVar()
# var = StringVar()
# var.set(0)
Emailvalue = StringVar()
Passwordvalue = StringVar() #detabase
ConfirmPasswordvalue = StringVar()
Paymentvalue = StringVar()
foodservicevalue = IntVar()
#==================================== Entries  for our form===============================================
nameentry =Entry(f1,textvariable=namevalue)
Phoneentry =Entry(f1,textvariable=Phonevalue)
# b1 = Radiobutton(f1,text="Male",value="Male",variable=var,bg="cyan3",fg="white",font="Helvetica 16 bold")
# b2 = Radiobutton(f1,text="Female",value="Female",variable=var,bg="cyan3",fg="white",font="Helvetica 16 bold")
Emailentry =Entry(f1,textvariable=Emailvalue)
Passwordentry = Entry(f1,textvariable=Passwordvalue)
ConfirmPasswordentry = Entry(f1,textvariable=ConfirmPasswordvalue)

Paymententry =Entry(f1,textvariable=Paymentvalue)

# =======================================packing the entry================================================
nameentry.grid(row=1,column=4)
Phoneentry.grid(row=2,column=4)
# b1.grid(row=3,column=4)
# b2.grid(row=3,column=5)
Emailentry.grid(row=3,column=4)
Passwordentry.grid(row=5,column=4)
ConfirmPasswordentry.grid(row=4,column=4)

Paymententry.grid(row=6,column=4)


def clearEnrtyBox():
    pass
def insert():

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")
        mycursor = mydb.cursor()
        insert = ("INSERT INTO login (name,phone,email,password,confirmpassword,payment) VALUES  (%s,%s,%s,%s,%s,%s)")
        values = [namevalue.get(),Phonevalue.get(),Emailvalue.get(),Passwordvalue.get(),ConfirmPasswordvalue.get(),Paymentvalue.get()]
        mycursor.execute(insert,values)
        # if Passwordvalue.get()==ConfirmPasswordvalue.get():
        mydb.commit()
        tmsg.showinfo(title="done", message=" Your Account is created Successfully")
        ok=namevalue.set(""),Phonevalue.set(""),Emailvalue.set(""),Passwordvalue.set(""),ConfirmPasswordvalue.set(""),Paymentvalue.set("")
        win.destroy()
        import twoinone.py
        # else:
        #     tmsg.showinfo(title="wrong", message="Account  not created ")

   
#================================================bg color===============================================

win.configure(bg="cyan3")
#======================================= button & paccking it and assigning it a command===============
Button(f1,text="Sign Up",command=insert,font=("Times 20 bold italic"),bg="green",fg="black",).grid(row=7,column=4)
win.mainloop()

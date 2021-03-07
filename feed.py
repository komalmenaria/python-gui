from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector
f_root=Tk()
f_root.geometry("800x350")
F1=Frame(f_root, bg="cyan3",padx=10, pady=10, borderwidth=15, relief=SUNKEN )
F1.grid(row=0,column=0)

#COMMANDS
def getvals():

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")
        mycursor = mydb.cursor()
        insert = ("INSERT INTO feedback (name,email,comment) VALUES  (%s,%s,%s)")
        values = [namevar.get(),emailvar.get(),commentvar.get()]
        mycursor.execute(insert,values)
        # if Passwordvalue.get()==ConfirmPasswordvalue.get():
        mydb.commit()
        tmsg.showinfo(title="done", message=" Thank you for visiting ")

    

#Form text
flabel=Label(F1,text="Customer Feedback",bg="cyan3",fg="white",font=("Times 30 bold italic"))
flabel.grid(row=1,column=4)
flabel1=Label(F1,text="Please give your feedback",bg="cyan3",fg="red",font=("Times 20 bold italic"))
flabel1.grid(row=3,column=4)
#name and email label
name=Label(F1,text="Name",bg="cyan3",fg="white",font=("Times 20 bold italic"))
email=Label(F1,text="E-mail",bg="cyan3",fg="white",font=("Times 20 bold italic"))
Com=Label(F1,text="Comment",bg="cyan3",fg="white",font=("Times 20 bold italic"))
#packing 
name.grid(row=5,column=4,sticky=NW,padx=100)
email.grid(row=6,column=4,sticky=NW,padx=100)
Com.grid(row=7,column=4)

#var for entry
namevar=StringVar()
emailvar=StringVar()
commentvar=StringVar()

#entry
name_entry=Entry(F1,textvariable=namevar,width=30)
email_entry=Entry(F1,textvariable=emailvar,width=30)
comm_entry=Entry(F1,textvariable=commentvar,width=50, font=("Times 20 bold italic"))

#packing entry
name_entry.grid(row=5,column=4)
email_entry.grid(row=6,column=4)
comm_entry.grid(row=8,column=4,sticky=E)

#Button 
b1=Button(F1,text="Submit",bg="Green",fg="black",font=("lucida 15 bold italic"),command=getvals)
b1.grid(row=9,column=4,pady=10)
b2=Button(F1,text="Exit",bg="Green",fg="black",font=("lucida 15 bold italic"),command=f_root.destroy)
b2.grid(row=9,column=5,pady=10)




f_root.mainloop()
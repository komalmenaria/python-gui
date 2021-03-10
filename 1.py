from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector
 
roote =Tk()
roote.title("login page")
roote.geometry("1500x800")


#========================function============================================================
# def value():
    

def newpage():
    roote.destroy()
    import register.py
def value():
  try:
      mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")
  except:
      print("you are not connected to server ")
  else:
      print("connection succsful")
      email=userentryvalue.get()
      seq=passentryvalue.get()
      mycursor = mydb.cursor()
      query =  "SELECT name,password FROM login"
      mycursor.execute(query)
      # myresult = mycursor.fetchall()
      for (name,password) in mycursor:
          if email==name and seq==password:
              login=True
              print("loginn succes")
              tmsg.showinfo(title="Done", message="You are logged in")
              roote.destroy()
              import twoinone.py
              break
          else:
              login=False
              print("logged in failed")
            #   tmsg.showinfo(title="Error", message="Failed to login ")







    # tmsg.showinfo("Notification",f" Hello  {userentryvalue.get()} you successfully loged In")
# =============================================heading====================================================
Label(roote,text="Welcome To Our Cafe",bg="cyan3",fg="crimson",font=("Times 30 bold italic"),anchor="ne").grid(pady=40,row=0,column=3,ipadx=200)
#========================================frame image======================================================
Image=Image.open("Restaurant.jpg")
Image = Image.resize((300,300))
photo=ImageTk.PhotoImage(Image)
lable1=Label(image=photo,)
lable1.grid(row=2,column=2,columnspan=3,rowspan=5)

# login input
#database
userentryvalue = StringVar()
passentryvalue=StringVar()




#========================================= entry widgets==========================================
f2 = Frame(roote).grid(row=3,column=4)
l1=Label(f2,text="Login Here ",fg="crimson",bg="cyan3",font=("Times 25 bold italic")).grid(row=3,column=4)
Label(f2,text="Username ",fg="crimson",bg="cyan3",font=("Times 20 bold italic")).grid(row=4,column=4)
userentry=Entry(f2,font=("Times 15 bold italic"),textvariable=userentryvalue)
userentry.grid(row=4,column=5)
Label(f2,text="Password ",fg="crimson",bg="cyan3",font=("Times 20 bold italic")).grid(row=5,column=4)
ent1=Entry(f2,font=("Times 15 bold italic"),textvariable=passentryvalue)
ent1.grid(row=5,column=5)
ent1.config(show="*")


#=========================================login / signin button======================================
Button(f2,text="Login",bg="green",font=("Times 20 bold italic"),command=value).grid(row=6,column=4)   
Button(f2,text="SignIn",bg="green",font=("Times 20 bold italic"),command=newpage).grid(row=6,column=5)
roote.configure(bg="cyan3")
roote.mainloop()
#=============================================login page end=========================================



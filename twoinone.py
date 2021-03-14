from tkinter import*
import random
import time
# from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector


root = Tk()
root.geometry("1600x700+0+0")
root.title("Cafe Management System")


Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN,bg="cyan3")
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN,bg="cyan3")
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops,font=("Times   30  italic bold"),bg="cyan3",text="Cafe Management System",fg="crimson",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=("Times   30  italic bold"),text=localtime,fg="black",anchor=W,bg="cyan3")
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
# text_Input=StringVar()
# operator =""

# txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
# txtdisplay.grid(columnspan=4)


def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=eval(operator)

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service=str('%.2f'% Ser_Charge)
    OverAllCost=str( PayTax + Totalcost + Ser_Charge)
    PaidTax=str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
    
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")
    mycursor = mydb.cursor()
    insert = ("INSERT INTO  bils (orde,fries,lunch,burger,pizza,cheese,drinks,cost,servicecharge,tax,subtotal,total) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    values = [rand.get(),Fries.get(),Largefries.get(),Burger.get(),Filet.get(),Cheese_burger.get(),(Drinks.get()),cost.get(),Service_Charge.get(),Tax.get(),Subtotal.get(),Total.get()]
    mycursor.execute(insert,values)
    print(values)
    mydb.commit()
    tmsg.showinfo("Notification","Your order is received")

rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Cheese_burger = StringVar()
Drinks = StringVar()
cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

# btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="grey58", command=lambda: btnclick(7) )
# btn7.grid(row=2,column=0)

# btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="grey58", command=lambda: btnclick(8) )
# btn8.grid(row=2,column=1)

# btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="grey58", command=lambda: btnclick(9) )
# btn9.grid(row=2,column=2)

# Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="grey58", command=lambda: btnclick("+") )
# Addition.grid(row=2,column=3)
# #---------------------------------------------------------------------------------------------
# btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="grey58", command=lambda: btnclick(4) )
# btn4.grid(row=3,column=0)

# btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="grey58", command=lambda: btnclick(5) )
# btn5.grid(row=3,column=1)

# btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="grey58", command=lambda: btnclick(6) )
# btn6.grid(row=3,column=2)

# Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="grey58", command=lambda: btnclick("-") )
# Substraction.grid(row=3,column=3)
# #-----------------------------------------------------------------------------------------------
# btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="grey58", command=lambda: btnclick(1) )
# btn1.grid(row=4,column=0)

# btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="grey58", command=lambda: btnclick(2) )
# btn2.grid(row=4,column=1)

# btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="grey58", command=lambda: btnclick(3) )
# btn3.grid(row=4,column=2)

# multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="grey58", command=lambda: btnclick("*") )
# multiply.grid(row=4,column=3)
# #------------------------------------------------------------------------------------------------
# btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="grey58", command=lambda: btnclick(0) )
# btn0.grid(row=5,column=0)

# btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="grey58", command=clrdisplay)
# btnc.grid(row=5,column=1)

# btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="grey70",command=eqals)
# btnequal.grid(columnspan=4)

# Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="grey58", command=lambda: btnclick(".") )
# Decimal.grid(row=5,column=2)

# Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="grey58", command=lambda: btnclick("/") )
# Division.grid(row=5,column=3)



#---------------------------------------------------------------------------------------





lblreference = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Order No.",fg="crimson",bg="cyan3",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)



lblfries = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Fries Meal",fg="crimson",bg="cyan3",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)



lblLargefries = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Lunch Meal",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Burger Meal",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Pizza Meal",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'Times' ,20, 'italic bold' ),bg="cyan3",text="Cheese burger",fg="crimson",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Drinks",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="cost",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1,font=( 'Times' ,20, 'italic bold' ),bg="cyan3",text="Service Charge",fg="crimson",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'Times' ,20, 'italic bold' ),text="Tax",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=( 'Times' ,20, 'italic bold' ), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1,font=( 'Times' ,20, 'italic bold' ),text="Subtotal",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,20,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1,font=( 'Times' ,20, 'italic bold' ),text="Total",bg="cyan3",fg="crimson",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,20,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,fg="white",bg="cyan3")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="green",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="green",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btnprice.grid(row=7, column=0)
root.configure(bg="cyan3")



def feed():
    root.destroy()
    import feed.py
btnfeed = Button(f2,text="Feedback here ==>",fg="green4",bg="yellow",font=('ariel', 20 ,'bold'),command=feed)
btnfeed.grid(columnspan=3)
root.mainloop()
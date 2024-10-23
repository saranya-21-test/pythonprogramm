'''Write a python program using tkinter for
withdraw money from the ATM
business conditions:
balance=10000
daily_limit=20000
i. withdrawal amount <=balance
ii. withdrawl notes should be multiples of 100
iii. daily limit should not be exceeded '''

from tkinter import *
from tkinter import messagebox



w=Tk()
w.title("ATM")
w.config(bg="purple")
w.geometry("250x300")


def withdraw():
    balance=int(e1.get())
    daily_limit=20000
    if balance<=daily_limit:
        messagebox.showinfo("RESULT","TAKE YOUR MONEY")
    elif balance%100==0 and balance<=daily_limit:
        messagebox.showinfo("RESULT","TAKE YOUR NOTES")
    else:
        messagebox.showinfo("RESULT"," daily limit should be Over")

def check_balance():
    balance=int(e1.get())
    total_amnt=int(e2.get())
    daily_limit=20000
    if balance<=daily_limit:
        messagebox.showinfo("BALANCE",total_amnt-balance)
    else:
        messagebox.showinfo("RESULT","DAILY LIMIT SHOULD BE OVER")




l1=Label(w,text="ENTER THE BALANCE")
l1.grid(row=0,column=0)
e1=Entry(w)
e1.grid(row=0,column=1)
l2=Label(w,text="TOTAL_BALANCE")
l2.grid(row=1,column=0)
e2=Entry(w)
e2.grid(row=1,column=1)
b1=Button(w,text="Checkbalance",command=check_balance)
b1.grid(row=2,column=0)
b2=Button(w,text="withdraw",command=withdraw)
b2.grid(row=2,column=1)



w.mainloop()
'''write a python program using tkinter for checking customer
is eligible for discount or not
business condition:
inputs: purchase_amt
        membership= True or False
purchase_amt>5000 or membership==True: 20% discount avail'''

from tkinter import*
from tkinter import messagebox
w=Tk()
w.title("DISCOUNT")
w.config(bg="gray")
w.geometry("250x300")
def discount_eligibility():
    purchase_amount=int(e1.get())
    membership=True
    if purchase_amount>5000 and membership==True:
        messagebox.showinfo("discount details","you will get 20% discount")
    else:
        messagebox.showinfo("Discount details ","your not get any discount")

l1=Label(w,text="Total Purchase Amount")
l1.grid(row=0,column=0)
e1=Entry(w)
e1.grid(row=0,column=1)

b1=Button(w,text="Discount",command=discount_eligibility)
b1.grid(row=2,column=1)

w.mainloop()
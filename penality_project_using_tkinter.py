#write python program using tkinter to check speed of the car and give warning penality if the speed exceeded
#speed_limit=90kmph
#i.speed<=speed_limit:no penality
#i.speed<=speed_limit+20:warning
#ii.speed<=speed_limit+20:penality 2000

from tkinter import*
from tkinter import messagebox

w=Tk()
w.title("fine")
w.config(bg="skyblue")
w.geometry("300x350")

def speed_cal():
    speed=int(e1.get())
    limit=int(e2.get())
    if speed<=limit:
        messagebox.showinfo("WARNING","YOU HAVE GOING TO LIMIT SPEED_LIMIT SO NO PENALITY")
    elif speed<=limit+20:
        messagebox.showinfo("WARNING","YOU GOING TOO SPEED SO TAKE CARE")
    else:
        messagebox.showinfo("WARNING","YOU HAVE CROSSING SPEED LIMIT SO YOU Hve to PAY FINE WITH 2000")


l1=Label(w,text="enter the speed")
l1.grid(row=0,column=0)
e1=Entry(w)
e1.grid(row=0,column=1)
l2=Label(w,text="enter the speed_limit")
l2.grid(row=1,column=0)
e2=Entry(w)
e2.grid(row=1,column=1)
b1=Button(w,text="speed_cal",command=speed_cal)
b1.grid(row=2,column=1)
w.mainloop()

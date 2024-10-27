from tkinter import*
from tkinter import messagebox
w=Tk()
w.title("Student Form")
w.config(bg="lavender")
w.geometry("250x300")
Tops=Frame(w,width=1350,height=50,bd=8,bg="olive")
Tops.pack()
f1=Frame(w,width=600,height=600,bd=8,bg="lavender")
f1.pack(side=LEFT)
f2=Frame(w,width=300,height=700,bd=8,bg="lavender")
f2.pack(side=RIGHT)
fla=Frame(f1,width=600,height=200,bd=8,bg="lavender")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="lavender")
flb.pack(side=BOTTOM)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    w.destroy()
    return

def reset():
  Name.set("")
  dateofbirth.set("")
  phonenumber.set("")
  address.set("")
  email.set("")
  degree.set("")
  department.set("")
  yearofpass.set("")
  txtgeneratecv.delete("1.0",END)

























Name=StringVar()
dateofbirth=StringVar()
phonenumber=StringVar()
address=StringVar()
email=StringVar()
degree=StringVar()
department=StringVar()
yearofpass=StringVar()
generatecv=StringVar()

#label widget
lblinfo=Label(Tops,font=('arial',20,'bold'),text="Student Registeration Form",bd=5,fg="black")
lblinfo.grid(row=0,column=0)
lblname=Label(fla,text="Name",font=('arial','16'),bd='20',fg='black',bg="lavender").grid(row=0,column=0)
lbldateofbirth=Label(fla,text="Date of Birth",font=('arial','16'),bd='20',fg='black',bg='lavender').grid(row=1,column=0)
lblphonenumber=Label(fla,text="Phone number",font=('arial','16'),bd='20',fg='black',bg='lavender').grid(row=2,column=0)
lbladdress=Label(fla,text="Address",font=('arial','16'),bd='20',fg='black',bg="lavender").grid(row=3,column=0)
lblemail=Label(fla,text="Email",font=('arial','16'),bd='20',fg='black',bg='lavender').grid(row=4,column=0)
lbldegree=Label(fla,text="Degree",font=('arial','16'),bd='20',fg='black',bg='lavender').grid(row=5,column=0)
lbldepartment=Label(fla,text="Department",font=('arial','16'),bd='20',fg='black',bg='lavender').grid(row=6,column=0)
lblyearofpass=Label(fla,text="Year Of Pass",font=('arial','16'),bd='20',fg='black',bg='lavender').grid(row=7,column=0)








#Entry widget
etxname=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd=10,width=10,justify='left')
etxname.grid(row=0,column=2)
etxdateofbirth=Entry(fla,textvariable=dateofbirth,font=('arial','16','bold'),bd='10',width="10",justify='left')
etxdateofbirth.grid(row=1,column=2)
etxphonenumber=Entry(fla,textvariable=phonenumber,font=('arial',16,'bold'),bd='10',width='10',justify='left')
etxphonenumber.grid(row=2,column=2)
etxaddress=Entry(fla,textvariable=address,font=('arial',16,'bold'),bd='10',width='10',justify='left')
etxaddress.grid(row=3,column=2)
etxemail=Entry(fla,textvariable=email,font=('arial',16,'bold'),bd='10',width='10',justify='left')
etxemail.grid(row=4,column=2)
etxdegree=Entry(fla,textvariable=degree,font=('arial',16,'bold'),bd='10',width='10',justify='left')
etxdegree.grid(row=5,column=2)
etxdepartment=Entry(fla,textvariable=department,font=('arial',16,'bold'),bd='10',width='10',justify='left')
etxdepartment.grid(row=6,column=2)
etxyearofpass=Entry(fla,textvariable=yearofpass,font=('arial',16),bd='10',width='10',justify='left')
etxyearofpass.grid(row=7,column=2)

#Text widget
generatecv=Label(f2,textvariable=generatecv,font=('arial',21,'bold'),fg="red",bg="powder blue").grid(row=0,column=0)

txtgeneratecv=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtgeneratecv.grid(row=1,column=0)


#button
btngeneratecv=Button(flb,text='Generate CV',padx=10,pady=10,bd=8,font=('arial',7,'bold'),width=6,fg="red",bg="powder blue").grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=10,pady=10,bd=8,font=('arial',7,'bold'),width=6,command=reset,fg="red",bg="powder blue").grid(row=0,column=1)

#btnpayslip=Button(flb,text='View Payslip',padx=10,pady=10,bd=8,font=('arial',7,'bold'),width=6,fg="red",bg="powder blue").grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=10,pady=10,bd=8,font=('arial',7,'bold'),width=6,fg="red",bg="powder blue").grid(row=0,column=3)
#btnquit=Button(flb,text='Quit System',padx=10,pady=10,bd=8,font=('arial',7,'bold'),width=6,command=exit,fg="red",bg="powder blue").grid(row=0,column=4)





w.mainloop()
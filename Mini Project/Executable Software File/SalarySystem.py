import time
import datetime
from tkinter import *
import tkinter.messagebox 
import webbrowser

root=Tk()
root.title("Employee Salary Management System")
root.geometry('675x375+0+0')
root.configure(background="#FFFF00")

Tops=Frame(root,width=675,height=25,bd=4,bg="#CCCC00")
Tops.pack(side=TOP)

f1=Frame(root,width=300,height=300,bd=4,bg="#FFFF00")
f1.pack(side=LEFT)
f2=Frame(root,width=150,height=350,bd=4,bg="#FFFF00")
f2.pack(side=RIGHT)

fla=Frame(f1,width=300,height=100,bd=4,bg="#FFFF00")
fla.pack(side=TOP)
flb=Frame(f1,width=150,height=300,bd=4,bg="#FFFF00")
flb.pack(side=TOP)

#lblinfo=Label(Tops,font=('arial',22,'bold'),text="Employee Salary Management system ",bd=5,fg="black")
#lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee Salary Management System","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  wageshour.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Manager.set("")
  Employee_ID.set("")
  txtpayslip.delete("1.0",END)
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Manager :\t\t"+Manager.get()+"\n\n")
  txtpayslip.insert(END,"EmployeeID :\t\t"+Employee_ID.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n") 
def weeklywages():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(wageshour.get())
  
  paydue=wagesperhours*hoursworkedperweek
  paymentdue="INR",str('%.2f'%(paydue))
  Payable.set(paymentdue)
  
  tax=paydue*0.2
  taxable="INR",str('%.2f'%(tax))
  Taxable.set(taxable)
  
  netpay=paydue-tax
  netpays="INR",str('%.2f'%(netpay))
  NetPayable.set(netpays)
  
  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime="INR",str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs="INR",str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)  
  return  

def callback():
        webbrowser.open_new(r"https://forms.gle/BNLUTUxig62btKCL6") 
def about():
    about=tkinter.messagebox.showinfo("SDUML Mini Project","Team Members:\n E050 Nihal Shetty \n E071 Arya Shah \n Mentor: Dr. Shubha Puthran")
    
    
#=============================== Variables ========================================================
Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OverTimeBonus=StringVar()
Manager=StringVar()
Employee_ID=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#================================ Label Widget =================================================

lblName=Label(fla,text="Name",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=0,column=0)
lblAddress=Label(fla,text="Address",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=0,column=2)
lblManager=Label(fla,text="Manager",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=1,column=0)
lblEmployee_ID=Label(fla,text="EmployeeID",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=1,column=2)
lblHoursWorked=Label(fla,text="Hours Worked",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=2,column=0)
lblHourlyRate=Label(fla,text="Hourly Rate",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=2,column=2)
lblTax=Label(fla,text="Tax",font=('arial',8,'bold'),bd=10,anchor='w',fg="black",bg="#FFFF00").grid(row=3,column=0)
lblOverTime=Label(fla,text="OverTime",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=3,column=2)
lblGrossPay=Label(fla,text="GrossPay",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=4,column=0)
lblNetPay=Label(fla,text="Net Pay",font=('arial',8,'bold'),bd=10,fg="black",bg="#FFFF00").grid(row=4,column=2)

#=============================== Entry Widget =================================================

etxname=Entry(fla,textvariable=Name,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxname.grid(row=0,column=1)

etxaddress=Entry(fla,textvariable=Address,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxaddress.grid(row=0,column=3)

etxmanager=Entry(fla,textvariable=Manager,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxmanager.grid(row=1,column=1)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxnin=Entry(fla,textvariable=Employee_ID,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxnin.grid(row=1,column=3)

etxgrosspay=Entry(fla,textvariable=Payable,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxgrosspay.grid(row=4,column=1)

etxnetpay=Entry(fla,textvariable=NetPayable,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxnetpay.grid(row=4,column=3)

etxtax=Entry(fla,textvariable=Taxable,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxtax.grid(row=3,column=1)

etxovertime=Entry(fla,textvariable=OverTimeBonus,font=('arial',8,'bold'),bd=8,width=22,justify='left')
etxovertime.grid(row=3,column=3)

#=============================== Text Widget ============================================================

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',10,'bold'),fg="black",bg="white").grid(row=0,column=0)
txtpayslip=Text(f2,height=22,width=30,bd=16,font=('arial',6,'bold'),fg="black",bg="white")
txtpayslip.grid(row=0,column=0)

#=============================== buttons ===============================================================

btnsalary=Button(flb,text='Calculate Salary',padx=8,pady=8,bd=4,font=('arial',8,'bold'),width=14,fg="black",bg="#FFFF00",command=weeklywages).grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=8,pady=8,bd=4,font=('arial',8,'bold'),width=14,command=reset,fg="black",bg="#FFFF00").grid(row=1,column=0)

btnpayslip=Button(flb,text='View Payslip',padx=8,pady=8,bd=4,font=('arial',8,'bold'),width=14,command=enterinfo,fg="black",bg="#FFFF00").grid(row=0,column=1)

btnexit=Button(flb,text='Exit System',padx=8,pady=8,bd=4,font=('arial',8,'bold'),width=14,command=exit,fg="black",bg="#FFFF00").grid(row=1,column=1)

btnfeedback=Button(flb,text='Feedback',padx=8,pady=8,bd=4,font=('arial',8,'bold'),width=14,command=callback,fg="black",bg="#FFFF00").grid(row=0,column=2)

btnabout=Button(flb,text='About Us',padx=8,pady=8,bd=4,font=('arial',8,'bold'),width=14,command=about,fg="black",bg="#FFFF00").grid(row=1,column=2)
root.mainloop()



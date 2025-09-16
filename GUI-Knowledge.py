from tkinter import *
from tkinter import ttk  #theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อของโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดของโปรแกรม

L1 = Label (GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=120,y=20)

##########################

def Button2():
    text = 'ตอนนี้มีเงินอยู่ในบัญชี 300 บาท'
    message.showinfo('เงินในบัญชีหลัก',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=50,y=100)
B2 = ttk.Button(FB2,text='เป้าหมายทางการเงินบัญชีหลัก')
B2.pack(ipadx=10,ipady=10)

##########################

def Button3():
    text = 'ตอนนี้มีเงินอยู่ในบัญชี 400 บาท'
    message.showerror('เงินในบัญชีสำรอง',text)

FB3 = Frame(GUI)
FB3.place(x=50,y=200)
B3 = ttk.Button(FB3,text='เป้าหมายทางการเงินบัญชีสำรอง')
B3.pack(ipadx=10,ipady=10)

GUI.mainloop()

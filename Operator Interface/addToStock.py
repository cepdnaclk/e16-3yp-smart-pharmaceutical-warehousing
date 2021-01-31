#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox

conn=mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='Shamra123')
mycursor = conn.cursor()
mycursor.execute("SELECT Max(id) from inventory")
result = mycursor.fetchall()
for r in result:
    id=r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Add New Product",font=('arial 25 bold'),fg='black')
         self.heading.place(x=20,y=0)


         #lables  for the window
         self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
         self.name_l.place(x=20,y=70)

         self.stock_l=Label(master,text="Enter Quantity",font=('arial 18 bold'))
         self.stock_l.place(x=20,y=120)

         self.rackNo_l = Label(master, text="Enter RackNo", font=('arial 18 bold'))
         self.rackNo_l.place(x=20, y=170)

         self.sectionNo_l = Label(master, text="Enter SectionNo", font=('arial 18 bold'))
         self.sectionNo_l.place(x=20, y=220)



        #enteries for window

         self.name_e=Entry(master,width=25,font=('arial 18 bold'))
         self.name_e.place(x=280,y=70)

         self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
         self.stock_e.place(x=280, y=120)

         self.rackNo_e = Entry(master, width=25, font=('arial 18 bold'))
         self.rackNo_e.place(x=280, y=170)

         self.sectionNo_e = Entry(master, width=25, font=('arial 18 bold'))
         self.sectionNo_e.place(x=280, y=220)


         #button to add to the database
         self.btn_add=Button(master,text='Add to Database',width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
         self.btn_add.place(x=420,y=270)

         self.btn_clear=Button(master,text="Clear All Fields",width=18,height=2,bg='red',fg='white',command=self.clear_all)
         self.btn_clear.place(x=250,y=270)

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, **kwargs):
    # get from entries
       self.name = self.name_e.get()
       self.stock = self.stock_e.get()
       self.rackNo = self.rackNo_e.get()
       self.sectionNo = self.sectionNo_e.get()



    # dynamic entries
       if self.name == '' or self.stock == '' or self.rackNo == '' or self.sectionNo == '' :
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
       else:
        mycursor.execute("INSERT INTO inventory (name, stock, rackNo, sectionNo) VALUES(%s,%s,%s,%s)",[self.name,self.stock,self.rackNo,self.sectionNo])
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Successfully added to the database")


    def clear_all(self, *args, **kwargs):
       num = id + 1
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.rackNo_e.delete(0, END)
       self.sectionNo_e.delete(0, END)




root=Tk()
b=Database(root)
root.geometry("700x400+0+0")
root.title("Add Product")
root.mainloop()
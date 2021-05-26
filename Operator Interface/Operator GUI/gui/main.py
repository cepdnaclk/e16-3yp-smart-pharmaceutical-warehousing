from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter as tk
from tkinter import PhotoImage
import PIL
import mysql.connector
from tkinter import *
from PIL import ImageTk ,Image
from tkinter import messagebox

from robotArm import *
from robotAGV import *
from stock import *
from order_status import *
from addToStock import *
from updateStock import *
#from ex import *
from grid_ex import *
from Inventory import *
from new_order import *


root = Tk()
root.title("Operator Interface")

width = 1000
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#00022e")

# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()


def connect():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                        database='inventory_system',
                                        user='root',
                                        password='Shamra123')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def Exit3():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to stop?', icon="warning")
    if result == 'yes':
        tkinter.messagebox.showinfo("Success", "Control Overridden")
#COMPLETE
def ShowLoginForm():
    global loginform
    loginform = Toplevel(bg="#00022e")
    loginform.title("Operator Interface/Login")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

def LoginForm():    #COMPLETE
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=0, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, bd=0, text="Operator Login",fg="white", font=('arial 20 bold'),bg="#00022e")
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600,bg="#00022e")
    MidLoginForm.pack(side=TOP, pady=20)
    lbl_username = Label(MidLoginForm, text="Username:", fg="white",font=('arial', 18), bd=18,bg="#00022e")
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", fg="white",font=('arial', 18), bd=18,bg="#00022e")
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18),bg="#00022e")
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 18), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 18), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", fg="black", font=('arial', 15), command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

def Login(event=None):  #COMPLETE
    global admin_id
    connect()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", font=('arial', 15),fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()

        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()
#COMPLETE
def Logout():
    result = tkMessageBox.askquestion('Operator Interface', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()

def Home():
    global Home,tree,productname,quantity
    Home = Toplevel()
    Home.title("Operator Interface/Home")
    width = 1100
    height = 800
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)

    LeftViewForm = Frame(Home, width=350,bg="#00022e")
    LeftViewForm.pack(side=LEFT, fill=Y)

    lbl_text = Button(LeftViewForm,bd=2, text="Inventory", font=('arial', 30), width = 12,command=inventory)
    lbl_text.place(x=20, y=150)

    lbl_text = Button(LeftViewForm,bd=2, text="Order Status", font=('arial', 30), width = 12,command=ShowOrderStatus)
    lbl_text.place(x=20, y=250)

    lbl_text = Button(LeftViewForm,bd=2, text="AGV", font=('arial', 30), width = 12,command=ShowAGV)
    lbl_text.place(x=20, y=350)

    lbl_text = Button(LeftViewForm,bd=2, text="Robot Arm", font=('arial', 30), width = 12,command=ShowArm)
    lbl_text.place(x=20, y=450)

    lbl_text = Button(LeftViewForm,bd=2, text="Location", font=('arial', 30), width = 12,command=Location)
    lbl_text.place(x=20, y=550)


    RightViewForm = Frame(Home, width=300,bg="#00022e")
    RightViewForm.pack(side=RIGHT, fill=Y)


    size = (200, 200)
    image2 = PIL.Image.open("/home/dell/Desktop/Operator GUI/gui/resources/stop.png")
    r_img2 = image2.resize(size)
    img2 = ImageTk.PhotoImage(r_img2)
    label2 = Button(RightViewForm, image=img2, bg="#00022e",command=Exit3)
    label2.image = img2
    # Position image
    label2.place(x=50, y=320)

    MiddleViewForm = Frame(Home, width=400)
    MiddleViewForm.pack(side=LEFT, fill=Y)

    orderDetails(MiddleViewForm)

    menubar = Menu(Home)
    filemenu1 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Account", menu=filemenu1)
    filemenu1.add_command(label="Logout", command=Logout)
    filemenu1.add_command(label="Exit", command=Exit2)

    Home.config(menu=menubar)
    Home.config()

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

def ViewOrder():
    connect()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()

# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Login", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Account", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root,  relief=SOLID)
Title.pack(pady=50)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Smart Pharmaceutical \n Warehouse Management System", fg="white", font=('arial 40 bold'),bg="#00022e")
lbl_display.pack()

size=(600,500)
image1 = PIL.Image.open("/home/dell/Desktop/Operator GUI/gui/resources/warehouse.png")
r_img2 = image1.resize(size)

test = ImageTk.PhotoImage(r_img2)

label1 = Label(root,image=test,bg="#00022e")
label1.image = test

# Position image
label1.pack()
# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
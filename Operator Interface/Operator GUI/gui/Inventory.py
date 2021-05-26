from tkinter import ttk

import tkinter as tk
import mysql.connector
from addToStock import *
from updateStock import *
from stock import *

def inventory():
    global inventory, tree
    inventory = Toplevel()
    inventory.title("Operator Interface/Home")
    width = 1200
    height = 800
    screen_width = inventory.winfo_screenwidth()
    screen_height = inventory.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    inventory.geometry("%dx%d+%d+%d" % (width, height, x, y))
    inventory.resizable(0, 0)

    LeftViewForm = Frame(inventory, width=450)
    LeftViewForm.pack(side=LEFT, fill=Y)
    RightViewForm = Frame(inventory, width=750,height = 400)
    RightViewForm.pack(side=BOTTOM, fill=Y)
    MiddleViewForm = Frame(inventory, width=750,height = 400)
    MiddleViewForm.pack(side=RIGHT, fill=Y)
    ShowStock(LeftViewForm)
    ShowAddNew(MiddleViewForm)
    ShowUpdate(RightViewForm)
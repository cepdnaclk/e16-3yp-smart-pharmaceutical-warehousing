# Import the module
import json
import math


with open('newOrder.json') as file:
  data = json.load(file)

Dict = {'panadol': (1,6), 'pfizer ': (12,6), 'x medicine':(1,15)}

res = []
for key in Dict.keys() :
    res.append(Dict[key])
print("The list of values is : " +  str(res))

l=len(data["details"])

p= data["details"][0]
#print(p)

a=1
sum = 0
while a<l:
    x = data["details"][a]["Name"]
    y = data["details"][a]["Quantity"]
    print("Product Name : " + x +"      Quantity : " +str(y))
    sum=sum+y
    a=a+1

no_of_agv = math.ceil(sum/4)
print("no_of_agv :  " +str(no_of_agv))

#allocating agv
Dict = {}

c=0
a=1
while c<4 & a<4 :
    x = data["details"][a]["Name"]
# Adding elements one at a time
    Dict['c'] = x
    a=a+1
    c=c+1
    print(Dict)

agvAllocated = {'0': [(1, 6), (11, 6), (12, 6)], '1': [(22, 6), (11, 6), (12, 6)], '2': [(11, 15)], '3': [(12, 6)] }


'''

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getJSON():
    global read_file

    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_json(import_file_path)


browseButton_JSON = tk.Button(text="      Import JSON File     ", command=getJSON, bg='green', fg='white',
                              font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JSON)


def convertToTXT():
    global read_file

    export_file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    read_file.to_csv(export_file_path, index=False)


saveAsButton_TXT = tk.Button(text='Convert JSON to TXT', command=convertToTXT, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_TXT)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
'''
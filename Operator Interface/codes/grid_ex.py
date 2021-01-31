import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 10
        self.columns = 10
        self.cellwidth = 50

        self.cellheight = 50

        self.rect = {}
        for column in range(10):
            for row in range(10):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect")

        self.redraw(1000)

    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="grey")
        for i in range(3):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            item_id = self.rect[row, col]
            self.canvas.itemconfig(item_id, fill="yellow")
        self.after(delay, lambda: self.redraw(delay))

        '''
        arrat4 = [x for x in range(0,10)]
        #print(arrat4)
        for i in range(6):
            ###########
            for j in range(6):
                row = i
                #print(row)
                col = j
                #print(col)
                #################
                print(row, col)
            item_id = self.rect[row,col]

            self.canvas.itemconfig(item_id, fill="yellow")
        self.after(delay, lambda: self.redraw(delay))
        '''

if __name__ == "__main__":
    app = App()
    app.title("Location")
    app.mainloop()
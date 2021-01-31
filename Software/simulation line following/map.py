from cell import *
from time import sleep
import threading

class MAP:
    def __init__(self,X ,Y) -> None:
        self.X = X 
        self.Y = Y
        self.cell_map = []
        for y in range(Y):
            tem = []
            for x in range(X):
                
                tem.append(CELL())
            self.cell_map.append(tem)

    def cell_table(self,X,Y,array):
        k = self.cell_map[Y][X]
        k.table(array = array ) 
        self.cell_x = len(k.Cell[0])
        self.cell_y = len(k.Cell)
    

    def map_rander(self):

        line = []
        for x in range(self.cell_x+3):
            line.append('.')

        self.mega = []
        
        for mapy in range(3):
            tem = []
            for mapx in range(self.X):
                tem.extend(line)
            self.mega.append(tem)

        for mapy in range(self.Y):
            tem = self.cell_map[0][0]
            for y in range(len( tem.Cell)) :
                tem1 = ['.',' ',' ']
                for mapx in range(self.X) :
                    k = self.cell_map[mapy][mapx]
                    z = k.Cell[y]
                    tem1.extend(z)
                tem1.extend([ ' ', ' ', '.'])
                self.mega.append(tem1)

        for mapy in range(self.cell_y-3, self.cell_y):
            tem = []
            for mapx in range(self.X):
                tem.extend(line)
            self.mega.append(tem)

        for x in range(1, (len(self.mega[0])-1)):
            self.mega[1][x] = ' '
            self.mega[2][x] = ' '
            self.mega[len(self.mega)-2][x] = ' '
            self.mega[len(self.mega)-3][x] = ' '

        for y in range(1, (len(self.mega)-1)):
            self.mega[y][1] = ' '
            self.mega[y][2] = ' '

            self.mega[y][len(self.mega[0])-3] = ' '
            self.mega[y][len(self.mega[0])-2] = ' '

    def map_print(self):
        
            self.map_rander()
            
            for y in self.mega:
                for x in y:
                    print(f"{x}", end=' ')
                print()
                
            sleep(1)
        
        #self.cls()
        
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def map_print_thread(self):
        self.print = threading.Thread(target=self.map_print, args=())
        self.print.start()

from colour import *
from time import sleep
import threading

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3



colour = bcolors()

class AGV:
    def __init__(self, MAP, full_map) -> None:
        self.ANGLE = DOWN
        k = u'\u2588'
        N = f"{bcolors.WARNING}{k}{bcolors.OKGREEN}"
        self.N =N
        self.AGV = [[N, N], [N, N]]
        self.MAP = MAP
        #self.line_map = LINE_MAP
        self.X = 5 
        self.Y = 18

        self.line_x = 0
        self.line_y = 0

        self.full_map = full_map

        self.food_print()

        self.agv_cpu = threading.Thread(target=self.cpu, args=())
        self.agv_cpu.start()

    def food_print(self):
        N=self.N
        self.AGV = [[N, N], [N, N]]
        if self.ANGLE == UP:
            self.AGV[0][0] = f"{bcolors.WARNING}{'*'}{bcolors.OKGREEN}"
        elif self.ANGLE == RIGHT:
            self.AGV[0][1] = f"{bcolors.WARNING}{'*'}{bcolors.OKGREEN}"
        elif self.ANGLE == DOWN:
            self.AGV[1][1] = f"{bcolors.WARNING}{'*'}{bcolors.OKGREEN}"
        else :
            self.AGV[1][0] = f"{bcolors.WARNING}{'*'}{bcolors.OKGREEN}"
        
    def agv_print(self):
        self.MAP.Cell[self.Y][self.X] = self.AGV[0][0]
        self.MAP.Cell[self.Y][self.X+1] = self.AGV[0][1]
        self.MAP.Cell[self.Y+1][self.X] = self.AGV[1][0]
        self.MAP.Cell[self.Y+1][self.X+1] = self.AGV[1][1]

    def street(self):
        status = 0
        
        if (self.Y>0) and (self.ANGLE == UP) and (self.MAP.Cell[self.Y-1][self.X] != '.')  :    # UP
            self.Y -= 1
            status = 1
        elif (self.X < len(self.MAP.Cell[0])-3) and (self.ANGLE == RIGHT) and (self.MAP.Cell[self.Y][self.X+1] != '.'): # RIGHT
            self.X +=1
            status = 1
        elif (self.X > 0 ) and (self.ANGLE == LEFT ) and (self.MAP.Cell[self.Y][self.X-1] != '.'): # LEFT
            self.X -=1 
            status = 1
        elif (self.Y < len(self.MAP.Cell)-3) and (self.ANGLE == DOWN) and (self.MAP.Cell[self.Y+1][self.X] != '.'):  # DOWN  
            self.Y += 1
            status = 1
            
        ## map fresh
        
        
        return status

    def turnleft(self):
        if self.ANGLE == UP :
            self.ANGLE = LEFT
        elif self.ANGLE == LEFT :
            self.ANGLE = DOWN
        elif self.ANGLE == DOWN :
            self.ANGLE = RIGHT
        else :
            self.ANGLE = UP

    def turnright(self):
        if self.ANGLE == UP:
            self.ANGLE = RIGHT
        elif self.ANGLE == RIGHT:
            self.ANGLE = DOWN
        elif self.ANGLE == DOWN:
            self.ANGLE = LEFT
        else:
            self.ANGLE = UP

        self.food_print()

    def go_to(self,dst):
        self.dst = dst

    def left_check(self):
        if self.ANGLE == UP:
            ANGLE = LEFT
        elif self.ANGLE == LEFT :
            ANGLE = DOWN
        elif self.ANGLE == DOWN :
            ANGLE = RIGHT
        else :
            ANGLE = UP

        return self.check(ANGLE)

    def right_chech(self):
        if self.ANGLE == UP:
            ANGLE = RIGHT
        elif self.ANGLE == RIGHT :
            ANGLE = DOWN
        elif self.ANGLE == DOWN :
            ANGLE = LEFT
        else :
            ANGLE = UP

        return self.check(ANGLE)

    def check(self,ANGLE):
        
        if ANGLE == UP :
            if (self.MAP.Cell[self.Y-1][self.X] != '.') and (self.MAP.Cell[self.Y-1][self.X+1] != '.'):
                return 1
            else:
                return 0
        elif ANGLE == RIGHT:
            if (self.MAP.Cell[self.Y][self.X+2] != '.') and (self.MAP.Cell[self.Y+1][self.X+2] != '.'):
                return 1
            else:
                return 0
        elif ANGLE == DOWN:
            if (self.MAP.Cell[self.Y+2][self.X] != '.') and (self.MAP.Cell[self.Y+2][self.X+1] != '.'):
                return 1
            else:
                return 0
        elif ANGLE == LEFT:
            if (self.MAP.Cell[self.Y][self.X-1] != '.') and (self.MAP.Cell[self.Y+1][self.X-1] != '.'):
                return 1
            else:
                return 0
            


    def cpu(self):

        while(1):
            self.full_map.cls()
            sleep(1)
            
            if ( self.right_chech() == 1):
                self.turnright()
                self.street()
                
            else:
                end =self.street()
                if end == 0:
                    self.turnright()
            
            self.MAP.cell_render()
            self.agv_print()
            
            self.full_map.map_print()
            

            if (self.X == self.MAP.en_x) and (self.Y == self.MAP.en_y):
                print('break')
                break
                

            
            

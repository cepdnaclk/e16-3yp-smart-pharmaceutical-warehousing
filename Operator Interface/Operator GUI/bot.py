import cv2
import numpy as np
import random
import math
import imgFunctions as img
import time
import map as mp
import collision as col
import driver as driver


counter = 1

# lists and dicts required to construct bot objects and graph
bots = list()
graph = {}
excp_Set = set()

shortestPathtoNodes = {}    # dict to hold shortest path to each node from each node
PathCost = {}               # dict to hold path cost from node to node

#Path_list = []

# parameters required for the GUI
BOT_COUNT = 4
RADI = 50
GRID_SIZE = 30
dS = 0.1
WINDOW_SIZE = 1000  # square window, height = width
CELL_SIZE = WINDOW_SIZE/GRID_SIZE 

backg_H = 0
backg_W = 0
bot_H = 0
bot_W = 0

# boolean flag to signify destination is reached
dest_reached = False

paused = False
set_dest = False


# class to make a bot
class Bot:
    def __init__(self, ID):

        # bot id
        self.ID = ID
    
        global dest_reached
       
        # list to contain path to follow
        self.path = []

        # list that contains orders
        self.orders = []
        
        # wait flag to hold the current position: initially set to false
        self.waitFlag = False

        # flag to indicate assigned order is completed: initially set to false
        self.OrderComplete =  True

        # flag to indicate interim destinations
        self.interim_dest = False
        
        # initial state of the bot : -1: stopped, 0: sucess, 1:moving
        self.state = -1

        # current orientation (from north)
        self.angle = 0
        self.dir = 'N'          # current direction
        self.prev_dir = 'N'     # previous direction

        # initial position of the bot (src of each bot)
        self.init_x = 0
        self.init_y = 0

        # current position & next postion, both initially set to (0,0)
        self.curr_x = 0
        self.curr_y = 0
        self.next_x = 0
        self.next_y = 0
        
        # destination position
        self.dest_x = int(-1)
        self.dest_y = int(-1)

        # IR sensor feedback (only for real bots)
        self.IR_feed = 0   # initially set to zero

        self.currentPosVal = [0,0]
        
    # import images of bots
    def setImgs(self, imgs):
        self.bot_imgs = imgs

    # function to set the current position
    def setPos(self, x, y):

        # check for the overflow of the x , y values over the backgrounf image
        self.curr_x = (bot_W/2 if (x < bot_W/2) else ((backg_W - bot_W/2)
                                                 if x > (backg_W - bot_W/2) else x))
        self.curr_y = (bot_H/2 if (y < bot_H/2) else ((backg_H - bot_H/2)
                                                 if y > (backg_H - bot_H/2) else y))
        #self.angle = angle

    # function to get the current state of the bot : moving, stationary or success
    def getState(self, bots):
        min = WINDOW_SIZE
        for i, bot in enumerate(bots):
            if self.ID != i:
                dist = math.sqrt((self.curr_x - bot.curr_x)*(self.curr_x -
                                                   bot.curr_x) + (self.curr_y - bot.curr_y)*(self.curr_y - bot.curr_y))
                # angle = math.atan((self.y - bot.y)/(self.x - bot.x))
                if min > dist:
                    min = dist

        if min < 100:
            self.state = -1
        else:
            self.state = 0

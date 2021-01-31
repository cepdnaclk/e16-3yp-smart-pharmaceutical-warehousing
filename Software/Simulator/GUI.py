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


'''... following functions are defined outside the Bot class ...'''

# # function to determine orientation
# # arguements: coordinates of current and next positions, previous orientation of the bot
# def orientation(bot):

#     # updates the previous direction
#     bot.prev_dir = bot.dir
        
#     # determines the direction of the next point
#     if(bot.next_x - bot.curr_x)==0 and (bot.next_y-bot.curr_y)>0:
#         bot.dir = 'N'
#     elif(bot.next_x - bot.curr_x)>0 and (bot.next_y-bot.curr_y)==0:
#         bot.dir = 'E'
#     elif(bot.next_x - bot.curr_x)==0 and (bot.next_y-bot.curr_y)<0:
#         bot.dir = 'S'
#     elif(bot.next_x - bot.curr_x)<0 and (bot.next_y-bot.curr_y)==0:
#         bot.dir = 'W'
    
#     # changes the orientation of the bot to advance to next point, depending on the current orientation
        
#     # if the previous direction and the next direction are same, angle does not change
#     if bot.prev_dir == bot.dir:
#         bot.angle = bot.angle
#         #self.prev_dir = self.dir
        
#     # from North
#     # N --> E
#     elif bot.prev_dir == 'N' and bot.dir == 'E':
#         bot.angle = bot.angle + 90
#         #self.prev_dir = self.dir
        
#     # N --> S
#     elif bot.prev_dir == 'N' and bot.dir == 'S':
#         bot.angle = bot.angle + 180
#         #self.prev_dir = self.dir
        
#     # N --> W
#     elif bot.prev_dir == 'N' and bot.dir == 'W':
#         bot.angle = bot.angle - 90
#         #self.prev_dir = self.dir
        
#     # from East
#     # E --> N
#     elif bot.prev_dir == 'E' and bot.dir == 'N':
#         bot.angle = bot.angle - 90
#         #self.prev_dir = self.dir
        
#     # E --> S
#     elif bot.prev_dir == 'E' and bot.dir == 'S':
#         bot.angle = bot.angle + 90
#         #self.prev_dir = self.dir
        
#     # E --> W
#     elif bot.prev_dir == 'W' and bot.dir == 'W':
#         bot.angle = bot.angle + 180
#         #self.prev_dir = self.dir

#     # from South
#     # S --> E
#     elif bot.prev_dir == 'S' and bot.dir == 'E':
#         bot.angle = bot.angle - 90
#         #self.prev_dir = self.dir
        
#     # S --> W
#     elif bot.prev_dir == 'S' and bot.dir == 'W':
#         bot.angle = bot.angle + 90
#         #self.prev_dir = self.dir
        
#     # S --> N
#     elif bot.prev_dir == 'S' and bot.dir == 'N':
#         bot.angle = bot.angle + 180
#         #self.prev_dir = self.dir
        
#     # from West
#     # W --> N
#     elif bot.prev_dir == 'W' and bot.dir == 'N':
#         bot.angle = bot.angle + 90
#         #self.prev_dir = self.dir
        
#     # W --> S
#     elif bot.prev_dir == 'W' and bot.dir == 'S':
#         bot.angle = bot.angle - 90
#         #self.prev_dir = self.dir
        
#     # W --> E
#     elif bot.prev_dir == 'W' and bot.dir == 'E':
#         bot.angle = bot.angle + 180
#         #self.prev_dir = self.dir


# # function to update positions of bots
# # inputs are bot object and path to follow
# def update(bots):
#     global counter
#     if counter%200 == 0:
#         counter = 0
#         #time.sleep(1)
#         # iterate over bots array and update path of all bots
#         for bot in bots:
            
#             # if the path is not empty 
#             if len(bot.path) !=0 and bot.waitFlag == False:
            
#                 bot.next_x = bot.path[0][0][0]
#                 bot.next_y = bot.path[0][0][1]
                
#                 # gets the orientation
#                 orientation(bot)
                    
#                 if(bot.curr_x == bot.dest_x and bot.curr_y == bot.dest_y):
#                     # sends a message to the central server once the destination is reached
#                     #mqtt.send_message("Done")

#                     # set the dest_reached flag to true
#                     bot.dest_reached = True
                        

#                 else:
                    
#                     if(bot.next_x >= bot.curr_x and bot.next_y ==  bot.curr_y): 
#                         # advance to right
#                         bot.curr_x = bot.curr_x + abs((bot.next_x-bot.curr_x))
#                         print(bot.curr_x, bot.curr_y)
                        
                        
#                     elif(bot.next_x < bot.curr_x and bot.next_y == bot.curr_y):
#                         # advance to left  
#                         bot.curr_x = bot.curr_x - abs((bot.curr_x-bot.next_x)) 
#                         print(bot.curr_x, bot.curr_y)
                        
                                        
#                     elif(bot.next_y >= bot.curr_y and bot.next_x == bot.curr_x):
#                         # advance towards +ve Y axis
#                         bot.curr_y = bot.curr_y + abs((bot.next_y-bot.curr_y))
#                         print(bot.curr_x, bot.curr_y)
                        
#                     elif(bot.next_y < bot.curr_y and bot.next_x == bot.curr_x):
#                         # advance towards -ve Y axis
#                         bot.curr_y = bot.curr_y - abs((bot.curr_y-bot.next_y))
#                         print(bot.curr_x, bot.curr_y)
                        
                    
#                     #print(bot.curr_x, bot.curr_y)
#                     # remove the first element from the path array
#                     bot.path[0].pop(0)

#                     # if the bot has reached immediate destination
#                     if not bot.path[0]:
#                         bot.path.pop(0)
#                     #time.sleep(1)
#     counter = counter + 1

""" draw bot images in the overlay canvas
    return : overlay(4 dims with the alpha layer)"""

# function to draw bots on the canvas
def draw_bots(bots):
    # create a overlay layer to draw all the robots with the alpha
    overlay = np.zeros((backg_H, backg_W, 4), dtype="uint8")
    for bot in bots:
        x = bot.curr_x*CELL_SIZE
        y = bot.curr_y*CELL_SIZE

        x = (0 if (x < 0) else ((backg_W - CELL_SIZE)
                                                 if x > (backg_W - CELL_SIZE) else x))
        y = (0 if (y < 0) else ((backg_H - CELL_SIZE)
                                                 if y > (backg_H - CELL_SIZE) else y))

        #print(bot.curr_x, bot.curr_y, x, y)
        angle = bot.angle
        x_start = int(x)
        y_start = int(y)

        #  set the state of the bot acording to the neighbour bots distatnce
        bot.getState(bots)

        # add the additional status color bar to the basic bot png
        if (bot.state == 0) :
            addon = bot.bot_imgs['blue']
        else:
            addon = bot.bot_imgs['red']

        # ---------------------Draw destination lines and rectangles -----------------------
        if bot.dest_x != -1:
            cv2.line(overlay, (int(bot.x), int(bot.y)),
                     (bot.dest_x, bot.dest_y), (0, 200, 200, 255), 2)


            cv2.rectangle(overlay, (bot.dest_x-int(CELL_SIZE), bot.dest_y-int(CELL_SIZE)),
                      (bot.dest_x+int(CELL_SIZE), bot.dest_y+int(CELL_SIZE)), color, 2)

        bot_img = cv2.add(bot.bot_imgs['bot'], addon)
        bot_img = img.rotate_image(bot_img, angle)
        roi = overlay[y_start:y_start+bot_W, x_start:x_start+bot_W]  # region of interest
        overlay[y_start:y_start+bot_W, x_start:x_start+bot_W] = roi + bot_img

    return overlay


if __name__ == "__main__":

    # load backgroug image according to the grid size
    backg_H, backg_W, background = img.loadBackground(GRID_SIZE, WINDOW_SIZE)
    bot_H, bot_W, bot_pngs = img.loadBotImgs(
        GRID_SIZE, WINDOW_SIZE)  # load all pngs of the bot to a dict
    bot_png = bot_pngs['bot']  # get the bot image

    print(backg_H, backg_W)
    print(bot_H, bot_W)

    cv2.namedWindow("image")
#   cv2.setMouseCallback("image", mosueEvent)

    # hard coded order schedulee
    inputSchedule = {'0':[(2,7), (2,16)], '1':[(2,7), (12,7)], '2':[(21,7), (12,16)], '3':[(21,7)]}


    ''' initializes the graph and the grid '''
    
    # adding shelves
    mp.add_shelves(excp_Set,(3,3), (10,10))
    mp.add_shelves(excp_Set,(3,13), (10,20))
    mp.add_shelves(excp_Set,(13,3), (20,10))
    mp.add_shelves(excp_Set,(13,10), (20,20))
    
    # creates the graph
    mp.generate_graph(graph, excp_Set, 31)
    #print(graph[(19, 5)])

    # destination array
    #racks = [[(0,0),(4,10)], [(1,0),(13,19)], [(2,0), (20,20)]]
    #Path_list = [[]for _ in range(BOT_COUNT)]
     
    while True:

        # creates bots images at the initial run
        if len(bots) == 0:
            for i in range(BOT_COUNT):
                imgs = bot_pngs.copy()
                bot = Bot(i)
               
                #bot.setPos(i, 0)
                bot.curr_x = i
                bot.curr_y = 0
                bot.angle = 180
                bot.waitFlag = False
                bot.setImgs(imgs)
                bots.append(bot)
                           
        else:    
            #col.collision(bots)
            #update(bots)

            for bot in bots:
                #print("checked")
                # checks if the assigned order is completed
                #print(bot.ID)
                
                if bot.OrderComplete:
                    driver.setPath(graph, excp_Set, shortestPathtoNodes, PathCost, bot, inputSchedule)

            # callls start function activate bots
            driver.start(bots)  
                    
            # ------------Draw bots ------------------------------
            # get a overlay that contains the vector with aplha which has the current orientation of bots
            overlay = draw_bots(bots)
            # mask the background with the overlay
            masked_backg = cv2.bitwise_and(background, background, mask=cv2.bitwise_not(overlay[:, :, 3]))
            # add the overlay and the background
            finalImg = cv2.add(overlay[:, :, :3], masked_backg)

            # ------------Draw rect on selected cell --------------
    #        x_cell, y_cell, CELL_SIZE = getCell(mouse_pos[0], mouse_pos[1])
            
    #        color = (125, 0, 100) if mouse_state == cv2.EVENT_LBUTTONDOWN else (125, 255, 0)
    #        cv2.rectangle(finalImg, (x_cell, y_cell),
    #                     (x_cell+CELL_SIZE, y_cell+CELL_SIZE), color, 2)

            cv2.imshow('image', finalImg)

            key = cv2.waitKey(5)

            if key == 27:
                break
            elif key == 32:
                paused = not paused
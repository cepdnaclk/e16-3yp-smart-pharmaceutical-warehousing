import cv2
import numpy as np
import random
import math
import imgFunctions as img
import time
import map as mp
import collision as col


counter = 1

bots = list()
graph = {}
excp_Set = set()
shortest_path = []
Path_list = []

BOT_COUNT = 3
RADI = 50
GRID_SIZE = 20
dS = 0.1
WINDOW_SIZE = 1000  # square window, height = width
CELL_SIZE = 50 

backg_H = 0
backg_W = 0
bot_H = 0
bot_W = 0

dest_reached = False

#mouse_pos = [0, 0]
#mouse_state = 0

paused = False
set_dest = False


# class to make a bot
class Bot:
    def __init__(self, ID, path):

        # bot id
        self.ID = ID
        self.path = path

        global dest_reached
       
        # list that contains orders
        self.orders = []
        
        # wait flag to hold the current position: initially set to false
        self.waitFlag = False
        
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
        

    '''
    # function to check if the mouse L button is clicked
    def isClicked(self):
        mouse_dist = np.sqrt(
            np.square(mouse_pos[0] - self.x) + np.square(mouse_pos[1] - self.y))
        if (mouse_dist < 50) and (mouse_state == cv2.EVENT_LBUTTONDOWN):
            self.clicked = not self.clicked
            return True
        return False 
    '''

    # import images of bots
    def setImgs(self, imgs):
        self.bot_imgs = imgs

    '''
    # function to set destination position and angle
    def setDest(self, x, y, angle):
        self.dest_x = int(x)
        self.dest_y = int(y)
        self.dest_angle = angle
    '''

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

# function to determine orientation
# arguements: coordinates of current and next positions, previous orientation of the bot
def orientation(bot):

    # updates the previous direction
    bot.prev_dir = bot.dir
        
    # determines the direction of the next point
    if(bot.next_x - bot.curr_x)==0 and (bot.next_y-bot.curr_y)>0:
        bot.dir = 'N'
    elif(bot.next_x - bot.curr_x)>0 and (bot.next_y-bot.curr_y)==0:
        bot.dir = 'E'
    elif(bot.next_x - bot.curr_x)==0 and (bot.next_y-bot.curr_y)<0:
        bot.dir = 'S'
    elif(bot.next_x - bot.curr_x)<0 and (bot.next_y-bot.curr_y)==0:
        bot.dir = 'W'
    
    # changes the orientation of the bot to advance to next point, depending on the current orientation
        
    # if the previous direction and the next direction are same, angle does not change
    if bot.prev_dir == bot.dir:
        bot.angle = bot.angle
        #self.prev_dir = self.dir
        
    # from North
    # N --> E
    elif bot.prev_dir == 'N' and bot.dir == 'E':
        bot.angle = bot.angle + 90
        #self.prev_dir = self.dir
        
    # N --> S
    elif bot.prev_dir == 'N' and bot.dir == 'S':
        bot.angle = bot.angle + 180
        #self.prev_dir = self.dir
        
    # N --> W
    elif bot.prev_dir == 'N' and bot.dir == 'W':
        bot.angle = bot.angle - 90
        #self.prev_dir = self.dir
        
    # from East
    # E --> N
    elif bot.prev_dir == 'E' and bot.dir == 'N':
        bot.angle = bot.angle - 90
        #self.prev_dir = self.dir
        
    # E --> S
    elif bot.prev_dir == 'E' and bot.dir == 'S':
        bot.angle = bot.angle + 90
        #self.prev_dir = self.dir
        
    # E --> W
    elif bot.prev_dir == 'W' and bot.dir == 'W':
        bot.angle = bot.angle + 180
        #self.prev_dir = self.dir

    # from South
    # S --> E
    elif bot.prev_dir == 'S' and bot.dir == 'E':
        bot.angle = bot.angle - 90
        #self.prev_dir = self.dir
        
    # S --> W
    elif bot.prev_dir == 'S' and bot.dir == 'W':
        bot.angle = bot.angle + 90
        #self.prev_dir = self.dir
        
    # S --> N
    elif bot.prev_dir == 'S' and bot.dir == 'N':
        bot.angle = bot.angle + 180
        #self.prev_dir = self.dir
        
    # from West
    # W --> N
    elif bot.prev_dir == 'W' and bot.dir == 'N':
        bot.angle = bot.angle + 90
        #self.prev_dir = self.dir
        
    # W --> S
    elif bot.prev_dir == 'W' and bot.dir == 'S':
        bot.angle = bot.angle - 90
        #self.prev_dir = self.dir
        
    # W --> E
    elif bot.prev_dir == 'W' and bot.dir == 'E':
        bot.angle = bot.angle + 180
        #self.prev_dir = self.dir


# function to update positions of bots
# inputs are bot object and path to follow
def update(bots):
    global counter
    if counter%200 == 0:
        counter = 0
        #time.sleep(1)
        # iterate over bots array and update path of all bots
        for bot in bots:
            
            # if the path is not empty 
            if len(bot.path) !=0 and bot.waitFlag == False:
            
                bot.next_x = bot.path[0][0]
                bot.next_y = bot.path[0][1]
                
                # gets the orientation
                orientation(bot)
                    
                if(bot.curr_x == bot.dest_x and bot.curr_y == bot.dest_y):
                    # sends a message to the central server once the destination is reached
                    #mqtt.send_message("Done")

                    # set the dest_reached flag to true
                    bot.dest_reached = True
                        

                else:
                    
                    if(bot.next_x >= bot.curr_x and bot.next_y ==  bot.curr_y): 
                        # advance to right
                        bot.curr_x = bot.curr_x + abs((bot.next_x-bot.curr_x))
                        print(bot.curr_x, bot.curr_y)
                        
                        
                    elif(bot.next_x < bot.curr_x and bot.next_y == bot.curr_y):
                        # advance to left  
                        bot.curr_x = bot.curr_x - abs((bot.curr_x-bot.next_x)) 
                        print(bot.curr_x, bot.curr_y)
                        
                                        
                    elif(bot.next_y >= bot.curr_y and bot.next_x == bot.curr_x):
                        # advance towards +ve Y axis
                        bot.curr_y = bot.curr_y + abs((bot.next_y-bot.curr_y))
                        print(bot.curr_x, bot.curr_y)
                        
                    elif(bot.next_y < bot.curr_y and bot.next_x == bot.curr_x):
                        # advance towards -ve Y axis
                        bot.curr_y = bot.curr_y - abs((bot.curr_y-bot.next_y))
                        print(bot.curr_x, bot.curr_y)
                        
                    
                    #print(bot.curr_x, bot.curr_y)
                    # remove the first element from the path array
                    bot.path.pop(0)
                    #time.sleep(1)
    counter = counter + 1
'''
# function to update bot positions

def update(bots):
    if len(bots) == 0:
        for i in range(BOT_COUNT):
            imgs = bot_pngs.copy()
            bot = Bot(i)
            bot.setPos(i, 0)
            bot.setImgs(imgs)
            bots.append(bot)

    else:
        # if the motion update is not paused
        if not paused:
            for bot in bots:
                # move the bot if there is a destinatiom
                # info: -1 for the destination represents that the bot has no destination
                if bot.dest_x != -1:
                    x = bot.x + dS*(bot.dest_x - bot.x)
                    y = bot.y + dS*(bot.dest_y - bot.y)
                    angle = bot.angle + 0.8
                    bot.setPos(x, y)
'''

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

'''
def mosueEvent(event, x, y, flags, param):
    global mouse_pos, mouse_state, bots, set_dest

    mouse_pos = [x, y]
    mouse_state = event

    # In a event of left down click
    #   - if the current state of destination mode is set
    if not set_dest:
        for bot in bots:
            if bot.isClicked():
                set_dest = True
                bot.setDest(-1, -1, 0)
                break

    elif event == cv2.EVENT_LBUTTONDOWN:
        for bot in bots:
            if bot.clicked:
                bot.clicked = False

                # convert the mouse point to the center clicked cell
                x_cell, y_cell, cell_size = getCell(x,y)
                x_cell = x_cell + int(cell_size/2)
                y_cell = y_cell + int(cell_size/2)

                bot.setDest(x_cell, y_cell, 0)
                set_dest = False
'''
'''
def getCell(x, y):
    cell_size = int(WINDOW_SIZE/GRID_SIZE)
    x_cell = int(mouse_pos[0]/cell_size)*cell_size
    y_cell = int(mouse_pos[1]/cell_size)*cell_size

    return x_cell, y_cell, cell_size
'''

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

    ''' initializes the graph and the grid '''
    
    # adding shelves
    mp.add_shelves(excp_Set,(2,2), (9,9))
    mp.add_shelves(excp_Set,(2,11), (9,18))
    mp.add_shelves(excp_Set,(11,11), (18,18))
    mp.add_shelves(excp_Set,(11,2), (18,9))
    
    # creates the graph
    mp.generate_graph(graph, excp_Set, 21)
    print(graph)

    # destination array
    path_dest = [[(0,0),(4,10)], [(1,0),(13,19)], [(2,0), (20,20)]]
    Path_list = [[]for _ in range(BOT_COUNT)]
         
    while True:

        # creates bots images at the initial run
        if len(bots) == 0:
            for i in range(BOT_COUNT):
                imgs = bot_pngs.copy()
                mp.dijkstra(graph,path_dest[i][0],path_dest[i][1],Path_list[i], [], {}, {})
                bot = Bot(i, Path_list[i])
                #print(Path_list[i])

                #bot.setPos(i, 0)
                bot.curr_x = i
                bot.curr_y = 0
                bot.angle = 180
                bot.waitFlag = False
                bot.setImgs(imgs)
                bots.append(bot)
            
        else:    
            col.collision(bots)
            #update(bots)

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

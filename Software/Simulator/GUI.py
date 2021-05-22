import cv2
import numpy as np
import random
import math
import imgFunctions as img
import time
import map as mp
import collision as col
import driver as driver
import bot as bt
import concurrent.futures


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
GRID_SIZE = 22
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
    inputSchedule = {'0':[(1,6), (11,15), (12,15)], '1':[(22,6), (22,15), (1,15)], '2':[(22,16), (1,6)], '3':[(1,6), (11,6), (12,6), (22,6), (1,15), (11,15), (12,15), (22,15)]
                     
                    }


    ''' initializes the graph and the grid '''
    
    # adding shelves
    mp.add_shelves(excp_Set,(3,3), (9,9))     # Rack A
    mp.add_shelves(excp_Set,(3,12), (10,18))    # Rack C
    mp.add_shelves(excp_Set,(13,3), (21,9))    # Rack B
    mp.add_shelves(excp_Set,(13,12), (21,18))   # Rack D

    # mp.add_shelves(excp_Set,(8,0), (21,1))      # run-off area near delivery station

    # mp.add_shelves(excp_Set,(2,3), (3,10))      # run-off area near rack A
    # mp.add_shelves(excp_Set,(2,12), (3,19))     # run-off area near rack C
    # mp.add_shelves(excp_Set,(13,3), (14,10))    # run-off area near rack B
    # mp.add_shelves(excp_Set,(13,12), (14,19))   # run-off area near rack D

    # mp.add_nodes(excp_Set, (2,6))
    # mp.add_nodes(excp_Set, (2,7))
    # mp.add_nodes(excp_Set, (2,15))
    # mp.add_nodes(excp_Set, (2,16))
    # mp.add_nodes(excp_Set, (13,6))
    # mp.add_nodes(excp_Set, (13,7))
    # mp.add_nodes(excp_Set, (13,15))
    # mp.add_nodes(excp_Set, (13,16))

    #print(excp_Set)

    # creates the graph
    mp.generate_graph(graph, excp_Set, 26)
    # print(graph)
    
    ''' Left side roads along columns '''
    # for (1,3) --> (1,9)
    for i in range(3,10):
        del graph[(1,i)][(0,i)]
        del graph[(1,i)][(2,i)]

    # for (0,2) --> (0,9)
    for i in range(2,10):
        #del graph[(0,i)][(0,i-1)]
        del graph[(0,i)][(1,i)]


    # for (1,12) --> (1,18)
    for i in range(12,19):
        del graph[(1,i)][(0,i)]
        del graph[(1,i)][(2,i)]

    # for (0,12) --> (0,19)
    for i in range(12,20):
        #del graph[(0,i)][(0,i-1)]
        del graph[(0,i)][(1,i)]
    
    ''' Bottom side roads along rows '''
    # for (1,20) --> (10,20)
    for i in range(1,11):
        del graph[(i,20)][(i,19)]
        del graph[(i,20)][(i,21)]
    
    # for (13,20) --> (22,20)
    for i in range(13,23):
        del graph[(i,20)][(i,19)]
        del graph[(i,20)][(i,21)]

    # for (2,19) --> (10,19)
    for i in range(2,11):
        del graph[(i,19)][(i,20)]
        #del graph[(1,20)][(1,21)]
    
    # for (13,19) --> (21,19)
    for i in range(13,22):
        del graph[(i,19)][(i,20)]
        #del graph[(1,20)][(1,21)]
    
    ''' Right side roads along columns '''

    # for (22,3) --> (22,9)
    for i in range(3,10):
        #del graph[(22,i)][(21,i)]
        del graph[(22,i)][(23,i)]

    # for (22,12) --> (22,18)
    for i in range(12,19):
        #del graph[(22,i)][(21,i)]
        del graph[(22,i)][(23,i)]


    # for (23,2) --> (23,9)
    for i in range(2,10):
        del graph[(23,i)][(22,i)]
        del graph[(23,i)][(24,i)]
    
    #print(graph)

    # for (23,12) --> (23,19)
    for i in range(12,19):
        del graph[(23,i)][(22,i)]
        del graph[(23,i)][(24,i)]

    ''' Top side roads along row '''

    # for (4,1) --> (10,1)
    for i in range(1,11):
        del graph[(i,1)][(i,2)]
        if i>=8:
            del graph[(i,1)][(i,0)]
    
    # for (13,1) --> (22,1)
    for i in range(13,23):
        del graph[(i,1)][(i,0)]
        del graph[(i,1)][(i,2)]

    # for (4,2) --> (10,2)
    for i in range(4,11):
        del graph[(i,2)][(i,1)]
        del graph[(i,2)][(i,3)]
    
    # for (13,2) --> (21,2)
    for i in range(13,22):
        del graph[(i,2)][(i,1)]
        del graph[(i,2)][(i,3)]

    ''' Center channel roads vertical '''

    # for (11,3) --> (11,9)
    for i in range(3,10):
        del graph[(11,i)][(12,i)]

    # for (11,12) --> (11,19)
    for i in range(12,20):
        del graph[(11,i)][(12,i)]

    # for (12,3) --> (12,9)
    for i in range(3,10):
        del graph[(12,i)][(11,i)]
        del graph[(12,i)][(13,i)]

    # for (12,12) --> (12,18)
    for i in range(12,19):
        del graph[(12,i)][(11,i)]
        del graph[(12,i)][(13,i)]

    ''' Junction points '''
    del graph[(1,2)][(0,2)]

    del graph[(1,19)][(0,19)]

    del graph[(22,2)][(23,2)]

    del graph[(22,19)][(23,19)]


    # destination array
    #racks = [[(0,0),(4,10)], [(1,0),(13,19)], [(2,0), (20,20)]]
    #Path_list = [[]for _ in range(BOT_COUNT)]
     
    while True:

        # creates bots images at the initial run
        if len(bots) == 0:
            for i in range(BOT_COUNT):
                imgs = bot_pngs.copy()
                bot = bt.Bot(i)
               
                #bot.setPos(i, 0)
                # each bot is positioned initially in a place where (x,y) coordinates are even
                # the mapping function used is as follows;
                # (x,y) ---> (2x,2y)
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

            # calls start function activate bots
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
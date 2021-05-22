import cv2
import numpy as np
import random
import math
import imgFunctions as img
import time
import map as mp
import collision as col
import TSP as tsp
import GUI as gui
import concurrent.futures


#bots = list()               # array of bot objects
#shortestPathtoNodes = {}    # dict to hold shortest path to each node from each node
#PathCost = {}               # dict to hold path cost from node to node
#graph = {}                  # graph of the floor
#excp_Set = set()            # set that contains disconnected nodes from the graph - nodes where shelves are placed 
#Path_List = {}

counter = 1

'''
# driver function - this function is called in the main method of the GUI.py. This handles all the processing including scheduling, path planning and collision avoidance
# input arguements :    
                        # shortestPathtoNodes   - dict that holds shortest path coordinates from a node to node of the entire graph
                        # PathCost              - dict that holds calculated path weight for the shortest paths stored in shortestPathtoNodes dict
                        # bots                  - an array of bot objects
                        # graph                 - dict containing graph of the floor
                        # inputSchedule/ racks  - dict containing 
                        # src                   - source node
                        # excp_Set              - set with disconnected nodes from the graph
'''

# function to set path for bots
def setPath(graph, excp_Set, shortestPathtoNodes, PathCost, bot, inputSchedule):
    
    ''' if any errors occur, check if the path is correctly assigned to bots'''
    # calculates optimal path 
    #print(bot.ID)
    #OptPath = tsp.travellingSalesmanProblem(graph, (bot.ID, 0), inputSchedule["{}".format(bot.ID)], shortestPathtoNodes)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future =  executor.submit(tsp.travellingSalesmanProblem, graph, (bot.ID, 0), inputSchedule["{}".format(bot.ID)], shortestPathtoNodes)
        OptPath =  future.result()
        

    del inputSchedule["{}".format(bot.ID)]
    
    # adds the path to bot
    #print(OptPath)
   
    bot.path = tsp.getPath(graph, (bot.ID, 0), shortestPathtoNodes, OptPath)
    bot.OrderComplete = False


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
    if counter%50 == 0:
        counter = 0
        #time.sleep(1)
        # iterate over bots array and update path of all bots
        for bot in bots:
            
            # if the path is not empty 
            if len(bot.path) !=0 and bot.waitFlag == False:

                subArr = bot.path[bot.currentPosVal[0]]
                if  bot.currentPosVal[1] + 1 <= len(subArr):
                    #print(bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]])
                    # if bot.waitFlag:
                    #     print(bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][0])
                    #     bot.next_x = bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][0] + 1  
                    #     bot.next_y = bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][1]
                    #     print(bot.next_x)
                    #else:

                    bot.next_x = bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][0]  
                    bot.next_y = bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][1]

                    #print(bot.path[0][0][0])
                    #print(bot.path[0][0][1])
                    
                                            
                    if(bot.curr_x == bot.dest_x and bot.curr_y == bot.dest_y):
                        # sends a message to the central server once the destination is reached
                        #mqtt.send_message("Done")

                        # set the dest_reached flag to true
                        bot.dest_reached = True
                            

                    else:
                        # if the bot has reached immediate destination
                                               
                        if(bot.next_x >= bot.curr_x and bot.next_y ==  bot.curr_y): 
                            # advance to right
                            bot.curr_x = bot.curr_x + abs((bot.next_x-bot.curr_x))
                            if(bot.curr_y%2 != 0 ):
                                if (bot.curr_y + 1) in mp.graph:
                                    bot.curr_y = bot.curr_y + 1
                                    #break

                                elif (bot.curr_y - 1) in mp.graph:
                                    bot.curr_y = bot.curr_y - 1
                                    #break
                            #print(bot.curr_x, bot.curr_y)
                            
                            
                        elif(bot.next_x < bot.curr_x and bot.next_y == bot.curr_y):
                            # advance to left  
                            bot.curr_x = bot.curr_x - abs((bot.curr_x-bot.next_x)) 
                            if(bot.curr_y%2 == 0 ):
                                if (bot.curr_y + 1) in mp.graph:
                                    bot.curr_y = bot.curr_y + 1
                                    #break

                                elif (bot.curr_y - 1) in mp.graph:
                                    bot.curr_y = bot.curr_y - 1
                                    #break
                            #print(bot.curr_x, bot.curr_y)
                            
                                            
                        elif(bot.next_y >= bot.curr_y and bot.next_x == bot.curr_x):
                            # advance towards +ve Y axis
                            bot.curr_y = bot.curr_y + abs((bot.next_y-bot.curr_y))
                            if(bot.curr_x%2 != 0 ):
                                if (bot.curr_x + 1) in mp.graph:
                                    bot.curr_x = bot.curr_x + 1
                                    #break

                                elif (bot.curr_x - 1) in mp.graph:
                                    bot.curr_x = bot.curr_x - 1
                                    #break
                            #print(bot.curr_x, bot.curr_y)
                            
                        elif(bot.next_y < bot.curr_y and bot.next_x == bot.curr_x):
                            # advance towards -ve Y axis
                            bot.curr_y = bot.curr_y - abs((bot.curr_y-bot.next_y))
                            if(bot.curr_x%2 == 0 ):
                                if (bot.curr_x + 1) in mp.graph:
                                    bot.curr_x = bot.curr_x + 1
                                    #break

                                elif (bot.curr_x - 1) in mp.graph:
                                    bot.curr_x = bot.curr_x - 1
                                    #break
                            #print(bot.curr_x, bot.curr_y)
                            
                        
                        # remove the first element from the path array
                        #print(bot.path)
                        #m = bot.path[0].pop(0)
                        #print(m)
                    bot.currentPosVal[1] += 1
                else:
                    if bot.currentPosVal[0] +1 < len(bot.path):
                        #bot.dest_reached = True
                        #if not bot.dest_reached:
                        bot.currentPosVal[0] += 1
                        bot.currentPosVal[1] = 0
                    else:
                        continue


                # gets the orientation
                orientation(bot)
                
                #print(bot.path[0])
                # if len(bot.path[0])==0:
                #     bot.path[0].pop(0)
                #     continue

                
                    
                    #time.sleep(1)
    counter = counter + 1

# function which resolves collisions and update postions
def start(bots):
    #col.collision(bots)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future =  executor.submit(col.collision, bots)
        #return_value =  future.result()

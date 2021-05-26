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
import paho.mqtt.client as mqtt
import json
#import mqtt_AGV



#bots = list()               # array of bot objects
#shortestPathtoNodes = {}    # dict to hold shortest path to each node from each node
#PathCost = {}               # dict to hold path cost from node to node
#graph = {}                  # graph of the floor
#excp_Set = set()            # set that contains disconnected nodes from the graph - nodes where shelves are placed 
#Path_List = {}

counter = 1

# flag to abort updating all AGV's next position
abort = False


def on_message(client, userdata, message):

    print(json.loads(message.payload))

#MQTT broker IP address


broker_address = "broker.mqttdashboard.com"


# client instance
client = mqtt.Client("Local_1", transport='websockets')
client.on_message = on_message

client.connect(broker_address, 8000, 60)

client.loop_start() 

client.subscribe("AGV_receive")



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
def setPath(graph, shortestPathtoNodes, PathCost, bot, inputSchedule):

    global client
    
    ''' if any errors occur, check if the path is correctly assigned to bots'''
    print((bot.ID,0))
    #OptPath = tsp.travellingSalesmanProblem(graph, (bot.ID, 0), inputSchedule["{}".format(bot.ID)], shortestPathtoNodes)

    # calculates the optimum path from src to racks
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future =  executor.submit(tsp.travellingSalesmanProblem, graph, (bot.ID, 0), inputSchedule["{}".format(bot.ID)], shortestPathtoNodes)
        OptPath =  future.result()
        
    # delete the entry from input schedule
    del inputSchedule["{}".format(bot.ID)]
    
    #print(OptPath)
    # adds the path to bot
    bot.path = tsp.getPath(graph, (bot.ID, 0), shortestPathtoNodes, OptPath)

    client.publish("AGV_send", json.dumps(bot.path), qos=2)

    # MQTT send
    # set the order complete status to false
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
    global client
    global counter
    global abort
    if counter%50 == 0:
        counter = 0
        # checks if the operation is aborted
        
        if(bool(abort)):
            for bot in bots:
                bot.curr_x = int(-1)
                bot.curr_y = int(-1)
         
        else:
        
            # iterate over bots array and update path of all bots
            for bot in bots:
                
                # if the path is not empty and waitFlag has not been raised
                if len(bot.path) !=0 and bot.waitFlag == False:

                    # get the first route to the first destination
                    subArr = bot.path[bot.currentPosVal[0]]
                    # checks if the sub array contains at least one coordinate pair
                    if  bot.currentPosVal[1] + 1 <= len(subArr):
                        
                        # set the dest_reached flag to false
                        bot.dest_reached = False

                        # gets the destination coordinate
                        # bot.dest_x = bot.path[bot.currentPosVal[0]][-1][0]
                        # bot.dest_y = bot.path[bot.currentPosVal[0]][-1][1]
                        
                        # gets the next coordinate from the bot.path
                        bot.next_x = bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][0]  
                        bot.next_y = bot.path[bot.currentPosVal[0]][bot.currentPosVal[1]][1]                   

                        orientation(bot)
                        
                        bot.curr_x = bot.next_x
                        bot.curr_y = bot.next_y    

                        
                        
                        # updates current position val tuple
                        # this keeps track of the coordinate pair that needs to fetched for next position
                        bot.currentPosVal[1] += 1
                    else:
                        if bot.currentPosVal[0] +1 < len(bot.path):
                            # up the dest_reached flag 
                            bot.dest_reached = True
                            
                            client.publish("destReached_Flag", json.dumps(True))
                            #mqtt_AGV.sendFlag(True)

                            
                            # add MQTT facility to send a msg from server to start moving the bo again
                            # setup a global variable in bot class which sense MQTT msgs and adjust a block inside bot class which frees bot
                            # wait for  seconds
                            #time.sleep(5)
                            
                            bot.currentPosVal[0] += 1
                            bot.currentPosVal[1] = 0
                        else:
                            bot.path = []
                            if(bot.curr_x == bot.init_x and bot.curr_y == bot.init_y):
                                bot.OrderComplete = True
                                #print("Order Complete %d" % bot.ID)
                            #print(bot.path)
                            continue


                    # gets the orientation
                    orientation(bot)
                    
                    #print(bot.path[0])
                    # if len(bot.path[0])==0:
                    #     bot.path[0].pop(0)
                    #     continue
                
                elif len(bot.path) !=0 and bot.waitFlag == True:

                    # bot.next_x = int(-1)
                    # bot.next_y = int(-1)

                    orientation(bot)

                    bot.curr_x = bot.curr_x
                    bot.curr_y = bot.curr_y    

                    

                
                    
                    #time.sleep(1)
    counter = counter + 1

# function which resolves collisions and update postions
def start(bots):
    #col.collision(bots)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future =  executor.submit(col.collision, bots)
        #return_value =  future.result()

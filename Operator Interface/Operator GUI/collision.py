import numpy as np
import random
import math
from collections import defaultdict
import GUI as gui
import driver as driver

''' lists to hold bots that reach junction points'''

''' center circular intersection '''
# junction codes and their corresponding coordinates
# J0 = (11,10), J1 = (11,11), J2 = (12,11), J3 = (12,10)
J0 = []
J1 = []
J2 = []
J3 = []

''' Upper T section intersection '''
# junction codes and their corresponding coordinates
# J4 = (11,2), J5 = (12,2), J6 = (12,1)
J4 = []
J5 = []
J6 = []


''' Lower T section intersection '''
# junction codes and their corresponding coordinates
# J7 = (11,19), J8 = (11,20)
J7 = []
J8 = []


''' LHS T section intersection '''
# junction codes and their corresponding coordinates
# J9 = (0,10), J10 = (1,10)
J9 = []
J10 = []

''' RHS T section intersection '''
# junction codes and their corresponding coordinates
# J11 = (22,11), J12 = (22,10)
J11 = []
J12 = []

# list that holds all junction nodes
junctions = [(11,10), (11,11), (12,11), (12,10), (11,2), (12,2), (12,1), (11,19), (11,20), (0,10), (1,10), (22,11), (22,10)]

# list that holds junction arrays
juncArray = [J0,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10,J11,J12]

def collision(bots):

    # dict to hold the next pos a sa key and bot ids in a list as values
    nextPos = {}
    # dict 
    botMapping = {}

    # iterate over all bots
    for botIndex in range(len(bots)):
        bot = bots[botIndex]
        botMapping[bot.ID] = bot

        # if next pos exist in the dict
        if (bot.next_x, bot.next_y) in nextPos:
            nextPos[(bot.next_x, bot.next_y)].append(bot.ID) 
        # if not, creates a new list 
        else:
            nextPos[(bot.next_x,bot.next_y)] = [bot.ID]
        
        if (bot.next_x, bot.next_y) in junctions:
            tempIndex = junctions.index((bot.next_x, bot.next_y))
            juncArray[tempIndex].append(bot.ID)
            #print(juncArray)
            #print(J1)

    # checks if any duplicates exists
    if len(nextPos) < len(bots):
        for key in nextPos:
            if len(nextPos[key])>1:
                #bot()
                botMapping[nextPos[key][0]].waitFlag = False

                for i in range(1, len(nextPos[key])):
                    
                    botMapping[nextPos[key][i]].waitFlag = True

                del botMapping[nextPos[key][0]]
                # calls update function to update positions
                driver.update(bots)
    # if no collisions detected, update bots to next positions
    else:
        for bot in bots:
            bot.waitFlag = False
            driver.update(bots)


    # virtual traffic light system
    for junc in juncArray:

        #print('here')
        # allows the first bot that arrives the junction to pass
        bots[junc[0]].waitFlag = False
        #print(bots[junc[0]].waitFlag)
        # halt others to until the wait the first one passes.
        for bt in junc:
            if bt != junc[0]:
                bots[bt].waitFlag = True
         
        # pop the first bot from the junc list
        junc.remove(junc[0])
        # update bots
        driver.update(bots)







'''----- UNIT TESTING -----'''

# if __name__ == "__main__": 

#     bots = list()
#     # creates bot objects
#     for i in range(4):
#         bot = gui.Bot(i)
#         bots.append(bot)
      
#     bot1 = bots[0]   # bot 1
#     bot2 = bots[1]   # bot 2
#     bot3 = bots[2]   # bot 3
#     bot4 = bots[3]   # bot 4

#     # setting initial coordinates and next positions of bot 1
#     bot1.curr_x = 0
#     bot1.curr_y = 0
#     bot1.next_x = 2
#     bot1.next_y = 7

#     # setting initial coordinates and next positions of bot 2
#     bot2.curr_x = 3
#     bot2.curr_y = 0
#     bot2.next_x = 2
#     bot2.next_y = 7

#     # setting initial coordinates and next positions of bot 3
#     bot3.curr_x = 6
#     bot3.curr_y = 0
#     bot3.next_x = 2
#     bot3.next_y = 7

#     # setting initial coordinates and next positions of bot 4
#     bot4.curr_x = 13
#     bot4.curr_y = 2
#     bot4.next_x = 2
#     bot4.next_y = 7

#     collision(bots)

#     for bot in bots:
#         print("Bot ID: ", bot.ID, ", Wait Flag status: ",bot.waitFlag)
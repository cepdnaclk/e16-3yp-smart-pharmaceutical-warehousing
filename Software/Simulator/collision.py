import numpy as np
import random
import math
from collections import defaultdict
import GUI as gui
import driver as driver

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

    # checks if any duplicates exists
    if len(nextPos) < len(bots):
        for key in nextPos:
            if len(nextPos[key])>1:
                #bot()
                botMapping[nextPos[key][0]].waitFlag = False

                for i in range(1, len(nextPos[key])):
                    
                    botMapping[nextPos[key][i]].waitFlag = True

                # calls update function to update positions
                driver.update(bots)
    # if no collisions detected, update bots to next positions
    else:
        for bot in bots:
            bot.waitFlag = False
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
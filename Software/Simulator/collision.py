import numpy as np
import random
import math
from collections import defaultdict
import GUI as gui

def collision(bots):

    # dict to hold the next pos asa key and bot ids in a list as values
    nextPos = {}
    
    # iterate over all bots
    for bot in bots:
        # if next pos exist in the dict
        if (bot.next_x, bot.next_y) in nextPos.keys():
            nextPos[(bot.next_x, bot.next_y)].append(bot.ID) 
        # if not, creates a new list 
        else:
            nextPos[(bot.next_x,bot.next_y)] = [bot.ID]

    # checks if any duplicates exists
    if len(nextPos) < len(bots):
        for key in nextPos:
            if len(nextPos[key])>1:
                #bot()
                for i in range(len(nextPos[key])):
                    # allows the first one to pass through
                    if bot.ID == nextPos[key][0]:
                        bot.waitFlag = False
                    # halts all the other bots
                    if bot.ID == nextPos[key][i]:
                        bot.waitFlag = True 
                # calls update function to update positions
                gui.update(bots)
    # if no collisions detected, update bots to next positions
    else:
        for bot in bots:
            bot.waitFlag = False
            gui.update(bots)

        
       

        
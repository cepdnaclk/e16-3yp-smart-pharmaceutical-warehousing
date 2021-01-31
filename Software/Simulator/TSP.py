from sys import maxsize 
import itertools
from itertools import permutations
import map as mp

#graph = {}

#excp_Set = set()

#shortestPathtoNodes = {}    # dict to hold shortest path to each node from each node

PathCost = {}      # dict to hold path cost from node to node

#racks = [(1,5), (19,5), (19,14), (1,14)]
 
# implementation of traveling Salesman Problem 
    # graph - graph of the floor map
    # src - source node
    # racks - assigned racks (destination points)
def travellingSalesmanProblem(graph, src, racks, shortestPathtoNodes): 
    
    indx = 0    # indexing variable
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize

    # optimal path
    opt_path = 0

    # calculates all possible path permutations
    next_permutation=list(itertools.permutations(racks))
    # print(next_permutation)
    # print("\n")
    # print("Wait for it...\n")
    # iterate over each permutation    
    for i in next_permutation:
       
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # computes shortest path and current path weight 
        k = src 
        for j in i:
            cost = 0

            # if the path is stored
            if ("{}-{}".format(k, j)) in shortestPathtoNodes.keys():
                
                # get the stored path cost
                cost = PathCost["{}-{}".format(k, j)] 

            # if the path is not stored
            elif ("{}-{}".format(k, j)) not in shortestPathtoNodes.keys(): 
                
                # calculates the shortest path 
                shortestPathtoNodes["{}-{}".format(k, j)] = [] # creates an empty list to hold the path
                mp.dijkstra(graph,k, j, shortestPathtoNodes["{}-{}".format(k, j)], [], {}, {})
                
                # calculates the cost of the path
                for l in range(len(shortestPathtoNodes["{}-{}".format(k, j)])):
                    # check this point - using l and l+1
                    if (l+1)<len(shortestPathtoNodes["{}-{}".format(k, j)]):
                        cost = cost + graph[shortestPathtoNodes["{}-{}".format(k, j)][l]][shortestPathtoNodes["{}-{}".format(k, j)][l+1]]
                
                # adds the calculated weight to Path Cost dict
                PathCost["{}-{}".format(k, j)] = cost
            
            # adds the path cost to 
            current_pathweight += cost 

            # sets the starting point as the current rack
            k = j 
        
        #current_pathweight += graph[k][src] 
       
        # update minimum 
        min_path = min(min_path, current_pathweight) 

        if min_path == current_pathweight:
            opt_path = next_permutation.index(i) 
        
        # print("Path Permutation: ",i)
        # print("Path Cost : ", current_pathweight)
        # print("Currently optimum path: ", next_permutation[opt_path])
        # print("Currently optimum path cost: ", min_path)
        # print("\n")
        
        
            
    #print(shortestPathtoNodes.keys())  
    # print("Optimum oath analysis is finished.")
    # print("Optimum path : ", next_permutation[opt_path])
    # print("Optimum path cost :", min_path) 
             
    # returns the optimal path with minimal cost    
    return next_permutation[opt_path]






# function to get the complete path cycle of a bot for one run
def getPath(graph, src, shortestPathtoNodes,OptRoute):
    #print(graph)
    # creates sublists to hold paths -  for one bot
    bot_path = [[]for _ in range(len(OptRoute)+1)]
    #print(bot_path)

    if ("{}-{}".format(src, OptRoute[0])) not in shortestPathtoNodes.keys():
        
        shortestPathtoNodes["{}-{}".format(src, OptRoute[0])] = []
        mp.dijkstra(graph, src, OptRoute[0], shortestPathtoNodes["{}-{}".format(src, OptRoute[0])], [], {}, {})
        #print(shortestPathtoNodes["{}-{}".format(src, OptRoute[0])])
        bot_path[0] = shortestPathtoNodes["{}-{}".format(src, OptRoute[0])]
    
    else:
        # path from src to the first rack
        bot_path[0] = shortestPathtoNodes["{}-{}".format(src, OptRoute[0])]
        #print(bot_path[0])

    # adding other paths 
    for i in range(len(OptRoute)):
        if (i+1)<len(OptRoute):
            #print(shortestPathtoNodes["{}-{}".format(OptRoute[i], OptRoute[i+1])])
            bot_path[i+1] = shortestPathtoNodes["{}-{}".format(OptRoute[i], OptRoute[i+1])]
              
       
    if ("{}-{}".format(OptRoute[-1], src)) not in shortestPathtoNodes.keys():
        
        shortestPathtoNodes["{}-{}".format(OptRoute[-1], src)] = []
        mp.dijkstra(graph, OptRoute[-1], src, shortestPathtoNodes["{}-{}".format(OptRoute[-1], src)], [], {}, {})
        #print(shortestPathtoNodes["{}-{}".format(src, OptRoute[0])])
        bot_path[-1] = shortestPathtoNodes["{}-{}".format(OptRoute[-1], src)]
    
    else:
        # path from src to the first rack
        bot_path[-1] = shortestPathtoNodes["{}-{}".format(OptRoute[-1], src)]

    #print(bot_path)
    return bot_path


# '''-----UNIT TESTING-----'''

# if __name__ == "__main__":
#     ### adding shelves and creating the graph

#     graph = {}
#     excp_Set = set()

#     shortestPathtoNodes = {}    # dict to hold shortest path to each node from each node
#     PathCost = {}               # dict to hold path cost from node to node
    
#     # adding shelves
#     mp.add_shelves(excp_Set,(3,3), (10,10))
#     mp.add_shelves(excp_Set,(3,13), (10,20))
#     mp.add_shelves(excp_Set,(13,3), (20,10))
#     mp.add_shelves(excp_Set,(13,10), (20,20))

#     # creates the graph
#     mp.generate_graph(graph, excp_Set, 31)

    
#     '''-----FOR TRAVELLING SALESMAN ALGORITHM-----'''
#     racks = [(2,6), (12,16), (12,7), (2,16)]
#     travellingSalesmanProblem(graph, (0,0), racks, shortestPathtoNodes)

   
   
   
   
   

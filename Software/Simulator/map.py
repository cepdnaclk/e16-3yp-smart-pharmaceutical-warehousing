import numpy as np
import random
import math
import concurrent.futures
from collections import defaultdict

# dict to hold the graph 
graph = {}

# list to hold the shortest path
path = []

# exception points in the graph
excp_Set = set()

# function to add shelves to the graph

def add_shelves(excp_Set,u,v):
    for i in range(u[0], v[0]+1):
        for j in range(u[1], v[1]+1):
            #print(i,j)
            excp_Set.add((i,j))
    return excp_Set   

# # function to add individual nodes
def add_nodes(excp_Set, u):
    excp_Set.remove(u)



# function to create a graph from the given size of a grid
def generate_graph(graph,excp_Set, nodes):
    
    # append neighbours
    for i in range(nodes):
        for j in range(nodes):
            if (i,j) not in excp_Set:
                if (i-1)>=0:
                    if (i,j) in graph: 
                        graph[(i,j)][(i-1,j)] = 1
                    else:
                        graph[(i,j)] = {(i-1,j): 1}
                if (j-1)>=0:
                    if (i,j) in graph:
                        graph[(i,j)][(i,j-1)] = 1
                    else:
                        graph[(i,j)] = {(i,j-1): 1}
                
                if (i,j) in graph and (i+1) < nodes:
                    graph[(i,j)][(i+1,j)] = 1
                elif (i+1) < nodes:
                    graph[(i,j)] = {(i+1,j): 1}
                
                if (i,j) in graph and (j+1) < nodes:
                    graph[(i,j)][(i,j+1)] = 1
                elif (j+1) < nodes:
                    graph[(i,j)] = {(i,j+1): 1}
    #return graph


# # function to mark roads along columns
# def mark_roadsX(graph, strtNode, endNode, ):
#      for i range( )



# function to find shortest path using Dijkstra's shortest path algorithm
def dijkstra(graph,src,dest,path,visited,distances,predecessors):
    """ calculates a shortest path tree routed in src"""    

    #print(graph[(19, 5)])
    # checks if the source and dest node are in the graph
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')  

    # terminating condition
    if src == dest:
        # array to hold the path
        #path=[]
        
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        #print(path)
        # reverses the array, to display the path nicely
        #readable=path[0]
        #for index in range(1,len(path)): readable = path[index]+'--->'+readable
        #prints it 
        if dest not in path:
            print("no path")
        
        else:
            path.reverse()
            #print(path)
            #return path  

    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                #print(graph[src][neighbor])
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    #print(graph[src][neighbor])
                    predecessors[neighbor] = src

        # mark as visited
        visited.append(src)
        #print(visited)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))  

        if not (unvisited == {}):     
            x=min(unvisited, key=unvisited.get)
            #dijkstra(graph,x,dest,path,visited,distances,predecessors)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future =  executor.submit(dijkstra, graph,x,dest,path,visited,distances,predecessors)
                #return_value =  future.result()


'''---- UNIT TESTING ----'''

# if __name__ == "__main__":
#     # creates the graph
#     #generate_graph(graph, 21)

#     # adding shelves
#     add_shelves(excp_Set, (2,2), (9,9))
#     add_shelves(excp_Set, (2,11), (9,18))
#     add_shelves(excp_Set, (11,11), (18,18))
#     add_shelves(excp_Set, (11,2), (18,9))

#     #print(graph)
#     generate_graph(graph,excp_Set, 21)
#     # gets the shortest path
#     dijkstra(graph,(2,0),(13,0))
#     print(path)

#     #add_shelves((2,2),(9,9))
#     #generate_graph(graph, 21)
#     #print(excp_Set)
#     #print("\n\n\n")
#     #print(len(excp_Set))
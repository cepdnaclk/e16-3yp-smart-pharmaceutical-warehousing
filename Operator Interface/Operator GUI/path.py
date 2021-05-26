import numpy as np
import random
import math
from collections import defaultdict

# dict to hold the graph 
graph = {}

# list to hold the shortest path
path = []

# exception points in the graph
excp_Set = set()

def add_shelves(u,v):
    for i in range(u[0], v[0]+1):
        for j in range(u[1], v[1]+1):
            #print(i,j)
            excp_Set.add((i,j))
        

# function to create a graph from the given size of a grid
def generate_graph(graph,nodes):
    
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
                
                if (i,j) in graph:
                    graph[(i,j)][(i+1,j)] = 1
                else:
                    graph[(i,j)] = {(i+1,j): 1}
                
                graph[(i,j)][(i,j+1)] = 1



# function to add shelves to the graph
# nodes where shelves are placed, are denoted by inf
# arguements: u,v - coordinate pairs of of the diagonal of the shelf
'''def add_shelves(graph, u, v):
    
    # iterate over the given graph
    for i in range(u[0], v[0]+1):
        for j in range(u[1], v[1]+1):

            excp_Set.add((i,j))
            graph[(i,j)][(i-1,j)] = float('inf')
            graph[(i,j)][(i+1,j)] = float('inf')
            graph[(i,j)][(i,j-1)] = float('inf')
            graph[(i,j)][(i,j+1)] = float('inf')

    return graph '''



# function to find shortest path using Dijkstra's shortest path algorithm
def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """    

    # takes access to the global variable
    global path

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
        # reverses the array, to display the path nicely
        #readable=path[0]
        #for index in range(1,len(path)): readable = path[index]+'--->'+readable
        #prints it 
        if dest not in path:
            print("no path")
        
        else:
            path.reverse()
            #print(path)
            return path  

    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
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

        print(unvisited)              
        x=min(unvisited, key=unvisited.get)
        #print("whats' in x\n")
        #print(unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)



'''---- Testing ----'''
'''
# creates the graph
generate_graph(graph, 21)

# adding shelves
add_shelves(graph, (2,2), (9,9))
add_shelves(graph, (2,11), (9,18))
add_shelves(graph, (11,11), (18,18))
add_shelves(graph, (11,2), (18,9))
#print(graph)

# gets the shortest path
dijkstra(graph,(10,1),(10,10))
#print(path)
'''
'''add_shelves((2,2),(9,9))
generate_graph(graph, 21)
print(excp_Set)
print("\n\n\n")
print(len(excp_Set))'''
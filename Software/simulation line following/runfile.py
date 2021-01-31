from cell import *
from agv import *
from map import *



my_map = MAP(Y=2,X=2)
my_map.cell_table( X= 0 , Y = 0 , array= [[2, 3], [3, 5], [2, 3], [2, 3], [2, 3]])
my_map.cell_table(X=1, Y=0, array=[[2, 3], [3, 5], [2, 3], [2, 3], [2, 3]])
my_map.cell_table(X=0, Y=1, array=[[1, 3], [3, 5], [6, 3], [2, 3], [2, 3]])
my_map.cell_table(X=1, Y=1, array=[[2, 3], [4, 5], [2, 3], [8, 3], [9, 3]])



#my_map.map_print_thread()

my_agv = AGV(MAP= my_map.cell_map[0][0] , full_map =my_map  )

#my_agv2 = AGV(MAP=my_map.cell_map[0][1], full_map=my_map)
#destination = [0,0] 
#my_agv.go_to(dst = destination)

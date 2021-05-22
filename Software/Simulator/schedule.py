import random
import time
from math import ceil

# class shedule:
#     def __init__(self, number_of_agv, agv_size, number_of_rack, racksize, pipeline):
        
#         self.free_agv = range(number_of_agv)
#         self.rack = range(number_of_rack)
#         self.rack_size = racksize
#         self.rack_iteam = []
#         self.pipeline = pipeline


#         for y in range(number_of_rack):
#             t = []
#             for x in range(number_of_rack):
#                 t.append([])
#             self.rack_iteam.append(t)

            
#         #print(self.rack_iteam)
#         self.size = agv_size
#         self.row_oders = []

#     def agv_list_fix(self, agv_list):
#         self.free_agv = list(set(self.free_agv)-set(agv_list))
        
#     def release_agv(self,agv_id):
#         self.free_agv.append(agv_id)
#         return self.order_process()

#     def agv_randomness(self,new_assign_agv):
#         return random.sample(self.free_agv, new_assign_agv)

#     def new_oderder(self,order):
#         self.row_oders.extend(order)
#         return self.order_process()

#     def order_process(self):
#         new_assign_agv = int(ceil(len(self.row_oders)/self.size))
#         if len(self.free_agv) < new_assign_agv:
#             new_assign_agv = len(self.free_agv)
#         print("number of agv = ",new_assign_agv,"   free =", self.free_agv)
#         agv_list = self.agv_randomness(new_assign_agv)
#         self.agv_list_fix( agv_list)

#         return agv_list

#     def rack__init__(self,X,Y,iteam_list):
#         #print(X,Y,iteam_list)
#         self.rack_iteam[Y][X] =   iteam_list
#         #print(self.rack_iteam)
#         #pass

from math import ceil

row_order = []
my_dict = {}

# function to assign each AGVs' jobs according to their payload capacity
def order_process(row_order, agv_size):
    agv_id = 0
    for x in row_order:
        tem = x[1]
        # oders are divided among AGVs according to their size
        # all AGVs are of fixed size
        while tem > agv_size :
            if agv_id in my_dict :
                tem2 = my_dict[agv_id]
                my_dict[agv_id] = [tem2, x[0]]

            else:
                my_dict[agv_id] = []
                my_dict[agv_id] = x[0]
            tem -= agv_size
            agv_id += 1

        if tem > 0 :
            my_dict[agv_id] = x[0]
           # my_dict[agv_id+1] = ''

    return my_dict


'''----- UNIT TESTING -----'''

if __name__ == "__main__":
    
    # row order
    row_order = [['r1', 100], ['r2', 80], ['r3', 15], ['r3', 35]]
    # dict to hold AGV ids with assigned orders
    my_dict = {}

    out = order_process( row_order=row_order , agv_size= 9 )
    print(out)

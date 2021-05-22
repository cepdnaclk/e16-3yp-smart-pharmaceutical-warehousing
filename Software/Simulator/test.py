# val = [0,0]

# arr = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5)]
#     , [(1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14)]
#     , [(1, 14), (1, 13), (1, 12), (1, 11), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10), (19, 11), (19, 12), (19, 13), (19, 14)]
#     , [(19, 14), (19, 13), (19, 12), (19, 11), (19, 10), (19, 9), (19, 8), (19, 7), (19, 6), (19, 5)], [(19, 5), (19, 4), (19, 3), (19, 2), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0)]]

# while (True):
#     subArr = bot.path[val[0]]
#     if  val[1] + 1 <= len(subArr):
#         print(arr[val[0]][val[1]])
#         val[1] += 1
#     else:
#         if val[0] +1 < len(arr):
#             val[0] += 1
#             val[1] = 0
#         else:
#             break


from math import ceil

row_order = [['r1', 5], ['r2', 10], ['r3', 15], ['r3', 20]]
my_dict = {0:[]}

def order_process(row_order, agv_size):
    agv_id = 0
    for x in row_order:
        tem = x[1]
        while tem > agv_size :
            if agv_id in my_dict :
                tem2 = my_dict[agv_id]
                my_dict[agv_id] = [tem2, x[0]]

            else:
                my_dict[agv_id] = x[0]
            tem -= agv_size
            agv_id += 1

        if tem > 0 :
            my_dict[agv_id] = x[0]
           # my_dict[agv_id+1] = ''

    return my_dict

out = order_process( row_order=row_order , agv_size= 9 )
print(out)



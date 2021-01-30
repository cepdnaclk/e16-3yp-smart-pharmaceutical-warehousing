import random
import numpy as np
import time

x1 = 2
y1 = 3
n = 5000
x = np.random.rand(n,1)
y = np.random.rand(n,1)



t1 = time.time()
min = 1000000
l = 0
for i in range(len(x)):
    z = np.sqrt((x[i] - x1)*(x[i] - x1) + (y[i] - y1)*(y[i] - y1))   
    if z <min:
        min = z 
        l = i
t2 = time.time()
print((t2 - t1)*1000, l)


t1 = time.time()
diffs =np.sqrt(np.square(x-x1) + np.square(y-y1))
z = np.where(diffs==np.min(diffs))
t2 = time.time()
print((t2 - t1)*1000,z[0])

n =10000000
a = np.zeros((n))
for i in range(n):
    a[i] = i 

t1 = time.time()
print(np.where(a == 90000)[0])
t2 = time.time()
print((t2 - t1)*1000)
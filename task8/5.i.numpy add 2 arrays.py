import numpy as np
a=int(input("enter the limit of arrays : "))
u=np.array([int(input("enter the elements of 1st array : ")) for i in range(a)])
v=np.array([int(input("enter the elements of 2nd array : ")) for i in range(a)])
print(u+v)
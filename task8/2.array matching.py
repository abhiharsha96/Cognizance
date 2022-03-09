import numpy as np
u=np.array([int(input("enter the elements of 1st array : ")) for i in range(6)])
v=np.array([int(input("enter the elements of 2nd array : ")) for i in range(6)])
print(u)
print(v)
print((u == v).all())
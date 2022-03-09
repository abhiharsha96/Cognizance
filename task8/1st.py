import numpy as n
a,b=int(input("First Number: ")),int(input("Second Number: ")); c=[]
for i in range(a,b+1): 
    c= n.append(c,[i,0,0,0,0,0]) if i!=b else n.append(c,b)
print(c)
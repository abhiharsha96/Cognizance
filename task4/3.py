lst=[]
for i in range(int(input("no.of std : "))):
 lst.append([int(input("Roll No : ")),input("Name : "),int(input("Marks : "))])
for i in lst:
 print()
 for j in i:
    print(j,end="   ")
for i in lst[int(input("\nEnter Row"))-1]:
 print(i,end="   ")


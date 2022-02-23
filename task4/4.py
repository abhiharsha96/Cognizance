num=int(input('Number: '))
temp=num
y=0
while(num>0):
    x=num%10
    y=y*10+x
    num=num//10
if(temp==y):
    print('True')
else:
    print('Not A Palindrome Number')
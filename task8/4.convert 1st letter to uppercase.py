import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' ,'chennai' , 'campus'])
print(ser)
for a in ser.str.title():
    print(a,end=" ")
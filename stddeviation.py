import math
import csv

with open('data.csv') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return(mean)

squareList=[]
for num in data:
    a=int(num)-mean(data)
    a=a**2
    squareList.append(a)

sum=0
for i in squareList:
    sum=sum+i 
result=sum/(len(data)-1)
standardDeviation=math.sqrt(result)
print(standardDeviation)
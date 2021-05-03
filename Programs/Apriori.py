import pandas as pd 

data=pd.read_csv("aprior.csv")
print(data)

items=data["LIST"]
print(items)

uniqueitems=[]
for i in items:
  for j in i.split(","):
    if j not in uniqueitems:
      uniqueitems.append(j)
print(uniqueitems)
n=len(uniqueitems)

from itertools import combinations 
flag=[]
for i in range(2,len(uniqueitems)):
  comb = combinations(uniqueitems, i) 
  for j in comb:
    flag.append(list(j))
print(flag) 
for i in flag:
  uniqueitems.append(i)

count=[]
p=0 
for k in uniqueitems:
  flag=0
  if p<n:
    p+=1
    for i in items:
      for j in i.split(","):
        if k==j:
          flag+=1
    count.append(flag)
    print(flag)
  else:
    for i in items:
      b=i.split(",")
      a=0
      for j in k:
        if j in b:
          a+=1
      if a==len(k):
        flag+=1
    count.append(flag)
    print(flag)
print(count)  

reldata=[]
for i in range(0,len(count)):
  if count[i]>=2:
    reldata.append([uniqueitems[i],count[i]])


print(reldata)







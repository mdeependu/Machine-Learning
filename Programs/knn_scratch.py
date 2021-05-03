import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Deependu Mandal\Desktop\knn.csv')

df = df.drop([13])
df = df.drop(labels='Index',axis=1)


df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df.head(15)

X = df.drop(labels='Purchase_Item',axis=1)

Y = df[['Purchase_Item']]

Y = pd.get_dummies(Y,drop_first=True)
X = pd.get_dummies(X,drop_first=True)
print(X)
print(Y)

X = X.to_numpy()
Y = Y.to_numpy()
print(X)
print(Y)

print(type(X),type(Y))

X_R = [45,50000,1,0]
X_R = np.array(X_R)

Distance=[]
for i in range(len(X)):
    print(X[i])
    dist = np.sqrt((X[i][0]-X_R[0])**2+(X[i][1]-X_R[1])**2+(X[i][2]-X_R[2])**2+(X[i][3]-X_R[3]))
    Distance.append(dist)
print(Distance)

K=5
index_sort=np.argsort(Distance)
print(index_sort)
print(Y)

countY,countN=0,0
for i in range(K):
    print(X[i])
    print(Y[i])
    if Y[i]=='Yes':
        countY=countY+1
        
    else:
        countN=countN+1
if(countN>countY):
    print("NO")
else:
    print("YES")
    
    
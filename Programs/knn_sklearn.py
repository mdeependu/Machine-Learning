import pandas as pd

df = pd.read_csv(r'C:\Users\Deependu Mandal\Desktop\knn.csv')

df = df.drop([13])
df = df.drop(labels='Index',axis=1)


df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df.head(15)

X = df.drop(labels='Purchase_Item',axis=1)
print(X)
Y = df[['Purchase_Item']]

Y = pd.get_dummies(Y,drop_first=True)
X = pd.get_dummies(X,drop_first=True)
print(X,Y)

val = [45,50000,1,0]

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(5)
knn.fit(X,Y)
Yp2 = knn.predict([val])
print(Yp2)
#Final Result with & without sklearn
label = ['No','Yes']
print("Predicted with sklearn : ",label[int(Yp2)])


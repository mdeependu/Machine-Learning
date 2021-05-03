import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r'C:\Users\A.SHESHUNARAYANA\Desktop\2 year\2 SEM\ml lab\lab2.csv')
data.head()
x_1=data.iloc[:,:1].values
x_2=data.iloc[:,1:2].values
x_3=data.iloc[:,2:3].values
y=data.iloc[:,-1:].values
l_1=[]
l_2=[]
l_3=[]
for i in range(len(x_1)):
    l_1.append(x_1[i])
    l_2.append(x_2[i])
    l_3.append(x_3[i])
y_p=[]
e=[]
for i in range(len(y)):
    y_hat=((0.014729726*l_1[i])+(0.371764998*l_2[i])+(0.56333258*l_3[i]))+6.051916364
    y_p.append(y_hat)
print(y_p)    
for i in range(len(y)):
    error=y_p[i]-y[i]
    e.append(error)
print(e)

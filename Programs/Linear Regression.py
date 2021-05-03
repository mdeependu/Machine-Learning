x=[1,2,3,4,5]
y=[2,4,5,4,5]

sum_X=sum(x)
print(sum_X)
sum_Y=sum(y)
print(sum_Y)

mean_X=(sum_X)/len(x)
mean_Y=(sum_Y)/len(y)

X_2=[]
for i in x:
    temp=i*i
    X_2.append(temp)
''''print(X_2)'''

sum_X_2=sum(X_2)
print(sum_X_2)

Y_2=[]
for i in y:
    temp=i*i
    Y_2.append(temp)
''''print(Y_2)''' 

sum_Y_2=sum(Y_2)
print(sum_Y_2)

X_Y=[]
for i in range(len(x)) :
    X_Y.append(x[i]*y[i])
'''print(X_Y)'''

sum_X_Y=sum(X_Y)
print(sum_X_Y)

m=((5*(sum_X_Y))-((sum_X)*(sum_Y)))/((5*(sum_X_2))-((sum_X)**2))
print(m)

c=(((sum_Y)*(sum_X_2))-((sum_X)*(sum_X_Y)))/((5*(sum_X_2)-(sum_X)**2))
print(c)

lin_reg=(m*(mean_X))+c
print(lin_reg)

print("\n")
Y_pred_1=(m*1)+c
Y_pred_2=(m*2)+c
Y_pred_3=(m*3)+c
Y_pred_4=(m*4)+c
Y_pred_5=(m*5)+c

Y_Ypred1=2-Y_pred_1
Y_Ypred2=4-Y_pred_2
Y_Ypred3=5-Y_pred_3
Y_Ypred4=4-Y_pred_4
Y_Ypred5=5-Y_pred_5

Y_Ypred1_2=(Y_Ypred1)**2
Y_Ypred2_2=(Y_Ypred2)**2
Y_Ypred3_2=(Y_Ypred3)**2
Y_Ypred4_2=(Y_Ypred4)**2
Y_Ypred5_2=(Y_Ypred5)**2

Y_pred_sum=(Y_Ypred1_2+Y_Ypred2_2+Y_Ypred3_2+Y_Ypred4_2+Y_Ypred5_2)
print(Y_pred_sum)

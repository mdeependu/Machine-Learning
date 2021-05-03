import pandas as pd

data=pd.read_csv(r"C:\Users\Deependu Mandal\Desktop\Baise.csv")
#print(data)
#data.describe()
#data.info()

X = data.iloc[:,:5].values
print(X)

def prediction(outlook,temperature,humidity,windy):
  count_O=0
  count_Oy=0
  count_T=0
  count_Ty=0
  count_H=0
  count_Hy=0
  count_W=0
  count_Wy=0
  county=0
  
  for i in X:
    
    if i[0] == outlook and  i[4] == "P":
      count_Oy+=1
    if i[0]==outlook:
      count_O+=1
    if i[1] == temperature and  i[4] == "P":
      count_Ty+=1
    if i[1]==temperature:
      count_T+=1
    if i[2] == humidity and  i[4] == "P":
      count_Hy+=1
    if i[2]==humidity:
      count_H+=1
    if i[3] == windy and  i[4] == "P":
      count_W+=1
    if i[3]==windy:
      count_Wy+=1
    if i[4] == "P":
      county+=1
  
  try:
    py= (count_Oy/count_O ) *(count_Ty/count_T ) *(count_Hy/count_H ) *(count_Wy/count_W ) *(county/len(X))
  except ZeroDivisionError:
    print("zero error")
  count_O=0
  count_Oy=0
  count_T=0
  count_Ty=0
  count_H=0
  count_Hy=0
  count_W=0
  count_Wy=0
  county=0  
  
  for i in X:
    
    if i[0] == outlook and  i[4] == "N":
      count_Oy+=1
    if i[0]==outlook:
      count_O+=1
    if i[1] == temperature and  i[4] == "N":
      count_Ty+=1
    if i[1]==temperature:
      count_T+=1
    if i[2] == humidity and  i[4] == "N":
      count_Hy+=1
    if i[2]==humidity:
      count_H+=1
    if i[3] == windy and  i[4] == "N":
      count_W+=1
    if i[3]==windy:
      count_Wy+=1
    if i[4] == "N":
      county+=1
  try:
    pn= (count_Oy/count_O ) *(count_Ty/count_T ) *(count_Hy/count_H ) *(count_Wy/count_W ) *(county/len(X))
  except ZeroDivisionError:
    print("zero error")
 
  p_yes=py/(py+pn)
  p_no=pn/(py+pn)
  if p_yes>p_no:
    print("yes")
  
  else:
    print("no")
 
  print(py,pn)
  print(p_yes,p_no)

prediction('sunny', 'hot', 'normal', False)


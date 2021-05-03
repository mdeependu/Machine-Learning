import pandas as pd

data = pd.read_csv(r'C:\Users\Deependu Mandal\Desktop\DIABETES.csv')

X=data.iloc[1:,:-1]
Y=data.iloc[1:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test=train_test_split(X,Y,test_size=.25,random_state=4)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

from sklearn import svm
#classifier= svm.SVC(kernel='linear', gamma='auto', C=2)
classifier= svm.SVC(kernel='poly', gamma='auto', C=2)

classifier.fit(x_train, y_train)

y_pred=classifier.predict(x_test)

score=classifier.score(x_test,y_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print("\nCONFUSION MATRIX\n")
print(cm)
accuracy = accuracy_score(y_test, y_pred)
print("\nACCURACY\n")
print(accuracy)

print("\nCLASSIFICATION REPORT")
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))




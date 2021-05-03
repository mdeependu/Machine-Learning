import pandas as pd

dataset = pd.read_csv(r'C:\Users\Deependu Mandal\Desktop\DIABETES.csv')

X = dataset.iloc[:,0:8].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

score=classifier.score(X_test,y_test)
print(score)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
'''accuracy = accuracy_score(y_test, y_pred)
print("\nACCURACY\n")
print(accuracy)
'''
print("\nCLASSIFICATION REPORT")
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


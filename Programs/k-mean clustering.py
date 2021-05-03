import pandas as pd

df=pd.read_csv(r'C:\Users\Deependu Mandal\Desktop\DIABETES.csv')

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=2)
kmeans.fit(df)

kmeans.cluster_centers_

def converter(cluster):
    
    if cluster=='Yes':
        return 1
    else:
        return 0
    
df['Cluster'] = df['Outcome'].apply(converter)
df.head()

from sklearn.metrics import confusion_matrix,classification_report
print("Confusion Matrix: \n",confusion_matrix(df['Cluster'],kmeans.labels_))
print(classification_report(df['Cluster'],kmeans.labels_))

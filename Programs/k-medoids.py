from k_medoids import KMedoids
import numpy as np
import matplotlib. pyplot as plt
import pandas as pd

def example_distance_func (data1, data2) :
    ''''example distance function.'''
    return np.sqrt(np.sum((data1 - data2)**2))

if __name__ == '__main__':
    
    data = pd.read_csv(r'C:\Users\Deependu Mandal\Desktop\DIABETES.csv')
    df=data.drop(['Outcome' ], axis = 1)
    X=df.iloc[:,0:7].values
    model = KMedoids(n_clusters=2, dist_func=example_distance_func)
    model.fit(X, plotit=True, verbose=True)
    plt.show( )
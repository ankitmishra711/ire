import numpy as np 
import pandas as pd 
from sklearn import preprocessing
# training set
df = pd.read_csv('totalSet.data',header=None)

x=df.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)
print "start"
df.to_csv('totalSet.data', sep=',',encoding='utf-8',header=None,index=False)
print "train set"

#testing set




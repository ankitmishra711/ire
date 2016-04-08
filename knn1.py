import pandas
from sklearn.neighbors import KNeighborsRegressor
import csv
import numpy as np
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn import datasets
import random
with open("trainSet.data", 'r') as csvfile:
    trainSet = pandas.read_csv(csvfile)
    #trainSet=list(trainSet)    
with open("trainLabel.data", 'r') as csvfile:
    trainLabel = pandas.read_csv(csvfile)

for k in range(1,20):
	
	m=max(.20,random.random())
	if m > .50:
		m=.20
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(trainSet, trainLabel, test_size=m, random_state=k)
	
	knn = KNeighborsRegressor(n_neighbors=k)
	#print len(trainSet)
	#print len(trainLabel)
	knn.fit(X_train,y_train)
	predictions = np.array([knn.predict(X_test)])
	actual = y_test
	print predictions.shape
	print actual.shape
	print len(predictions)
	mse = (((predictions - actual) ** 2).sum()) / len(predictions)
	print "mse for k",k,float(1-mse)
	





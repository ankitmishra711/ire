import pandas
from sklearn.neighbors import KNeighborsRegressor
import csv
from sklearn.cross_validation import KFold
import sklearn as sk
import sklearn.cross_validation as cv
from sklearn import tree
import numpy as np
from sklearn.naive_bayes import GaussianNB
#import pydot

with open("totalSet.data", 'r') as csvfile:
    trainSet = pandas.read_csv(csvfile)
    trainSet=trainSet.as_matrix()
    #trainSet=list(trainSet)    
with open("totalLabel.data", 'r') as csvfile:
    trainLabel = pandas.read_csv(csvfile)
	
    trainLabel=trainLabel.as_matrix()
'''
with open("testSet.data", 'r') as csvfile:
    testSet = pandas.read_csv(csvfile)
    testSet=testSet.as_matrix()
with open("testLabel.data", 'r') as csvfile:
    testLabel = pandas.read_csv(csvfile)	
    testLabel=testLabel.as_matrix()
'''
col=trainLabel.shape[0]


for k in range(1,30):
	
	kf = cv.KFold(col, n_folds=5)
	mylist = list(kf)	
	#train, test = mylist[0]
	sk.cross_validation.KFold(n=col, n_folds=5, shuffle=True,random_state=None)
	print "check1"
	
	for train_index, test_index in mylist:
		X_train, X_test, y_train, y_test =trainSet[train_index],trainSet[test_index],trainLabel[train_index],trainLabel[test_index]
		print "check2"
		gnb = GaussianNB()
		clf = tree.DecisionTreeClassifier()
		clf = gnb.fit(X_train,np.ravel(y_train))
		predictions=np.array([clf.predict(X_test)]).T
		actual = y_test
		print predictions.shape
		print actual.shape
		print len(predictions)
		p=(((predictions - actual) ** 2).sum())
		print p
		mse = p /(1.0* len(predictions))
		print "eFF for k",k,float(1-mse)
				
			

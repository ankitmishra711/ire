import pandas
from sklearn.neighbors import KNeighborsRegressor
import csv
from sklearn.cross_validation import KFold
import sklearn as sk
import sklearn.cross_validation as cv
from sklearn import svm
import numpy as np
with open("totalSet.data", 'r') as csvfile:
    trainSet = pandas.read_csv(csvfile)
    trainSet=trainSet.as_matrix()
    #trainSet=list(trainSet)    
with open("totalLabel.data", 'r') as csvfile:
    trainLabel = pandas.read_csv(csvfile)
    trainLabel=trainLabel.as_matrix()
col=trainLabel.shape[0]
for k in range(1,5):
	
	clf = svm.SVC(kernel='rbf', C = 1.0)	
	kf = cv.KFold(col, n_folds=5)
	mylist = list(kf)	
	#train, test = mylist[0]
	sk.cross_validation.KFold(n=col, n_folds=5, shuffle=True,random_state=None)
	print "check1"
	for train_index, test_index in mylist:
		X_train, X_test, y_train, y_test =trainSet[train_index],trainSet[test_index],trainLabel[train_index],trainLabel[test_index]
		print "check2"
		clf.fit(X_train,np.ravel(y_train))
		predictions=clf.predict(X_test)
		print "check3"
	
		predictions=np.array([predictions]).T
		print predictions.shape
		
		actual = y_test
		print actual.shape
		print len(predictions)
		p=(((predictions - actual) ** 2).sum())
		print p
		mse = p /(1.0* len(predictions))
		print "eFF for k",k,float(1-mse)




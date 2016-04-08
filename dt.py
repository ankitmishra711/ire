import pandas
from sklearn.neighbors import KNeighborsRegressor
import csv
from sklearn.cross_validation import KFold
import sklearn as sk
import sklearn.cross_validation as cv
from sklearn import tree
import numpy as np
#import pydot
import os
from sklearn.externals.six import StringIO  
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from subprocess import call
with open("trainSet.data", 'r') as csvfile:
    trainSet = pandas.read_csv(csvfile)
    trainSet=trainSet.as_matrix()
    #trainSet=list(trainSet)    
with open("trainLabel.data", 'r') as csvfile:
    trainLabel = pandas.read_csv(csvfile)
	
    trainLabel=trainLabel.as_matrix()
with open("testSet.data", 'r') as csvfile:
    testSet = pandas.read_csv(csvfile)
    testSet=testSet.as_matrix()
with open("testLabel.data", 'r') as csvfile:
    testLabel = pandas.read_csv(csvfile)	
    testLabel=testLabel.as_matrix()
col=trainLabel.shape[0]


for k in range(1,30):
	
		
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(trainSet,trainLabel )
	predictions=np.array([clf.predict(testSet)]).T
	actual = testLabel
	print predictions.shape
	print actual.shape
	print len(predictions)
	p=(((predictions - actual) ** 2).sum())
	print p
	mse = p /(1.0* len(predictions))
	print "eFF for k",k,float(1-mse)
	with open("tree.dot", 'w') as f:
		tree.export_graphviz(clf, out_file=f,max_depth=3)

	#call(["dot", "-Tpng", "tree.dot", "-o", "tree.png"])
	
	
	'''
	dot_data = StringIO()
	tree.export_graphviz(clf, out_file=dot_data)
	graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
	graph.write_pdf("dtree.pdf")
#	mylist = list(kf)	
	#train, test = mylist[0]
	#sk.cross_validation.KFold(n=col, n_folds=5, shuffle=True,random_state=None)
	print "check1"
	
	for train_index, test_index in mylist:
		X_train, X_test, y_train, y_test =trainSet[train_index],trainSet[test_index],trainLabel[train_index],trainLabel[test_index]
		print "check2"
		
		
		
		
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
	'''



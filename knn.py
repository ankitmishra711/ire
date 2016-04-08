import pandas
from sklearn.neighbors import KNeighborsRegressor
import csv
from sklearn.cross_validation import KFold
import sklearn as sk
import sklearn.cross_validation as cv
with open("trainSet.data", 'r') as csvfile:
    trainSet = pandas.read_csv(csvfile)
    trainSet=trainSet.as_matrix()
    #trainSet=list(trainSet)    
with open("trainLabel.data", 'r') as csvfile:
    trainLabel = pandas.read_csv(csvfile)
    trainLabel=trainLabel.as_matrix()
with open("testSet.data", 'r') as csvfile:
    testSet = pandas.read_csv(csvfile)
    
with open("testLabel.data", 'r') as csvfile:
    testLabel = pandas.read_csv(csvfile)
print trainSet.shape[0]
print trainLabel.shape[0]
col=trainLabel.shape[0]
for k in range(1,20):
	
	knn = KNeighborsRegressor(n_neighbors=k)	
	kf = cv.KFold(col, n_folds=5)
	print len(kf)
	mylist = list(kf)
	#train, test = mylist[0]
	sk.cross_validation.KFold(n=col, n_folds=5, shuffle=False,random_state=None)
	for train_index, test_index in mylist:
		X_train, X_test, y_train, y_test =trainSet[train_index],trainSet[test_index],trainLabel[train_index],trainLabel[test_index]
	
		knn.fit(X_train,y_train)
		predictions = knn.predict(X_test)
		print "pred",predictions.shape
		
		actual = y_test
		print "actual",actual.shape
		print len(predictions)
		mse = (((predictions - actual) ** 2).sum()) / len(predictions)
		print "eFF for k",k,float(1-mse)
	





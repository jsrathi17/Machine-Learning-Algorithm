import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB


def main():
	value_holder = np.genfromtxt("bmi.csv",delimiter=",")
	X= [[a[0],a[1]] for a in value_holder]
	y =[a[2] for a in value_holder]
	X= X[1:]
	y=y[1:]
	classifier = GaussianNB()
	classifier.fit(X,y)
	y_predicted = classifier.predict(X)
	correctly_predicted = np.sum(y == y_predicted)
	accuracy = correctly_predicted / len(y) * 100
	
	print(accuracy)
	
	
	
main()
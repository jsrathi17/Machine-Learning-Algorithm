import numpy as np
import csv
def leastsquare(X, y):
	num = np.dot(np.transpose(X),y)
	den = np.dot(np.transpose(X),X)
	try:
	    inverse = np.linalg.inv(den)

	except np.linalg.LinAlgError:
	    print("Not invertible")
	    return "Error"

	else:
		weight = np.dot(inverse, num)
		return weight

def test(X,y_test,w):
	y_predict = np.dot(X,w)
	error=np.sqrt(((y_predict-y_test) ** 2).mean())
	print (error)

def main():
	value_holder = np.genfromtxt("House_Data.csv",delimiter=",")
	X = [[1,a[1]] for a in value_holder]
	y = [a[2] for a in value_holder]
	X_train=X[1:61]
	X_test=X[61:]
	y_train=y[1:61]
	y_test = y[61:]
	W = leastsquare(X_train,y_train)
	test(X_test,y_test,W)
	

main()
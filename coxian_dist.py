import numpy as np 
import sys
import matplotlib.pyplot as plt 
from scipy.stats import poisson
 
def matrixPower(matData,pow):
	res = matData
	for i in xrange(1,pow+1):
		res = res*matData
	return res
def coxian(d):
	# This is a unimodal coxian probability mass function
	mu = np.array([0.16,0.11,0.04,0.32,0.36])	
	lmda = [0.07,0.62,0.43,0.64,0.18]
	#mu = np.array([0.11,0.25,0.01,0.31,0.32])
	#lmda =[0.58,0.64,0.46,0.25,0.41]
	A = np.matrix([[1-lmda[4],lmda[4],0.0,0.0,0.0],[0.,1-lmda[3],lmda[3],0.,0.],[0.,0.,1-lmda[2],lmda[2],0.],[0.,0.,0.,1-lmda[1],lmda[1]],[0.,0.,0.,0.,1-lmda[0]]])
	E = np.array([[0.],[0.],[0.],[0.],[lmda[0]]])
	tmp = np.transpose(mu)*(matrixPower(A,d-1))
	return tmp*E
def main():
	x = []
	y = []
	for i in xrange(100):
		x.append(i)
		tmp = coxian(i)
		print tmp[0,0]
		y.append(tmp[0,0])
	
	fig = plt.figure()
	plt.plot(x,y)
	plt.show()	


if __name__ == '__main__':
	main()

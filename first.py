import numpy as np
import matplotlib.pyplot as plt
import math 
import random
import sys
from scipy import signal

np.set_printoptions(threshold='nan')
def mean(signal):
	s = 0.0
	for i in signal:
		s = s + i
	return s/10.0


def MAF(arr):
	#for j in range(50000)
	for i in range(10,len(arr)):
		tmp = []
		for j in range(10):
			tmp.append(i-j)
		arr[i] = mean(tmp)
	return arr

def rms(signal):
	sum = 0.0 
	for i in signal:
		sum = sum + i*i
	return np.sqrt(sum/len(signal))
def rmsFilter(arr):
	for i in range(15,len(arr)):
		tmp =[]
		for j in range(15):
			tmp.append(arr[i-j])
		arr[i] = rms(tmp)
	return arr
	#print rms(tmp)

def butterworth(arr):
	pass
def analyze_data(arr):
	plt.plot(arr)
	print "Mean = " 
	print np.mean(arr)
	print "Peak is "
	print np.amax(arr)
	print "Area under the emg = "
	print np.trapz(arr)

def analyze_x(arr):
	data_x_1 = []
	for i in range(3500,6500):
		data_x_1.append(arr[i])
	data_x_2 = []
	for i in range(7500,10500):
		data_x_2.append(arr[i])
	data_x_3 = []
	for i in range(11500,14500):
		data_x_3.append(arr[i])
	data_x_4 = []
	for i in range(15500,18500):
		data_x_4.append(arr[i])
	data_x_5 = []
	for i in range(19500,22500):
		data_x_5.append(arr[i])

	filtered_data_x_1 = rmsFilter(data_x_1)
	filtered_data_x_2 = rmsFilter(data_x_2)
	filtered_data_x_3 = rmsFilter(data_x_3)
	filtered_data_x_4 = rmsFilter(data_x_4)
	filtered_data_x_5 = rmsFilter(data_x_5)
	#print filtered_x
	"""plt.plot(filtered_data_x_1)
	print np.mean(filtered_data_x_1)
	print np.amax(filtered_data_x_1)
	print np.trapz(filtered_data_x_1)
	plt.plot(filtered_data_x_2)
	print np.mean(filtered_data_x_2)
	print np.amax(filtered_data_x_2)
	print np.trapz(filtered_data_x_2)
	plt.plot(filtered_data_x_2)
	print np.mean(filtered_data_x_2)
	print np.amax(filtered_data_x_2)
	print np.trapz(filtered_data_x_2)
	"""
	analyze_data(filtered_data_x_1)
	analyze_data(filtered_data_x_2)
	analyze_data(filtered_data_x_3)
	analyze_data(filtered_data_x_4)
	analyze_data(filtered_data_x_5)
if __name__=='__main__':
	with open(sys.argv[1],'r') as data_file:
		data=[]
		x=[]
		y=[]
		z=[]
		k=[]
		for line in data_file:
			tmp = line.strip().split() 
			data.append(tmp)
			x.append(abs(float(tmp[1])))
			y.append(abs(float(tmp[2])))
			z.append(abs(float(tmp[3])))
			k.append(abs(float(tmp[4])))

	#print len(data),len(x),len(y),len(z),len(k)
	#filtered_x = rmsFilter(x)		#MAF(x)
	
	analyze_x(x)
	#plt.plot(y)
	plt.show()

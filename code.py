## Generic code for Linear Regression
import sys
import os
import matplotlib.pyplot as plt
### Functions

def summation(lst):
	sumn = 0
	for i in lst:
		sumn = sumn + i
	return sumn

def changedValues(m1,m2,x1,x2,y,alp):
	IV1 = 0
	IV2 = 0 
	for i in range(0,len(x1)):
		IV1 = IV1 + ( ( y[i] - (m1*x1[i]) - (m2*x2[i]) ) * x1[i] )
		IV2 = IV2 + ( ( y[i] - (m1*x1[i]) - (m2*x2[i]) ) * x2[i] )
		m1=m1-(alp*(-2)*IV1)
		m2=m2-(alp*(-2)*IV2)
	return [m1,m2]
### Input

fileObject = open("train.txt","r+")
lines = fileObject.readlines()
fileObject.close()

x1=[]
x2=[]
y=[]

for line in lines:
	if line.strip() == "" : break 
	lineSep = line.split("\t")
	x1.append(lineSep[0].strip())
	x2.append(lineSep[1].strip())
	y.append(lineSep[2].strip())
	
### Verify Lengths

if len(x1) != len(x2):
	print "Error Do No Proceed. Absurd Results maybe met"
	sys.exit
if len(x2) != len(y):
	print "Error Do not Proceed"
	sys.exit()

### Convert all inputs to integer data type
for i in range(0,len(x1)):
	x1[i]=int(x1[i])
	x2[i]=int(x2[i])
	y[i]=int(y[i])


### Initialize Constants

m1 = 10
m2 = 10


apl = float(sys.argv[1])
max_iter = int(sys.argv[2])


### Main Source Code

iteration = 0
delt_hist = []		##delt_hist is summation of all delta per iteration

while(iteration<max_iter):
	print "Iteration Number = "+str(iteration)
	delta = [] 	## Delta is the difference between Actual output to calculate output. In our case Y - M1*X1 - M2*X2
	for i in range(0,len(x1)):
		delt = (y[i] - (m1*x1[i]) - (m2*x2[i]))
		delt = delt ** 2
		delta.append(delt)				
	delt_hist.append(summation(delta))	
	print "Error in this iteration = "+str(summation(delta))
	print "Details passed are :"
	print "m1="+str(m1)
	print "m2="+str(m2)
	print "x1="+str(x1)
	print "x2="+str(x2)
	[m1,m2] = changedValues(m1,m2,x1,x2,y,apl)
	iteration = iteration + 1
	
plt.plot(delt_hist)
plt.ylabel('Difference Sum Sqaured')
plt.xlabel('No of Iterations')
plt.show()









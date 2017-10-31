# Apk_ML

The file code.py is a linear regression code which can work with two variables x1 and x2 and an output y

The code takes input from the file train.txt a sample of which is shown.
The format of the file is
x1_1  x2_1  y_1
x2_2  x2_2  y_2
....
....
x1_n  x2_n y_n
where values are seperated by tab.

The code outputs m1 and m2 where m1 and m2 are variables which satisfies the equation:

y = (m1*x1) + (m2*x2)
for all given testcases with minimum possible error.

The syntax to run a test case is as follows

python code.py <learning_rate> <max_iterations>

Learning rate and Max number of iteration to be followed is to be adjusted suitably. View the plot generated at the end of the code.

In the plot if :
The graph does not decrease, decrease the learning rate
The graph decreases but does not reaches sufficiently close to zero, increase the number of iterations.



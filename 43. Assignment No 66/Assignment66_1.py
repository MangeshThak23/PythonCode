import numpy as np

input = np.array([2.0, 3.0])
weights = np.array([0.4, 0.6])
bias = 0.5

#Calculate weighted sum
z = np.dot(input, weights) + bias
print("Weighted sum is: ",z)

#Activate sigmoid function
def Sigmoid(z):
    return 1 / (1 + np.exp(-z))

#Function call
output = Sigmoid(z)
print("Final output is: ",output)

#Check whether output is close to 0 or 1.
if 0.50 >= output:
    print("Output is close to 0.")
else:
    print("Output is close to 1.")

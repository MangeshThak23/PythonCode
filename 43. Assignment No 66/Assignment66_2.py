import numpy as np
import matplotlib.pyplot as plt

input_data = np.array([-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0, 
                      1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

def Sigmoid(x):
    """Sigmoid is used for binary classification to show the output in probabilities (0 to 1)."""
    return 1 / (1 + np.exp(-x))

Sigmoid_out = Sigmoid(input_data)
print("Sigmoid output: ",Sigmoid_out)
print("")

def ReLu(x):
    """ReLu is used in hidden layers for non-linearity and it will returns the negative value to 0 and keep positive as it is."""
    return np.maximum(0,x)

ReLu_out = ReLu(input_data)
print("ReLu Output: ", ReLu_out)
print("")

def Tanh(x):
    """Recurrent neural networks (zero-centered outputs between -1 and 1)."""
    return np.tanh(x)

Tanh_out = Tanh(input_data)
print("Tanh Output: ",Tanh_out)
print()

plt.figure(figsize=(10,6))

plt.plot(input_data, Sigmoid_out, label = "sigmoid", marker = "o")
plt.plot(input_data, ReLu_out, label = "relu", marker = "s")
plt.plot(input_data, Tanh_out, label = "tanh", marker = "*")

plt.title("Activation Functions")

plt.xlabel("Input data")
plt.ylabel("Output data")
plt.grid()
plt.legend()
plt.show()

print("Sigmoid use case: ")
print(Sigmoid.__doc__)
print("*"*50)

print("Relu use case: ")
print(ReLu.__doc__)
print("*"*50)

print("tanh use case: ")
print(Tanh.__doc__)
print("*"*50)

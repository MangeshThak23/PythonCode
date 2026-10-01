x = 2.0
weight = 0.5
bias = 0.3
target = 1.0
learning_rate = 0.1

Y_pred = (x * weight) + bias
print("Prediction is: ",Y_pred)

calculated_error = Y_pred - target
print("Calculated error is: ",calculated_error)

gradient = calculated_error * x

updated_weight = weight - (learning_rate * gradient)
print(f"Initial weight is: {weight} and Updated weight is: {updated_weight}")


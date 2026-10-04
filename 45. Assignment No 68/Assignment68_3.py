import numpy as np

# Task 1: 2D Matrix Input
matrix = [
    [6, 4],
    [8, 6]
]

print("--- Task 1: Input 2D Matrix ---")
for row in matrix:
    print(row)
print()

# Task 2: Convert 2D Matrix into a 1D Vector (Flattening)
flatten_output = []
for row in matrix:
    for val in row:
        flatten_output.append(val)

# Alternatively using NumPy: flatten_output = np.array(matrix).flatten()

print("--- Task 2: Flattened 1D Output ---")
print(f"flatten_output = {flatten_output}\n")

# Task 3 & 4: Pass to Fully Connected Layer & Calculate Output Manually
# Dense layer with 1 output neuron, 4 weights (one per feature), and 1 bias
weights = np.array([0.5, -0.2, 0.1, 0.3])
bias = 1.0

# Manual calculation: Output = (w1*x1 + w2*x2 + w3*x3 + w4*x4) + bias
x = np.array(flatten_output)

# Step-by-step dot product terms
terms = [f"({w} * {val})" for w, val in zip(weights, x)]
dot_product = np.dot(x, weights)
final_output = dot_product + bias

print("--- Task 3 & 4: Fully Connected Layer Calculation ---")
print(f"Weights             : {weights.tolist()}")
print(f"Bias                :    {bias}")
print("\nCalculation        :")
print(" + ".join(terms) + f" + {bias}")
print(f"= ({6*0.5}) + ({4*-0.2}) + ({8*0.1}) + ({6*0.3}) + {bias}")
print(f"= {3.0} + ({-0.8}) + {0.8} + {1.8} + {bias}")
print(f"Final Output Value = {final_output:.2f}")
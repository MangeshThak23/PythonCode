# 1. Input Feature Map (3x3)
feature_map = [
    [ 3,  3,  3],
    [ 0,  0,  0],
    [-3, -3, -3]
]

print("--- Step 1: Input Feature Map ---")
for row in feature_map:
    print(row)
print()

# 2. Apply ReLU Activation (Task 2)
# ReLU Rule: f(x) = max(0, x)
rows = len(feature_map)
print(rows)
cols = len(feature_map[0])

relu_output = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        relu_output[i][j] = max(0, feature_map[i][j])

# 3. Display ReLU Output (Task 4)
print("--- Step 2: Output After ReLU ---")
for row in relu_output:
    print(row)
print()

# 4. Apply 2x2 Max Pooling (Task 3)
# Pooling kernel size: 2x2, Stride: 1 
# With a 3x3 input and 2x2 filter (stride=1, valid padding), output size is (3-2+1) x (3-2+1) = 2x2

pool_size = 2
stride = 1

out_rows = (rows - pool_size) // stride + 1
print("pool",out_rows)
out_cols = (cols - pool_size) // stride + 1
print("pool",out_cols)

pooled_output = [[0 for _ in range(out_cols)] for _ in range(out_rows)]

print("--- Step 3: Max Pooling Calculations (2x2 Patch) ---")
for i in range(out_rows):
    for j in range(out_cols):
        # Extract 2x2 region
        region = [
            relu_output[i][j],     relu_output[i][j+1],
            relu_output[i+1][j],   relu_output[i+1][j+1]
        ]
        max_val = max(region)
        pooled_output[i][j] = max_val
        print(f"Region at ({i},{j}): {region} -> Max = {max_val}")

print()

# 5. Display Final Pooled Output (Task 4)
print("--- Step 4: Final Output After 2x2 Max Pooling ---")
for row in pooled_output:
    print(row)
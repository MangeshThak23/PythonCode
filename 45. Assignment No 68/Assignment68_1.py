# 1. Input Image (5x5) and Kernel (3x3)
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

# Image and Kernel dimensions
img_rows = len(image)
print(img_rows)
img_cols = len(image[0])
print(img_cols)
k_rows = len(kernel)
k_cols = len(kernel[0])

# Feature map dimensions: Output size = (N - M + 1)
out_rows = img_rows - k_rows + 1
print(out_rows)

out_cols = img_cols - k_cols + 1
print(out_cols)
# Initialize empty feature map
feature_map = [[0 for _ in range(out_cols)] for _ in range(out_rows)]
print("fm",feature_map)

print("--- Region Calculations ---\n")

# 2. Perform Convolution (Task 1, 2 & 4)
for i in range(out_rows): 
    for j in range(out_cols):
        region_sum = 0
        calc_terms = []
        
        # Overlay 3x3 kernel on current image patch
        for m in range(k_rows):
            for n in range(k_cols):
                pixel_val = image[i + m][j + n]
                kernel_val = kernel[m][n]
                
                prod = pixel_val * kernel_val
                region_sum += prod
                calc_terms.append(f"{pixel_val}*{kernel_val}")
        
        feature_map[i][j] = region_sum
        
        # Task 4: Print calculation details for each region
        print(f"Region at output index ({i}, {j}):")
        print(" + ".join(calc_terms))
        print(f"Output = {region_sum}\n")

# 3. Print Final Feature Map (Task 3)
print("--- Final Feature Map ---")
for row in feature_map:
    print(row)
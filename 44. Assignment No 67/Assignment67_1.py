import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


np.random.seed(42)
tf.random.set_seed(42)

# -----------------------------------------------------------------------------
# Task 1: Load/Create Dataset
# -----------------------------------------------------------------------------
# Features: [Age, Monthly charges, Tenure, Number of complaints, Customer support calls]
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# -----------------------------------------------------------------------------
# Task 2: Clean the Dataset
# -----------------------------------------------------------------------------
# Check for null or missing values

print("Check null values per colummn: ",np.isnan(X).sum())

# -----------------------------------------------------------------------------
# Task 3: Apply StandardScaler
# -----------------------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------------------------------------------------------
# Task 4: Train Feedforward Neural Network (FNN) Model
# -----------------------------------------------------------------------------
print("Shape of features: ",X.shape)
model = Sequential([
    Dense(8, activation='relu'),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X_scaled, y, epochs=150, verbose=0)

# -----------------------------------------------------------------------------
# Task 5: Evaluate Accuracy
# -----------------------------------------------------------------------------
loss, accuracy = model.evaluate(X_scaled, y, verbose=0)
print(f"Training Accuracy: {accuracy * 100:.2f}%\n")

# -----------------------------------------------------------------------------
# Test Input Prediction
# -----------------------------------------------------------------------------
new_customer = np.array([[46, 1450, 5, 6, 0]])

# Scale the test sample using the fitted scaler
new_customer_scaled = scaler.transform(new_customer)


probability = model.predict(new_customer_scaled, verbose=0)[0][0]

if probability >=0.5:
    print("The probability is: ",probability)
    print("Prediction: customer will leave. ")

else:
    print("The probability is: ",probability)
    print("Prediction: customer will not leave. ")


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt 
from sklearn.metrics import accuracy_score,confusion_matrix

Border = "-"*100

##############################################
# Step 1: DataSet loading
##############################################

DataSet = "student_performance_ml.csv"

df = pd.read_csv(DataSet)
print(Border)
print(f"DataSet loaded successfully: \n\n{df.head()}\n")
print(Border)

#################################################
# Step 2: Data analysis(EDA)
#################################################

print("Data analysis:")

print("\nShape of dataset: ",df.shape)
print("\nColumn names: \n",list(df.columns))
print("\nNull value details: ",df.isnull().sum())
print(df["FinalResult"].value_counts())
print(df.describe())
print(Border)

#################################################
# Step 3: Decide Independent & Dependent Variables.
#################################################

print("Decide Independent & Dependent Variables:")

Feature_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[Feature_cols]
Y = df["FinalResult"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)
print(Border)

#################################################
# Step 4: Visualisation of dataset.
#################################################

print("Visualisation of dataset.")

plt.figure(figsize=(7,5))
for st in df["FinalResult"].unique():
    temp = df[df["FinalResult"]==st]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],label=st)

plt.title("Student performance case study.")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.legend()
plt.grid()
plt.show()
print(Border)

#################################################
# Step 5: Split dataset for training and testing.
#################################################

print("Split dataset for training and testing:")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("X: ",X.shape)
print("Y: ",Y.shape)

print("X_train",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)
print(Border)

#################################################
# Step 6: Build the model.
#################################################
model = DecisionTreeClassifier(max_depth=3)

#################################################
# Step 7: Train the model.
#################################################
model.fit(X_train,Y_train)

#################################################
# Step 8: Test the model.
#################################################
Y_pred = model.predict(X_test)

#################################################
# Step 9: Evaluate the model performance.
#################################################

accuracy = accuracy_score(Y_test,Y_pred)*100
print(f"The accuracy of model is: {accuracy:.2f}%\n")

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix: \n",cm)
print(Border)

#################################################
# Step 10: Final conclusion.
#################################################

print("FINAL CONCLUSION:")
print("1. Data loading and EDA completed with no missing values found.")
print("2. Features selected and dataset successfully split into 80% train and 20% test sets.")
print(f"3. Decision Tree Classifier trained with max_depth=3 achieved {accuracy:.2f}% accuracy.")
print("4. Confusion matrix shows the distribution of true vs predicted labels.")
print(Border)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


Border = "-"*60

#########################################################
# Question 1: 1. After training the Decision Tree model, use:
# model.feature_importances_
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?
#########################################################

print(Border)
print("Data Set Load")
print(Border)

DataSet = "student_performance_ml.csv"

df = pd.read_csv(DataSet)

print("Data analysis")

print("Shape of dataset: ", df.shape)
print("Column names: ",list(df.columns))
print(df.isnull().sum())
print(df["FinalResult"].value_counts())
print(df.describe())

print("Independent and Dependent Variables")

Feature_Cols = ["StudyHours","Attendance",
                "PreviousScore","AssignmentsCompleted",
                "SleepHours"
                ]

X = df[Feature_Cols]
Y = df["FinalResult"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

print("Split the dataset for training and testing.")

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

model = DecisionTreeClassifier(max_depth=5)
print("Model has been built.")

model.fit(X_train,Y_train)
print("Model has been trained.")

Importance = model.feature_importances_
for feature, score in zip(X.columns, model.feature_importances_):
    print(f"{feature} : {score:.2f}")

Importance_dict = dict(zip(X.columns, model.feature_importances_))

most_important = max(Importance_dict, key=Importance_dict.get)
least_important = min(Importance_dict, key=Importance_dict.get)

print("most in predicting FinalResult: ",most_important)
print("least in predicting FinalResult: ",least_important)

Y_pred = model.predict(X_test)
accuracy_prev = accuracy_score(Y_test, Y_pred)
print("Accuracy of model is: ",accuracy_prev*100)


######################################################
#2. Remove the column SleepHours from the dataset.
# Train the model again.
# Compare new accuracy with previous accuracy.
# Does removing this feature affect performance?
######################################################

print("\n2. Remove the column SleepHours from the dataset.")

X_After = df[Feature_Cols].drop(columns=["SleepHours"])

Y_After  = df["FinalResult"] 

X_train2,X_test2,Y_train2,Y_test2 = train_test_split(X_After,Y_After,test_size=0.20,random_state=42)


model_new = DecisionTreeClassifier(max_depth=5)

model_new.fit(X_train2,Y_train2)

Y_NewPred = model_new.predict(X_test2)
accuracy_new = accuracy_score(Y_test2,Y_NewPred)
print("Accuracy of model is: ",accuracy_new*100)

if accuracy_prev == accuracy_new:
    print("Does not affect on accuracy after removing SleepHours column.")
else:
    print("Affected on accuracy after removing SleepHours column.")


#################################################################
#3. Train the model using only:
# StudyHours
# Attendance
#Compare the accuracy with the full-feature model.
#Is the model still performing well?
##################################################################


print("\n3. Train the model using only: StudyHours and Attendance")

X_After1 = df[["StudyHours","Attendance"]]

Y_After1  = df["FinalResult"] 


X_train3,X_test3,Y_train3,Y_test3 = train_test_split(X_After1,Y_After1,test_size=0.20,random_state=42)

model_new1 = DecisionTreeClassifier(max_depth=5)

model_new1.fit(X_train3,Y_train3)

Y_NewPred1 = model_new1.predict(X_test3)
accuracy_new1 = accuracy_score(Y_test3,Y_NewPred1)
print("Accuracy of model is: ",accuracy_new1*100)

if accuracy_prev == accuracy_new1:
    print("Accuracy is identical to the full-feature model after comparison.")
else:
    print("Affected on accuracy.")


#####################################################################
#4. Create a new DataFrame with details of 5 new students.
#Use the trained model to predict their results.
#Display predictions clearly.
#####################################################################
print(Border)
print("New dataframe\n")
print(Border)

New_DataSet = {"StudyHours":[2.5,6,5,3,1],"Attendance":[90,91,92,93,94],
                "PreviousScore":[60,61,62,63,64],"AssignmentsCompleted":[2,1,3,4,5],
                "SleepHours":[7,8,9,10,12]}

df_new_students = pd.DataFrame(New_DataSet)

predictions = model.predict(df_new_students)

df_new_students["PredictedResult"] = predictions

df_new_students["Result_Label"] = df_new_students["PredictedResult"].map({1: "Pass", 0: "Fail"})

print(df_new_students)




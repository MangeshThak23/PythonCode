from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


Border = "-"*60
################################################
#1. Import DecisionTreeClassifier from sklearn.
#Create a model object and train it using fit().
################################################

DataPath = "student_performance_ml.csv"

print(Border)
print("\nDataset loaded")
print(Border)

df = pd.read_csv(DataPath)

Feature_Cols = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

X = df[Feature_Cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.5,random_state=42)

model = DecisionTreeClassifier(max_depth=5,random_state=42)

model.fit(X_train,Y_train)

#############################################################
#2. Use the trained model to predict results for X_test.
#Display predicted values along with actual values.
##############################################################

Y_pred = model.predict(X_test)


print(Border)
print("Predicted values along with actual values: ")
print(Border)

result_df = pd.DataFrame({"Actual_Values":Y_test.values,"Predicted":Y_pred})

print(result_df.to_string(index=False))

#########################################################
#3. Calculate model accuracy using accuracy_score.
#Display the result in percentage format.
##########################################################

accuracy = accuracy_score(Y_test,Y_pred)

print(Border)
print(f"Accuracy is: {(accuracy*100):.2f}%")
print(Border)


##############################################################
# 4. Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.
# Explain clearly:
# • True Positive
# • True Negative
# • False Positive
# • False Negative
##############################################################
print(Border)
print("Confusion matrix")
print(Border)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion matrix\n",cm)

display = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
display.plot(cmap=plt.cm.Blues)
plt.title("Display matrix")
plt.show()

if cm.shape == (2,2):
    tn, fp, fn, tp = cm.ravel()
    print("Confusion matrix explanation:")
    print(f"True negative: {tn}")
    print(f"False negative: {fn}")
    print(f"True positive: {tp}")
    print(f"False positive: {fp}")
else:
    print("Explanation skipped.")

################################################################################################
# 5. Calculate:
# • Training accuracy
# • Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.
################################################################################################

print(Border)
print("Calculate training and testing accuracy.")
print(Border)

Y_train_pred = model.predict(X_train)

train_accuracy = accuracy_score(Y_train,Y_train_pred)*100
test_accuracy = accuracy_score(Y_test,Y_pred)*100

print(f"Train accuracy: {train_accuracy:.2f}%")
print(f"Test accuracy: {test_accuracy:.2f}%")

print(Border)

if train_accuracy - test_accuracy > 10:
    print("Model is overfitting.")

elif train_accuracy < 70:
    print("Model is underfitting.")

else:
    print("Model is well balanced.")



####################################################
# #6. Train three Decision Tree models with:
# • max_depth = 1
# • max_depth = 3
# • max_depth = None
# Compare their testing accuracies and write your observations.
#####################################################

print(Border)
print("Train the model with different max_depth.")
print(Border)

model1 = DecisionTreeClassifier(max_depth=1, random_state=42)
model1.fit(X_train,Y_train)
Y_pred1 = model1.predict(X_test)
accuracy1 = accuracy_score(Y_test,Y_pred1)*100
print(f"Accuracy with max_depth 1 is: {accuracy1:.2f}%")

model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train,Y_train)
Y_pred2 = model2.predict(X_test)
accuracy2 = accuracy_score(Y_test,Y_pred2)*100
print(f"Accuracy with max_depth 3 is: {accuracy2:.2f}%")

model3 = DecisionTreeClassifier(max_depth=None, random_state=42)
model3.fit(X_train,Y_train)
Y_pred3 = model3.predict(X_test)
accuracy3 = accuracy_score(Y_test,Y_pred3)*100
print(f"Accuracy with max_depth None is: {accuracy3:.2f}%")

# ##############################################################
# 7. Use the trained model to predict result for a student with:
# • StudyHours = 6
# • Attendance = 85
# • PreviousScore = 66
#• AssignmentsCompleted = 7
# • SleepHours = 7
# Will the student Pass or Fail?
#################################################################

print(Border)
print("To predict the new student data.")
print(Border)

new_student = pd.DataFrame(
    [
        {
            "StudyHours" : 6,
            "Attendance": 85,
            "PreviousScore" : 66,
            "AssignmentsCompleted" : 7,
            "SleepHours" : 7
        }
    ]
)

prediction = model.predict(new_student)[0]
if prediction == 1:
    print("Student will pass")
else:
    print("Student will fail")


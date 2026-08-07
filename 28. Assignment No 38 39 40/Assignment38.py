import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

Border = "-"*50

################################################################
# Step 1 : Load the dataset and display the required details.
################################################################

print(Border)
print("Step 1 : Load the dataset and display the required details.")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print(df.head(),"\n")
print(df.tail(),"\n")
print("Total number of rows and columns: ",df.shape)
print("\n List of column names: ",list(df.columns))
print("\n Data types of each column: ",df.dtypes)

print("Total number of students in dataset is: ",df["FinalResult"].count())
print("Count how many students Passed (FinalResult = 1): ",(df["FinalResult"]==1).sum())
print("Count how many students Failed (FinalResult = 0): ",(df["FinalResult"]==0).sum())

print("Average StudyHours: ",df["StudyHours"].mean())
print("Average Attendance: ",df["Attendance"].mean())
print("Maximum PreviousScore: ",df["PreviousScore"].max())
print("Minimum SleepHours: ",df["SleepHours"].min())

################################################################
# Step 2 : Data Analysis (EDA).
################################################################

print(Border)
print("Step 2 : Data Analysis (EDA).")
print(Border)

print("Null data:\n",df.isnull().sum())

print(df["FinalResult"].value_counts())

percentages = df["FinalResult"].value_counts(normalize=True)*100

pass_percentages = percentages[1]
fail_percentages = percentages[0]
print(f"Percentage of pass students: {pass_percentages:.2f}%")
print(f"Percentage of fail students: {fail_percentages:.2f}%")

if 40 <= pass_percentages <=60:
    print("Dataset is balanced.")
    print("Pass and fail distribution is almost equally.")
else:
    print("Dataset is not balanced.")
    print("Pass and fail distribution is not equally.")

education_summary = df.groupby("FinalResult")[["StudyHours","Attendance"]].mean()

print(education_summary)

################################################################
# Step 3 : Visualisation of dataset.
################################################################

print(Border)
print("Step 3 : Visualisation of dataset.")
print(Border)

plt.figure(figsize=(7,5))

plt.hist(df["StudyHours"], bins=10, color='skyblue', edgecolor='black')

plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours (per day)")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.75)
plt.show()

for fr in df["FinalResult"].unique():
    temp =df[df["FinalResult"] == fr]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"], label="Pass (1)" if fr == 1 else "Fail (0)")

plt.title("Scatter plot of StudyHours vs PreviousScore")
plt.xlabel("Study hours")
plt.ylabel("Previous score")
plt.legend()
plt.grid()
plt.show()


# Question 8: Boxplot for Attendance
plt.figure(figsize=(6, 5))
plt.boxplot(df["Attendance"], patch_artist=True)
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance (%)")
plt.grid(axis="y")
plt.show()

# IQR Calculation for Outliers
Q1 = df["Attendance"].quantile(0.25)
Q3 = df["Attendance"].quantile(0.75)
IQR = Q3 - Q1
outliers = df[
    (df["Attendance"] < (Q1 - 1.5 * IQR)) | (df["Attendance"] > (Q3 + 1.5 * IQR))
]
print(f"Total outliers in Attendance: {len(outliers)}")


plt.figure(figsize=(8, 5))
sns.countplot(data = df, x= "AssignmentsCompleted", hue= "FinalResult",hue_order=[0, 1])
plt.title("Relationship between AssignmentsCompleted and FinalResult.")
plt.xlabel("Assignment Completed")
plt.ylabel("Number of students")
plt.legend(title = "FinalResult", labels=["Fail (0)","Pass (1)"])
plt.grid(axis="y")
plt.show()


#question 10 pending
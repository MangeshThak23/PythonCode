import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

Border = "-"*50

print(Border)
df = pd.read_csv("Customer_Loan_Approval.csv")

print("Shape of dataset: ",df.shape)
print("First 5 records from a dataset:")
print(df.head())

print(Border)

#Step 2: Check missing values
print("\nMissing values:")
print(df.isnull().sum())

print(Border)

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

    #Logistic Regression Classifier
model_LR = LogisticRegression(max_iter=1000)
model_LR = model_LR.fit(X_train,Y_train)
pred_LR = model_LR.predict(X_test)
accuracy_LR = accuracy_score(Y_test,pred_LR)
print("Accuracy of LR: ",accuracy_LR)

    #Decision Tree Classfier
model_DT = DecisionTreeClassifier(random_state=42)
model_DT = model_DT.fit(X_train,Y_train)
pred_DT = model_DT.predict(X_test)
accuracy_DT = accuracy_score(Y_test,pred_DT)
print("Accuracy of DT: ",accuracy_DT)

    #KNN Classfier
model_KN = KNeighborsClassifier(n_neighbors=5)
model_KN = model_KN.fit(X_train,Y_train)
pred_KN = model_KN.predict(X_test)
accuracy_KN =accuracy_score(Y_test,pred_KN)
print("Accuracy of KNN: ",accuracy_KN)

models = [("logistic", model_LR), ("decision_tree", model_DT), ("knn", model_KN)]
scores = {"LR": accuracy_LR, "DT": accuracy_DT, "KNN": accuracy_KN}

model_LRObj = LogisticRegression(max_iter=1000)
model_KNObj = KNeighborsClassifier(n_neighbors=5)
model_DTObj = DecisionTreeClassifier(random_state=42)

model_hard = VotingClassifier(
    estimators=
    [
        ("logistic",model_LRObj),
        ("decision_tree",model_DTObj),
        ("knn",model_KNObj)
    ],
    voting="hard",
    )

model_soft = VotingClassifier(
    estimators=
    [
        ("logistic",model_LRObj),
        ("decision_tree",model_DTObj),
        ("knn",model_KNObj)
    ],
    voting="soft",
    )

model_hard = model_hard.fit(X_train,Y_train)
pred_hard = model_hard.predict(X_test)
accuracy_hard = accuracy_score(Y_test,pred_hard)

model_soft = model_soft.fit(X_train,Y_train)
pred_soft = model_soft.predict(X_test)
accuracy_soft = accuracy_score(Y_test,pred_soft)

print("Accuracy for hard: ",accuracy_hard)
print("Accuracy for soft: ",accuracy_soft)










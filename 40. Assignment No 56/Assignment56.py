import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

from sklearn.preprocessing import StandardScaler

#Step 1: Load dataset
df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Shape of dataset: ",df.shape)
print("First 5 data from a dataset: ",df.head())

#Step 2: Split Dataset
X = df.drop("Fraud",axis=1)
Y = df["Fraud"]

print("Shape of X: ",X.shape)
print("Shape of Y: ",Y.shape)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

base_DT = DecisionTreeClassifier(random_state=42)

base_RF = RandomForestClassifier(n_estimators=10)

model_vote = VotingClassifier(
    estimators = [
        ("decision_tree",base_DT),
        ("randonforest",base_RF)
        
    ],
    voting = "hard"
)

model = BaggingClassifier(
    estimator = {"Hard Voting":model_vote,"DecisionTree":base_DT,"RandomForest":base_RF},
        n_estimators = 10
)


#----------------------------------
#Step 6: Train the model
#--------------------------------------

model = model.fit(X_train,Y_train)

#--------------------------------------
#Step 7: Test the model
#--------------------------------------

Y_pred = model.predict(X_test)

#--------------------------------------
#Step 8: Evaluate the model
#--------------------------------------

accuracy = accuracy_score(Y_test,Y_pred)*100
c_report = classification_report(Y_test,Y_pred)
cm = confusion_matrix(Y_test,Y_pred)
print("Decision Tree")
print()
print("Confusion matrix: ")
cm_data = {"Decision Tree":base_DT.cm}

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

Border = "-"*50

#Step 1: Load the dataset
def LoadDataset(DataPath):

    print(Border)

    df = pd.read_csv(DataPath)

    print("Shape of dataset: ",df.shape)
    print("First 5 records from a dataset:")
    print(df.head())

    print(Border)

    #Step 2: Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    print(Border)

    return df

#Step 3: Separate input and output variables.
def SeparateVariables(df):

    X = df.drop("LoanApproved", axis = 1)
    Y = df["LoanApproved"]

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    return X,Y

#Step 4: Split the dataset into training and testing data.
def SplitDataset(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    return  X_train,X_test,Y_train,Y_test

#Step 5: Train Dataset.
def TrainDataset(X_train,Y_train,X_test,Y_test):

    #Step 5.1: Train Logistic Regression.
    model_LR = LogisticRegression(max_iter=1000)
    model_LR = model_LR.fit(X_train,Y_train)
    pred_LR = model_LR.predict(X_test)
    


    #Step 5.2: Train Decision Tree.
    model_DT = DecisionTreeClassifier(random_state=42)

    #Step 5.3: Train KNN
    model_KNN = KNeighborsClassifier(n_neighbors=5)

    #Step 5.4: Create a Hard Voting Classifier.

    model_Hard = VotingClassifier(
        estimators=[
            ("logistic",model_LR),
            ("decision_tree",model_DT),
            ("knn",model_KNN)
        ],
            voting="hard"
    )

    #Step 5.5: Create a Soft Voting Classifier.

    model_Soft = VotingClassifier(
        estimators=[
            ("logistic",model_LR),
            ("decision_tree",model_DT),
            ("knn",model_KNN)
        ],
            voting="soft"
    )

    model_Hard = model_Hard.fit(X_train,Y_train)
    model_Soft = model_Soft.fit(X_train,Y_train)

    
    return model_Hard,model_Soft

#Step 6: Evaluate Hard model
def TestHardModel(model_Hard,X_test,Y_test):

    Y_pred = model_Hard.predict(X_test)

    print("Accuracy of hard model is: ",accuracy_score(Y_test,Y_pred))

#Step 7: Evaluate Soft model
def TestSoftModel(model_Soft,X_test,Y_test):

    Y_pred = model_Soft.predict(X_test)

    print("Accuracy of soft model is: ",accuracy_score(Y_test,Y_pred))


def main():

    df = LoadDataset("Customer_Loan_Approval.csv")

    X,Y = SeparateVariables(df) 
    X_train,X_test,Y_train,Y_test = SplitDataset(X,Y)

    model_Hard, model_Soft = TrainDataset(X_train,Y_train)

    TestHardModel(model_Hard,X_test,Y_test)

    TestSoftModel(model_Soft,X_test,Y_test)

if __name__ == "__main__":
    main()
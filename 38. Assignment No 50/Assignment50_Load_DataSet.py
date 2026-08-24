import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.model_selection import train_test_split


def LoadData(DataPath):

    df = pd.read_csv(DataPath)
    print("Dataset loaded sucessfully")
    print(df.head())
    return df

def PreProcessing(df):
    df["BareNuclei"] = df["BareNuclei"].replace("?", np.nan)
    df["BareNuclei"] = df["BareNuclei"].fillna(df["BareNuclei"].mode()[0]).astype(int)

    print("Preprocessing completed.")
    print(df.head())

    return df

def SplitData(df):

    X = df.drop(columns = ["CodeNumber","CancerType"])
    Y = df["CancerType"]

    print("Independent Variables X: \n",X.head())
    print("Dependent Variables Y: \n",Y.head())
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    return X_train,X_test,Y_train,Y_test

def TrainModel(X_train,Y_train):
    model = LogisticRegression(max_iter=1000)
    model = model.fit(X_train,Y_train)
    return model

def EvaluateModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is: ",accuracy*100)
    print(confusion_matrix(Y_test,Y_pred))

    Report = classification_report(Y_test,Y_pred,target_names=["Benign (2)", "Malignant (4)"])
    print("Classification report: ")
    print(Report)

def main():
    df = LoadData("breast-cancer-wisconsin.csv")
    df = PreProcessing(df)
    X_train,X_test,Y_train,Y_test = SplitData(df)
    model = TrainModel(X_train,Y_train)
    EvaluateModel(model,X_test,Y_test)

if __name__ == "__main__":
    main()

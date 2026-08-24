import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

def LoadDataset():
    cancer = load_breast_cancer()
    df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)

    df['target'] = cancer.target

    print("Dataset loaded sucessfully.")
    print("Shape of dataset: ",df.shape)
    print("First 5 data: ")
    print(df.head())
    return df

def SplitScale(df):

    X = df.drop(columns=["target"])
    Y = df["target"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.fit_transform(X_test)

    return X_train,X_test,Y_train,Y_test

def TrainModel(X_train,Y_train):

    model = LogisticRegression(max_iter=1000)
    model = model.fit(X_train,Y_train)

    return model

def EvaluateModel(model, X_test,Y_test):

    Y_pred = model.predict(X_test)
    accurcay = accuracy_score(Y_test,Y_pred)
    print("Accuracy is: ",accurcay)

    print("Confusion matrix: ")
    print(confusion_matrix(Y_test,Y_pred))

    Report = classification_report(Y_test,Y_pred,target_names=["Malignant (0)","Benign (1)"])
    print("Classification report: ")
    print(Report)


def main():
    df = LoadDataset()
   
    X_train,X_test,Y_train,Y_test = SplitScale(df)
    model = TrainModel(X_train,Y_train)
    EvaluateModel(model,X_test,Y_test)

if __name__ == "__main__":
    main()
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def AccuracySet(Y_test,Y_pred):
    return accuracy_score(Y_test,Y_pred)*100

def KNNWinePredictor(DataPath):

    Border = "*"*90

    df = pd.read_csv(DataPath)

    print(Border)
    print("File loaded and below are the 5 data:\n",df.head())


    #Clean dataset ----> to remove null values from the dataset
    df.dropna(inplace=True)

    print("Shape of data: ",df.shape)
    print("Total records: ",df.shape[0])
    print("Total columns: ",df.shape[1])
    print(Border)


    #Prepare and manipulate
    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    #Train

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print("Shape of X_train: ",X_train.shape)
    print("Shape of X_test: ",X_test.shape)
    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test: ",Y_test.shape)


    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test)

    print("Feature scaling completed.\n")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)
    model = model.fit(X_train_scaled,Y_train)
    Y_pred = model.predict(X_test_scaled)
    
    #Calculate accuracy
    #accuracy = accuracy_score(Y_test,Y_pred)*100
    #print("Accuracy is :",accuracy)

    print("Accuracy is: ",AccuracySet(Y_test,Y_pred))

def main():
    KNNWinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()
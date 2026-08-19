import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression
import numpy as np


def MarvellousAssignment46(filename):
    #Step 1: Get data
    df = pd.read_csv(filename)
    print(df.head())

    #Step 2: Clean, Prepare and Manipulate data
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    print(df.head())

    print(df.isnull().sum())

    #Step 3: Train and test the date -Separate Independent and Dependent Variables
    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Training data: ",X_train.shape)
    print("Testing data: ",X_test.shape)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)
    print("Expected answers is: ",Y_test[:3])
    print("Predicted answers is: ",Y_pred[:3])

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("MSE: ",MSE)
    print("RMSE: ",RMSE)
    print("R2: ",R2)

    #Display coefficient

    print("TV coefficient: ",model.coef_[0])
    print("Radio coefficient: ",model.coef_[1])
    print("Newspaper coefficient: ",model.coef_[2])
    
def main():
    MarvellousAssignment46("Advertising.csv")

if __name__ == "__main__":
    main()
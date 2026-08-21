from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import joblib 

def Marks(Datapath):

    data = {
    "Study Hours": [1, 2, 3, 4, 5],
    "Marks": [50, 55, 60, 70, 75]
    }

    df = pd.DataFrame(data)

    print("Data:    \n",df.head())

    X = df[["Study Hours"]]
    Y = df["Marks"]

    X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2,random_state=42)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)
    

    print("Study Hours X: ",model.coef_.item())
    print("Intercept of Y: ",model.intercept_.item())


    joblib.dump(model,"filename.pkl")
    print("Model preserved sucessfully")



def main():
    
    Marks("Marks.csv")
    

if __name__ == "__main__":
    main()
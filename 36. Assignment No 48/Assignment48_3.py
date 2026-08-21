import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def MarvellousLinearRegression():
    Data ={
    "Experience" : [1,2,3,4,5],
    "Salary" : [20000,25000,30000,35000,40000]
    }

    df = pd.DataFrame(Data)

    print(df.head())

    X = df[["Experience"]]
    Y = df["Salary"]
   
    model = LinearRegression()
    model = model.fit(X,Y)

    new_exp = pd.DataFrame({"Experience" : [6]})

    Y_pred = model.predict(new_exp)[0]


    print(f"Predicted salary for 6 years Experience: ₹{Y_pred:.0f}")

    plt.scatter(X,Y)
    plt.plot(X,model.predict(X))
    plt.title("Employee Salary")
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.grid()
    plt.show()



def main():
    MarvellousLinearRegression()

if __name__ == "__main__":
    main()
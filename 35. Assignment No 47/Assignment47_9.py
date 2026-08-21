import pandas as pd
from sklearn.linear_model import LinearRegression

def StudentDataset():

    Data = {
        "StudyHours" : [1,2,3,4,5],
        "SleepHours" : [7,6,7,6,8],
        "Marks" : [50,55,60,65,70]
    }

    df = pd.DataFrame(Data)

    X = df[["StudyHours","SleepHours"]]
    Y = df["Marks"]

    model = LinearRegression()
    model = model.fit(X,Y)

    print(f"Coefficient of StudyHours : {model.coef_[0]:.2f}")
    print(f"Coefficient of SleepHours : {model.coef_[1]:.2f}")
    print(f"Intercept of Y : {model.intercept_:.2f}")

def main():
    StudentDataset()

if __name__ == "__main__":
    main()
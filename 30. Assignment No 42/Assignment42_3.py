from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    Data = {
        "Study_hours" : [2,5,6,1],
        "Attendance" : [60,80,85,50],
        "Result" : ["Fail","Pass","Pass","Fail"]
    }

    df = pd.DataFrame(Data)
    X = df[["Study_hours","Attendance"]]
    Y = df["Result"]

    scalar = StandardScaler()
    X_scalar = scalar.fit_transform(X)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_scalar,Y)

    Study_hours = int(input("Enter the study hours: "))
    Attendance = int(input("Enter the attendance: "))

    user_data = pd.DataFrame([[Study_hours,Attendance]],columns=["Study_hours", "Attendance"])
    Y_scalar = scalar.transform(user_data)

    pred = model.predict(Y_scalar)[0]

    
    print("Predicted result is: ",pred)

if __name__ == "__main__":
    main()



                
import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix

import matplotlib.pyplot as plt


#Step 1. Load the dataset using Pandas.
def LoadDataset(Datapath):

    df = pd.read_csv(Datapath)
    print("Dataset loaded sucessfully.")

#Step 2. Display the shape, columns and first five records.
    
    print("Shape of the dataset is: ",df.shape)

    #Used pd.series to show the columns in lines.
    print("Columns from the dataset are: \n",pd.Series(df.columns))

    print("First five records are: \n",df.head())

#Step 3. Check for missing values.

    print("Missing values: ",df.isnull().sum())

#Step 4. Identify numerical and categorical features.    
    print(df.dtypes)
    print(df.select_dtypes(include="number").columns)
    print(df.select_dtypes(exclude="number").columns)

#Step 5. Convert categorical features such as OverTime into numerical representation.
    #Used astype and converted the features to numbers for Yes=0 & No=1
    df["OverTime"] = (df["OverTime"] == "Yes").astype(int)
   
#Step 6. Convert the target Attrition into 0 and 1.
    #Used labelencoder to convert Target string values into numbers
    le = LabelEncoder()
    df["Attrition"] = le.fit_transform(df["Attrition"])

    return df

#Step 7. Separate independent and dependent variables.
def SplitDataset(df):

    X = df.drop("Attrition", axis=1)
    Y = df["Attrition"]

    print("Shape of Independent Variables: ",X.shape)
    print("Shape of Dependent Variables: ",Y.shape)

#Step 8. Divide the dataset into training and testing data.

    X_train,X_test,Y_train,Y_test = train_test_split(X,
                                                     Y,
                                                     test_size=0.20,
                                                     random_state=42,
                                                     stratify=Y)

#Step 9. Apply appropriate feature scaling.

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    return X_train,X_test,Y_train,Y_test,scalar

#Step 10. Design an MLP with at least two hidden layers.
def TrainModel(X_train,Y_train):

    model = MLPClassifier(hidden_layer_sizes=(8,4),
                          activation="relu",
                          solver="adam",
                          max_iter=1000,
                          random_state=42)

#Step 11. Train the network.

    model = model.fit(X_train,Y_train)

#Step 12. Display the number of iterations required for training.

    print("Number of iteration required for training: ",model.n_iter_)    

    return model

def EvaluateModel(model,X_train,X_test,Y_train,Y_test):
#Step 13. Calculate training accuracy.
    Y_train_pred = model.predict(X_train)
    accuracy_train = accuracy_score(Y_train,Y_train_pred)*100
    print(f"Training accuracy is: {accuracy_train:.2f}%")

#Step 14. Calculate testing accuracy.
    
    Y_pred = model.predict(X_test)
    accuracy_test = accuracy_score(Y_test,Y_pred)*100
    print(f"Testing accuracy is: {accuracy_test:.2f}%")

#Step 15. Generate a confusion matrix.

    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion Matrix: \n",cm)

#Step 16. Plot the loss curve.
    plt.figure(figsize=(8, 5))
    plt.plot(model.loss_curve_, color='blue', linewidth=2)
    plt.title('Loss Curve during Training')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.grid()
    plt.show()

    return accuracy_train,accuracy_test
def PredictAttrition(scalar,model):

    new_employee = pd.DataFrame([[24,52421,6,5,43,1,1,"Yes",4,4],
                                 [23,54221,2,6,34,2,2,"Yes",6,4],
                                 [22,52422,6,2,32,3,3,"Yes",8,1],
                                 [21,52423,3,7,31,4,1,"Yes",2,2],
                                 [20,52424,4,8,30,4,2,"Yes",1,0]],
                                 columns=['Age', 
                                          'MonthlyIncome', 
                                          'YearsAtCompany', 
                                          'TotalWorkingYears',
       'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance',"OverTime",
       'NumCompaniesWorked', 'TrainingTimesLastYear'])

    new_employee['OverTime'] = (new_employee['OverTime'] == "Yes").astype(int)

    new_employee_scaled = scalar.transform(new_employee)

    new_prediction = model.predict(new_employee_scaled)

    new_probability = model.predict_proba(new_employee_scaled)

    print("New employee data: ")
    print(new_employee)

    print("Prediction probability: \n",new_probability)

    count = 1

    for pred in new_prediction:
        
        if pred == 1:
            
            print("Employee", count, "-> Will Leave")
        else:
            print("Employee", count, "-> Will Stay")

        count = count + 1


def CheckFit(accuracy_train,accuracy_test):
    print("\n")
    gap = accuracy_train - accuracy_test

    if gap > 10.0:
        print("Model is: Overfitting")

    elif accuracy_train < 70.0 and accuracy_test < 70.0:
        print("Model is: Underfitting")

    else:
        print("Model is: Best fit")


def main():
    df = LoadDataset("Employee_Attrition.csv")
    X_train,X_test,Y_train,Y_test,scalar = SplitDataset(df)
    model = TrainModel(X_train,Y_train)
    accuracy_train,accuracy_test = EvaluateModel(model,X_train,X_test,Y_train,Y_test) 
    PredictAttrition(scalar,model)
    CheckFit(accuracy_train,accuracy_test)

if __name__ == "__main__":
    main()

import pandas as pd

from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

import matplotlib.pyplot as plt

#Load the dataset
def LoadDataset(Datapath):

    df = pd.read_csv(Datapath)

    print("Shape of dataset: ",df.shape)
    print("First Five Data from a dataset: \n",df.head())

    print(df.columns)

    print(df.isnull().sum())

    df["PreviousDefault"] = (df["PreviousDefault"] == "Yes").astype(int)

    le = LabelEncoder()
    df["HomeOwnership"] = le.fit_transform(df["HomeOwnership"])

    print(df.head())

    class_counts = df["Default"].value_counts()
    class_pct = df["Default"].value_counts(normalize=True) * 100
    print(class_counts)
    print(class_pct.round(2))

    imbalance_ratio = class_counts.max() / class_counts.min()
    print(f"\nImbalance ratio (majority:minority) = {imbalance_ratio:.2f} : 1")
    if imbalance_ratio < 1.5:
        print("=> Classes are reasonably balanced (mild skew is fine).")
    else:
        print("=> Classes are noticeably imbalanced; consider stratified splitting,")
      

    return df,le

def SplitDataset(df):

    X = df.drop("Default", axis = 1)
    Y = df["Default"]

    print("Independent variables: ",X.shape)
    print("Dependent variables: ",Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42,
        stratify=Y
    )

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    return X_train,X_test,Y_train,Y_test,scalar

def ModelCreation(X_train,Y_train):

    model = MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )


    model = model.fit(X_train,Y_train)

    return model

def EvaluateModel(model,X_train,X_test,Y_train,Y_test):

    Y_pred = model.predict(X_test)

    accuracy_test = accuracy_score(Y_test,Y_pred)*100
    print(f"Accuracy of testing is: {accuracy_test:.2f}%")

    Y_train_pred = model.predict(X_train)
    accuracy_training = accuracy_score(Y_train,Y_train_pred)*100
    print(f"Accuracy of training is:{accuracy_training:.2f}%")


    gap = accuracy_training - accuracy_test
   
    if gap > 10.0:
        print("Model is: Overfitting")
   
    elif accuracy_training < 70.0 and accuracy_test < 70.0:
        print("Model is: Underfitting")
   
    else:
           print("Model is: Best fit")

    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion matrix is: \n",cm)

    print("Classification report: ")
    print(classification_report(Y_test,Y_pred))

    

    plt.figure(figsize=(8,5))
    plt.plot(model.loss_curve_, color = "blue", linewidth = 2)
    plt.title("Training losss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid()
    plt.show()

def PredictLoanApplication(scalar,model,le):

    new_app = pd.DataFrame([[37, 45000, 15000, 720, 5, 1, 1200, 36, "No", "Rent"],
        [24, 22000, 25000, 580, 1, 3, 1100, 60, "Yes", "Rent"]],
                           columns=['Age','Income', 'LoanAmount', 
                                    'CreditScore', 'EmploymentYears',
       'ExistingLoans', 'MonthlyDebt', 'LoanTerm', 'PreviousDefault',
       'HomeOwnership'])

    new_app["PreviousDefault"] = (new_app["PreviousDefault"]=="Yes").astype(int)
    new_app["HomeOwnership"] = le.transform(new_app["HomeOwnership"])

    new_app_scaled = scalar.transform(new_app)

    new_pred = model.predict(new_app_scaled)

    new_prob = model.predict_proba(new_app_scaled)

    print("New loan application data: ")
    print(new_app)

    print("Prediction probability: \n",new_prob)

    count = 1
    for pred in new_pred:
        if pred == 1:
            print("Applicant no.: ",count,"-> is defaultor")
        else:
            print("Applicant no.: ",count,"-> is Not defaultor")
        count += 1

def main():

    df,le = LoadDataset("Loan_Default.csv")
    X_train,X_test,Y_train,Y_test,scalar = SplitDataset(df)
    model = ModelCreation(X_train,Y_train)
    EvaluateModel(model,X_train,X_test,Y_train,Y_test)
    PredictLoanApplication(scalar,model,le)

if __name__ == "__main__":
    main()
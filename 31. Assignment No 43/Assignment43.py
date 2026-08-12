from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def CheckAccuracy(Y_test,Y_pred):
    return accuracy_score(Y_test,Y_pred)*100


def KNNClassifierStudy(DataPath):

    #####################################
    #Step 1: Load data
    #####################################
    print("Step 1: Load data\n")
    df = pd.read_csv(DataPath)
    print(df.head())

    #####################################
    #Step 2: Clean, Prepare and Manipulate data 
    #####################################
    print("Step 2: Clean, Prepare and Manipulate data\n")
    df.dropna(inplace=True)

    #print("Separate Independent and Dependent\n")
    encoder_wether = LabelEncoder()
    encoder_tempratue = LabelEncoder()
    encoder_play = LabelEncoder()

    df["Wether"] = encoder_wether.fit_transform(df["Wether"])
    df["Temperature"] = encoder_tempratue.fit_transform(df["Temperature"])
    df["Play"] = encoder_play.fit_transform(df["Play"])

    X = df[["Wether","Temperature"]]
    Y = df["Play"]

    print("Encoded data sammple: \n",df.head())

   
    #####################################
    #Step 3: Train data 
    #####################################    

    model = KNeighborsClassifier(n_neighbors=3)
    model = model.fit(X,Y)

    #####################################
    #Step 4:  Test Data
    #####################################    
    print("\nStep 4: Predict for new test input (Weather='Overcast', Temp='Cool')")

    # Custom Input
    test_w = encoder_wether.fit_transform(["Overcast"])[0]
    test_t = encoder_tempratue.fit_transform(["Cool"])[0]

    input_data = pd.DataFrame([[test_w, test_t]], columns=["Wether","Temperature"])

    prediction = model.predict(input_data)
    result = encoder_play.inverse_transform(prediction)[0]
    print(f"Prediction Result: {result}\n")


    #####################################
    #Step 5: Calculate Accuracy 
    ##################################### 


    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    model = KNeighborsClassifier(n_neighbors=3)
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy = CheckAccuracy(Y_test,Y_pred)
    print(accuracy)

    
def main():

    KNNClassifierStudy("MarvellousInfosystems_PlayPredictor.csv")
if __name__ == "__main__":
    main()
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    "Gender": ["Male", "Male", "Female"],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df_encoded = pd.get_dummies(df,columns=["Gender"],dtype=int)

    print(df_encoded)

if __name__ == "__main__":
    main()
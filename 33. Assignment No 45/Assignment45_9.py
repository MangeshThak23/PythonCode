import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    "Gender": ["Male", "Male", "Female"],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    print("Before rename: \n",df)

    df = df.rename(columns={"Math":"Mathematics"})

    print("After rename: \n",df)
    
if __name__ == "__main__":
    main()
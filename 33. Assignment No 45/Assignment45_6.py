import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    "Gender": ["Male", "Male", "Female"],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    df["Total"] = df["Math"]+df["Science"]+df["English"]

    df["Status"] = np.where(df["Total"]>=250,"Pass","Fail")
    print(df)
    
    Pass_count = (df["Status"]=="Pass").sum()
    print("Total Number of students passed:",Pass_count)

if __name__ == "__main__":
    main()
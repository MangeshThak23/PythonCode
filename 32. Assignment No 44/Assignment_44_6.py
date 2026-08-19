import pandas as pd
import numpy as np

def main():

    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df["Total"] = df["Math"]+df["Science"]+df["English"]

    dfsorted = df.sort_values(by="Total",ascending=False)

    print(dfsorted)
    
if __name__ == "__main__":
    main()
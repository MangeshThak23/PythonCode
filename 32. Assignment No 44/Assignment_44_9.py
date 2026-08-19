import pandas as pd
import numpy as np
def main():
    data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
    }

    df = pd.DataFrame(data2)

    fillna = df.fillna(df.mean(numeric_only=True))
    
    print(fillna)

if __name__ == "__main__":
    main()
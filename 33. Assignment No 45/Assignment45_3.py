import pandas as pd

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    "Gender": ["Male", "Male", "Female"],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    Avg = df.groupby("Gender")[["Math","Science","English"]].mean()

    print(Avg)

if __name__ == "__main__":
    main()
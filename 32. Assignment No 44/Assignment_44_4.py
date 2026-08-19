import pandas as pd

def main():

    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    High_Score = df[df["Science"]>85]
    print(High_Score[["Name","Science"]])

    
if __name__ == "__main__":
    main()
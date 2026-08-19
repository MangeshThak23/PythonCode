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

    Sagar_row = df[df["Name"]=="Sagar"].iloc[0]
    Subjects = ["Math","Science","English"]
    Marks = [Sagar_row[sub] for sub in Subjects]

    plt.figure(figsize = (6,6))
    plt.pie(Marks,labels = Subjects,autopct="%1.1f%%", startangle=90)
    plt.title("Sagar's details")
    plt.show()


if __name__ == "__main__":
    main()
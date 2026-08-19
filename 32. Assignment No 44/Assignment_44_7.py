import pandas as pd
import matplotlib.pyplot as plt

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

    plt.figure(figsize=(8,5))
    plt.bar(df["Name"],df["Total"],color = "r",edgecolor = "g")
    plt.title("Student Details")
    plt.xlabel("Student Name", fontsize =12)
    plt.ylabel("Total Marks", fontsize = 12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.show()


if __name__ == "__main__":
    main()
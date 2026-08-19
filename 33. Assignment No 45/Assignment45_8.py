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

    plt.figure(figsize = (6,4))
    plt.hist(df["Math"],bins = 5, color="g", edgecolor = "r")
    plt.title("Student details")
    plt.xlabel("Marks")
    plt.ylabel("Number of students")
    plt.grid(axis="y")
    plt.show()
    
if __name__ == "__main__":
    main()
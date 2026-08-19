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

    Subjects = ["Math","Science","English"]
    amit_marks = df[df['Name'] == 'Amit'][Subjects].values[0]
      
    plt.plot(Subjects,amit_marks,marker="o")
    plt.title("Student Details")
    plt.xlabel("Subjets")
    plt.ylabel("Marks")
    plt.grid(True)   
    plt.show()


if __name__ == "__main__":
    main()
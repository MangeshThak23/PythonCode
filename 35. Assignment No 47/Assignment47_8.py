import joblib
import pandas as pd

def LoadModel(filename,StudyHours):
    
    model = joblib.load(filename)

    Student = pd.DataFrame({"Study Hours":[StudyHours]})

    print("Model loaded sucessfully.")
      
    Y_pred = model.predict(Student)[0]
    print(f"Marks predicted for student: {Y_pred:.2f}")
    
def main():

    LoadModel("filename.pkl",6)

if __name__ == "__main__":
    main()

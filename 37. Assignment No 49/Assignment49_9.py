import numpy as np
from sklearn.metrics import classification_report

def main():

    actual = np.array([1,1,1,1,0,0,0,0])
    predicted = np.array([1,1,0,1,0,1,0,0])

    report = classification_report(actual,predicted)
    print("The classification report is:")
    print(report)

    
if __name__ == "__main__":
    main()
    


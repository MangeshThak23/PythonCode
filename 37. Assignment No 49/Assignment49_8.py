import numpy as np
from sklearn.metrics import confusion_matrix


def main():
    actual = np.array([1,1,1,1,0,0,0,0])
    predicted = np.array([1,1,0,1,0,1,0,0])

    TN,FP,FN,TP = confusion_matrix(actual,predicted).ravel()

    print("True Positive  (TP):", TP)
    print("True Negative  (TN):", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)
    
if __name__ == "__main__":
    main()
    


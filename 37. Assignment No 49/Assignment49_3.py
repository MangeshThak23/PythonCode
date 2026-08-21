import numpy as np
from sklearn.preprocessing import StandardScaler


def main():
    Data = [[25,20000],[30,40000],[35,80000]]

   
    scalar = StandardScaler()
    scalar = scalar.fit_transform(Data)

    print("The data is: \n",np.array(Data))
    print("The scaled data is: \n",scalar)

if __name__ == "__main__":
    main()
    


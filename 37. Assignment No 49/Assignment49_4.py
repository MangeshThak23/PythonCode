import numpy as np
from sklearn.preprocessing import StandardScaler


def main():
    Data = np.array([[25,20000],[30,40000],[35,80000]])

    print("The data is: \n",Data)

    point1 = Data[0]
    point2 = Data[1]

    prior_dist = np.linalg.norm(point1 - point2)
    print(f"Prior distance between {point1} and {point2} is: {prior_dist}\n")

  
    scalar = StandardScaler()
    scalar = scalar.fit_transform(Data)

    print(f"The scaled data is: \n{scalar}")

    scaled_point1 = scalar[0]
    scaled_point2 = scalar[1]

    after_dist = np.linalg.norm(scaled_point1 - scaled_point2)

    print(f"After scaled the Euclidean distance between {scaled_point1} and {scaled_point2} is: {after_dist}")

    

if __name__ == "__main__":
    main()
    


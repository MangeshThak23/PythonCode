import numpy as np

def MarvellousSimpleLinearRegression():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Value of independent variable X: ",X)
    print("Value of dependent variable Y: ",Y)

    #Mean
    Sum_X = 0
    Sum_Y = 0

    for i in range(len(X)):
        Sum_X = Sum_X + X[i]
        Sum_Y = Sum_Y + Y[i]

    n = len(X)
    Mean_X = Sum_X/n
    Mean_Y = Sum_Y/n

    print(f"Mean_X is: {Mean_X:.2f}")
    print(f"Mean_Y is: {Mean_Y:.2f}")

    #slope

    numerator = 0
    denomenator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-Mean_X)*(Y[i]-Mean_Y))
        denomenator = denomenator + (X[i]-Mean_X)**2

    m = numerator / denomenator

    print(f"Slope(m) is: {m:.2f}")

    #Intercept

    C = Mean_Y - m * Mean_X

    print("Y intercept is: ",C)

    X_pred = 6
    Y_pred = (m*X_pred) + C 
    print(f"Predicted Y is for X is: {Y_pred:.2f}") 

    sum_res = 0
    sum_square = 0

    for i in range(n):
        Y_Pred1 = (m * X[i])+C
        sum_res += (Y[i] - Y_Pred1)**2
        sum_square += (Y[i] - Mean_Y)**2

    MSE = sum_res / n
    R2 = 1 - (sum_res/sum_square)

    print(f"MSE is: {MSE:.2f}")
    print(f"R2 is: {R2:.2f}")
        
   
def main():
    MarvellousSimpleLinearRegression()

if __name__ == "__main__":
    main()
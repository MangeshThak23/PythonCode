import math

def Mean_Squared_Error(actual,pred):

    n = len(actual)
    squared_errors = [(a - p)**2 for a,p in zip(actual,pred)]
    return sum(squared_errors)/n

def Calculate_BCE(actual, pred):

    n = len(actual)
    epsilon = 1e-15
    bce_sum = 0

    for a,p in zip(actual,pred):
        p = max(min(p, 1 - epsilon), epsilon)
        bce_sum += -(a * math.log(p) + (1 - a) * math.log(1 - p))
    return bce_sum / n

def main():

    Y_actual_reg = [3.0, 4.0, 2.0, 4.0, 5.0]
    Y_pred_reg = [2.8, 3.2, 3.6, 4.0, 4.4]

    mse_loss = Mean_Squared_Error(Y_actual_reg,Y_pred_reg) 

    print("MSE: used for regression to calculate the loss ",mse_loss)

    Y_actual_class = [1, 0, 0, 1]
    Y_pred_class = [0.6, 0.1, 0.5, 0.6]

    bce_loss = Calculate_BCE(Y_actual_class, Y_pred_class)

    print("BCE: used for classification to calculate the loss ",bce_loss)

if __name__ == "__main__":
    main()



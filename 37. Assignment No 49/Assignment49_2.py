import numpy as np

def main():
    Data = [6, 7, 8, 9, 10, 11, 12]

    variance = np.var(Data)
    standard_deviation = np.std(Data)


    print(f"Variance of dataset is: {variance}")
    print(f"standard deviation of dataset is: {standard_deviation}")

if __name__ == "__main__":
    main()
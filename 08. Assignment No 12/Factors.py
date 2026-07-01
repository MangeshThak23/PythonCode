# 2. Write a program which accepts one number and prints its factors.
    
def main():
    No1 = int(input("Enter a number:"))
    for i in range(1,No1+1):
        if No1 % i == 0:
            print("Factors:",i)
        
    
if __name__ == "__main__":
    main()

# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

DivisibleFilter = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Mylist = []
    Num = int(input("Enter how much numbers do you want to enter in the list: "))
     
    for i in range(Num):
          Numbers = int(input("Enter the numbers:   "))
          Mylist.append(Numbers)
    print("The entered list is: ",Mylist)

    FData = list(filter(DivisibleFilter, Mylist))
    print("The numbers which are divisible by 3 and 5:  ",FData)

if __name__ == "__main__":
     main()


#Output: 
# Enter how much numbers do you want to enter in the list: 3
#Enter the numbers:   15
#Enter the numbers:   30
#Enter the numbers:   45
#The entered list is:  [15, 30, 45]
#The numbers which are divisible by 3 and 5:   [15, 30, 45]

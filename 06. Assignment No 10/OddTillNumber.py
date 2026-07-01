#5.Write a program which accepts one number and prints all odd numbers till that number.

def Odd(No):
   if No < 1:
      print("Enter number which is more than 1")
      return
   
   for i in range(1, No+1):
      if i%2!=0:
         print(i)
        
if __name__ == "__main__":
   Num=int(input("Enter a number:"))
   Odd(Num)
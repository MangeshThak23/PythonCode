"""9. Write a program which display first 10 even numbers on screen."""

def Even():
    No = 20
    for i in range(1,No+1): 
        if i%2==0: 
            print(i)

def main():
    Even()

if __name__ == "__main__":
    main()
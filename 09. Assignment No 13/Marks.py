#5. Write a program which accepts marks and displays grade.
# Condition Example:
# ≥ 75 → Distinction
# ≥ 60 → First Class
# ≥ 50 → Second Class
# < 50 → Fail


def main():
    Marks = int(input("Enter marks:"))
    if Marks>=75:
        print("Distinction")
    elif Marks>=60:
        print("First Class")
    elif Marks>=50:
        print("Second Class")
    else:
        print("Fail")

if __name__ == "__main__":
    main()
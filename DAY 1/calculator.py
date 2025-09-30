import os
import time

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("..............CALCULATOR..............")
    print("Select your choice.......\n enter")
    print("0 for Exit")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")

    try:
        n = int(input("Enter your choice: "))

        match n:
            case 0:
                print("Exiting calculator. Bye!")
                exit(0)

            case 1 | 2 | 3 | 4:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))

                match n:
                    case 1:
                        print(f"Result of Addition: {add(a, b)}")
                    case 2:
                        print(f"Result of Subtraction: {sub(a, b)}")
                    case 3:
                        print(f"Result of Multiplication: {mul(a, b)}")
                    case 4:
                        if b == 0:
                            print("Error: Division by zero not allowed")
                        else:
                            print(f"Result of Division: {div(a, b)}")

            case _:
                print("Please enter a valid choice")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    time.sleep(3)

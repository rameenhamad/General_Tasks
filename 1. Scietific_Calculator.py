import math as m

# get two numbers
def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

# get one number
def get_number():
    a = float(input("Enter a number: "))
    return a

print("Welcome to Calculator")
print("Enter 0 to exit")
print("""Choose an operation: 1. Addition
2. Subtraction
3. Multiplication
4. Exponent
5. Division
6. Remainder
7. Square Root
8. Maximum
9. Minimum
10. Natural Log
11. Common Log
12. Log base 10
13. Value of Pi
14. Factorial
""")

while True:
    try:
        choice = int(input("Enter your choice (0 to exit): "))

        match choice:
            case 0:
                print("Exiting calculator...")
                break

            case 1:
                a, b = get_numbers()
                print("Addition:", a + b)
            case 2:
                a, b = get_numbers()
                print("Subtraction:", a - b)
            case 3:
                a, b = get_numbers()
                print("Multiplication:", a * b)
            case 4:
                a, b = get_numbers()
                print("Exponent:", a ** b)
            case 5:
                a, b = get_numbers()
                if b == 0:
                    print("Error: Division by zero")
                else:
                    print("Division:", a / b)
            case 6:
                a, b = get_numbers()
                if b == 0:
                    print("Error: Division by zero")
                else:
                    print("Remainder:", a % b)
            case 7:
                a = get_number()
                print("Square Root:", m.sqrt(a))
            case 8:
                a, b = get_numbers()
                print("Maximum:", max(a, b))
            case 9:
                a, b = get_numbers()
                print("Minimum:", min(a, b))
            case 10:
                a = get_number()
                print("Natural Log:", m.log(a))
            case 11:
                a = get_number()
                print("Common Log (base e):", m.log(a))
            case 12:
                a = get_number()
                print("Log base 10:", m.log10(a))
            case 13:
                print("Value of Pi:", m.pi)
            case 14:
                a = get_number()
                print("Factorial:", m.factorial(int(a)))
            case _:
                print("Invalid choice! Please enter 0 to 14.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print("Error:", e)

print("All calculations done!")

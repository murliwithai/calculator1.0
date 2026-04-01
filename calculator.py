print("=== YOUR CALCULATOR IS LIVE ===")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter the operation: ")

if c == "+":
    print("Sum:", a + b)

elif c == "-":
    print("Difference:", a - b)

elif c == "*":
    print("Product:", a * b)

elif c == "/":
    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Error: Division by zero not allowed")

elif c == "%":
    if b != 0:
        print("Modulus:", a % b)
    else:
        print("Error: Modulus by zero not allowed")

elif c == "**":
    print("Power:", a ** b)

# AREA CALCULATIONS
elif c == "rectangle":
    print("Area of Rectangle:", a * b)

elif c == "triangle":
    print("Area of Triangle:", 0.5 * a * b)

elif c == "circle":
    print("Area of Circle:", 3.14 * a * a)

elif c == "square":
    print("Area of Square:", a * a)

# PERCENTAGE
elif c == "percentage":
    if b != 0:
        print("Percentage:", (a / b) * 100, "%")
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation")
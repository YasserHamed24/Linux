import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x):
    return math.log10(x)

print('''
Select mode: 
1) SCIENTIFIC Mode
2) PROGAMMER Mode
''')

mode = input("mode: ")

if mode == '1':
    print('''
    Select operation:
    1) Add
    2) Subtract
    3) Multiply
    4) Divide
    5) Power
    6) Square Root
    7) Logarithm
    ''')

    while True:
        choice = input("choice: ")

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            if choice == '1':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(add(num1, num2))

            elif choice == '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(subtract(num1, num2))

            elif choice == '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(multiply(num1, num2))

            elif choice == '4':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(divide(num1, num2))

            elif choice == '5':
                num1 = float(input("Enter base: "))
                num2 = float(input("Enter exponent: "))
                print(power(num1, num2))

            elif choice == '6':
                num = float(input("Enter number: "))
                print(square_root(num))

            elif choice == '7':
                num = float(input("Enter number: "))
                print(logarithm(num))
            break
        else:
            print("WRONG ENTRY!!")

elif mode == '2':
    print("1. Decimal to Binary")
    print("2. Decimal to octal")
    print("3. Decimal to hex")

    while True:
        choice = input("choice: ")

        if choice in ('1', '2','3'):
            if choice == '1':
                decimal = int(input("Enter the number: "))
                print("binary is", bin(decimal))

            elif choice == '2':
                decimal = int(input("Enter the number: "))
                print("octal is", oct(decimal))
            elif choice == '3':
                decimal = int(input("Enter the number: "))
                print("hex is",hex(decimal))
            break
        else:
            print("WRONG ENTRY!!")

else:
    print("WRONG ENTRY!!")

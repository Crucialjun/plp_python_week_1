num1 = input("Enter first number: \n")
num2 = input("Enter second number: \n")

sign = input("Enter the sign: +, -, *, / : \n")

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)
else:
    print("Invalid sign")
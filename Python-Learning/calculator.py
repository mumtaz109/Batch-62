# Option 1: User Input

num1 = float(input("first number: "))
num2 = float(input("second number: "))
operator = input("what do you want to do (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

print("Output:", result)


# Option 2: Using Variables

def calculator_with_variables():

    a = 10
    b = 5

    add = a + b
    sub = a - b
    multi = a * b

    if b == 0:
        div = "Division by zero is not allowed."
    else:
        div = a / b

    return {
        "Addition": add,
        "Subtraction": sub,
        "Multiplication": multi,
        "Division": div
    }
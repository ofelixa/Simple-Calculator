operator = input("Would you like to add (+), subtract (-), multiply (*) or divide (/)")
num1 = float(input("Enter the first number: "))
num2 = float(input('Enter the second number: '))
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
if operator in ["add", "Add", "+", "addition", "Addition"]:
    result1
    print(f"= {result1}")
elif operator in ["subtract", "Subtract", "minus", "Minus", "-"]:
    result2
    print(f"= {result2}")
elif operator in ["multiply", 'Multiply', "*", "multiplication", "Multiplication", "times", "Times","x","X"]:
    result3
    print(f"= {result3}")
elif operator in ["divide","Divide","Division", "division","/",]:
    result4
    print(f"= {result4}")
else:
    print(f"{operator} is an invalid operator")
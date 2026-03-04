num1_input = input("Enter the first number: ")

num2_input = input("Enter the second number: ")

operation = input("Enter an operation (+, -, *, /): ").strip()

    num1 = float(num1_input)
    num2 = float(num2_input)


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    result = num1 / num2
else:
    print("Invalid operation. Please choose one of +, -, *, /.")
    exit(1)
    #We can also make use of a dowhile loop to keep asking the user 
    #for a valid operation until they provide one. For simplicity, we will just exit the program if the operation is invalid.

# Display the result to the user using an f-string for better readability
print(f"{num1} {operation} {num2} = {result}")
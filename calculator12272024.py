def calculator(operation, num1, num2):
  try:
    num1 = float(num1)
    num2 = float(num2)

    if operation == 'add':
      return num1 + num2
    elif operation == 'subtract':
      return num1 - num2
    elif operation == 'multiply':
      return num1 * num2
    elif operation == 'divide':
      if num2 == 0:
        return "Error: Division by zero is not allowed."
      return num1 / num2
    else:
      return "Error:Invalid operation."
  except ValueError:
    return "Error: Invalid input. Please enter numeric values."

operation = input ("Enter operation (add, subtract, multiply, divide):").lower()
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = calculator(operation, num1, num2)
print("Result:", result)
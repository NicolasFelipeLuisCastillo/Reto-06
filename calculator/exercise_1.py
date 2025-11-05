def calculator(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Both inputs must be numeric values.")

    if operation not in ("+", "-", "*", "/"):
        raise ValueError(f"Invalid operation '{operation}'. Use one of: +, -, *, /")

    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return num1 / num2
    except Exception:
        raise RuntimeError(f"Unexpected error in calculation: {Exception}")

try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (+, -, *, /): ")

    result = calculator(num1, num2, operation)
    print(f"Result: {result}")

except ValueError:
    print(ValueError)
except ZeroDivisionError:
    print(ZeroDivisionError)
except RuntimeError:
    print(RuntimeError)
except Exception:
    print(f"Unexpected error: {Exception}")

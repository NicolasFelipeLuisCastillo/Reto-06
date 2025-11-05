numbers: list = [2, 10, 29, 25, 2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 19]

def sum_last_two_numbers(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list of numbers.")

        if not numbers:
            raise ValueError("The list cannot be empty.")
        
        if len(numbers) < 2:
            raise ValueError("The list must contain at least two numbers to sum the last two.")

        for n in numbers:
            if not isinstance(n, (int, float)):
                raise ValueError(f"Invalid element '{n}' — all elements must be numbers.")

        numbers.sort()
        length: int = len(numbers)
        result: float = numbers[length - 1] + numbers[length - 2]

        print(f"The result is: {result}")

    except TypeError:
        print(f"TypeError: {TypeError}")
    except ValueError:
        print(f"ValueError: {ValueError}")
    except Exception:
        print(f"Unexpected error: {Exception}")


sum_last_two_numbers(numbers)

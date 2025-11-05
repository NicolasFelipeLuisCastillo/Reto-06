numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def is_prime(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("The input must be a list of integers.")

        if not numbers:
            raise ValueError("The list cannot be empty.")

        for n in numbers:
            if not isinstance(n, int):
                raise ValueError(f"All elements must be integers. Invalid element: {n}")

        primes: list = []

        if 1 in numbers:
            numbers.remove(1)

        if not numbers:
            raise ValueError("List contains only '1', which is not a prime number.")

        for number in numbers:
            if number < 2:
                continue
            for dividers in range(2, number):
                if number % dividers == 0:
                    break
            else:
                primes.append(number)

        print(f"The prime numbers are: {primes}")

    except TypeError:
        print(f"TypeError: {TypeError}")
    except ValueError:
        print(f"ValueError: {ValueError}")
    except Exception:
        print(f"Unexpected error: {Exception}")

is_prime(numbers)

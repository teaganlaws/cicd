"""
    Even/ odd checking code
    By: Teagan Laws, assisted by ChatGPT
    Date: 1 May 2023
"""


def is_odd(num: int) -> bool:
    """Return True if num is odd, False otherwise."""
    return num % 2 == 1


def is_odd_str(num: str) -> str:
    """Return a string indicating whether num is odd or even."""
    if num.isnumeric():
        return f"{num} is {'odd' if is_odd(int(num)) else 'even'}."
    else:
        return "Please enter a number."


def is_prime(num: int) -> bool:
    """Return True if num is prime, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_prime_str(num: str) -> str:
    """Return a string indicating whether num is odd or even."""
    if num.isnumeric():
        return f"{num} is {'prime' if is_prime(int(num)) else 'not prime'}."
    else:
        print(num, "is not a prime number")


def is_divisible_by_23(n):
    if n % 23 == 0:
        return True
    return False


num = int(input("Enter a number: "))

if is_divisible_by_23(num):
    print(num, "is divisible by 23")
else:
    print(num, "is not divisible by 23")


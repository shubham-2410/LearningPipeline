def factorial_iterative(n):
    if n < 0:
        return "Invalid input! Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print(f"The factorial of {number} is {factorial_iterative(number)}")

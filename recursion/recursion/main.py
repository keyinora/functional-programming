def factorial_r(x):
    # Base case: if x is 0, return 1 (since 0! = 1)
    if x == 0:
        return 1
    # Recursive case: x * factorial of (x - 1)
    return x * factorial_r(x - 1)

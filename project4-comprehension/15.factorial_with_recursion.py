def calculate_factorial(n):
    if n != 1:
        return n * calculate_factorial(n - 1)
    return n

number = int(input())
result = calculate_factorial(number)
print(result)

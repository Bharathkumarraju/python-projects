def calculate_sum(n):
    if n!= 0:
        n = n + calculate_sum(n - 1)
    return  n

result = calculate_sum(5)
print(result)
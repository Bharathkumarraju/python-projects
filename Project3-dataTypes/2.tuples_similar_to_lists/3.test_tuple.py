numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1: 4])    # (20, 30, 40)

numbers = (10, 20, 30, 40, 50, 60)

# items from index 0 to 3
print(numbers[0: 4])    # (10, 20, 30, 40)

# items from index 3 to 4
print(numbers[3: 5])   # (40, 50)

# items from index 3 to second-last
# remember, last index is exclusive
print(numbers[3: -1])   # (40, 50)


numbers = (10, 20, 30, 40, 50, 60)

# items from first index to 3
print(numbers[: 4])    # (10, 20, 30, 40)

# items from index 3 to last
print(numbers[3: ])   # (40, 50, 60)

# omitting both start and end index
# items from first to last
print(numbers[:])   # (10, 20, 30, 40, 50, 60)


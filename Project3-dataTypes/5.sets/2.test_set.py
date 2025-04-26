# create an empty set
numbers = set()

# get integer input
number = int(input())

# add number to the numbers set
numbers.add(number)

# print the numbers set
print(numbers)

numbers1 = {1, 10, 3.14, 25.1, 56.15, 22.12}
print(numbers1)
numbers1.discard(22.12)
print(numbers1)
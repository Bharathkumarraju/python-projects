numbers = [1, 2, 3, 4, 5, 6]

square_numbers = {}

for i in numbers:
    square_numbers[i] = i ** 2

print(square_numbers)


s_numbers= { i:i**2 for i in numbers }
print('the dictionary is')
print(s_numbers)

# get integer input
n = int(input("Enter the number: "))

# create the dictionary using comprehension
numbers = { i:i*10  for i in range(1, n+1) if i >= 3}

print(numbers)
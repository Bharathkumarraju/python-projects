numbers = [10, 45, 61, -6, 199, 1999, 2025, 2026]

largest = numbers[6]

print("largest number is: ", largest)
print("------")
for i in numbers:
    if largest < i:
        largest = i

print(f"the largest number is: {largest}")



cubes = {'one': 1, 'two': 2, 'three': 3}

if 'three' in cubes:
    print(cubes['three'])
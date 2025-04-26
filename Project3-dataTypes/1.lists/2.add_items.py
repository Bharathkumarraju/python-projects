# create an empty list
from stomp.utils import length

animals = []

# append 'dog' to the list
animals.append('dog')

print(animals)

# append 'cat' to the list
animals.append('cat')

print(animals)


fruits = ["apple", "banana", "mango"]

if 'apple' in fruits:
    print('apple is tasty')

if 'potato' in fruits:
    print("really?")


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
length = 0

for i  in numbers:
    length = length + 1

print(length)



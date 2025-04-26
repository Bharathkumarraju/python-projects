person = {'name': 'bharath', 'age': 28}
print(person)
print(person.items())
print(person.keys())
print(person.values())

"""
 The important thing to remember about dictionaries is that the keys of a dictionary must be unique and immutable objects (that cannot be changed).

So, we can use strings, numbers, even tuples as keys. But, we cannot use lists as keys because they can be changed.
"""

dict1 = {}
print(type(dict1))

dict2 = { 1: 20, 'greet': ['hey', 'hello', 'how are you'], 'one': 1}
for i in dict2:
    print(i)
for i in dict2.items():
    print(i)

# dict3 = {[1, 2]: 'Hey'}

dict4 = {1: 'One', 1: 'Two'}
print(dict4.items())
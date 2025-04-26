animals = {'dog', 'cat', 'tiger'}
print(type(animals))
print(animals)

for i in dir(animals):
    if not i.startswith('__'):
        print(i)


numbers = { 1, 2, 3, 4, 5, 6, 2, 3, 1}
print(numbers)

set1 = {10, 'god', 3.14}
print(set1)
set1.add('hello')
print(set1)
set2 = {"hanuman", "the power of god"}

set1.update(set2)
print(set1)

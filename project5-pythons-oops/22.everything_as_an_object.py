number = 10
print(type(number))


numbers = [1, 4, 9, 16]
print(type(numbers))   # <class 'list'>

flag = True
print(type(True))   # <class 'bool'>

def my_function():
    pass

print(type(my_function))    # <class 'function'>

n = 1
print(dir(n))

result = n.__add__(100)
print(result)
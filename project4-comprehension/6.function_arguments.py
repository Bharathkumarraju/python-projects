def display_info(name,age):
    print(name)
    print(age)

display_info('Hundu', 27)


def display_info2(name, age):
    print(f"name is: {name}")
    print(f"age is: {age}")


display_info2(age=38, name='Bharath')


def subtract(first, second):
    result = first - second
    return result

result = subtract(second = 20, first = 10)
print(result)
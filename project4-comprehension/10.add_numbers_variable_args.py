def add_numbers(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

result = add_numbers(10, 20,30,40)
print(f"the sum is {result}")

result1 = add_numbers(1, 2, 3, 4, 5)
print(f"the sum is {result1}")

#------------------------------------------------------------

def print_items(*messages):
    for i in messages:
        print(i)

# take two string inputs
text1 = input("enter string1: ")
text2 = input("enter string2: ")

print_items(text1)

print_items(text1,text2)
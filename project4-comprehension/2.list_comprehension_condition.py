numbers = [1, 2, 4, 6 , 7, 9, 5, 11, 14, 17, 15, 18, 18]

even_numbers = [ i for i in numbers if i % 2 == 0]
print(even_numbers)



# get an integer input
n = int(input("enter a positive number: "))

# create a list using list comprehension
numbers = [i for i in range(1, n+1)]

# print the list
print(numbers)
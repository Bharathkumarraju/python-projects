# User input
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

# Check if n1 is the largest?
if (n1 >= n2) and (n1 >= n3):
    largest = n1

# Check if n2 is the largest?
elif (n2 >= n1) and (n2 >= n3):
    largest = n2
else:
    largest = n3

print("The largest number is:", largest)
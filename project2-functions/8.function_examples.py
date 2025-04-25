
# Define the compute_factorial() function
def compute_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# Get the user input
number = int(input("Enter a positive integer: "))

output = compute_factorial(number)
print(output)


# Print largest number


def find_largest(n1, n2, n3):
    if (n1 >= n2) and (n1 >= n3):
        largest=n1
    elif (n2 >= n3) and (n2 >= n1):
        largest=n2
    else:
        largest=n3
    return largest


n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
n3 = int(input("enter third number: "))
res = find_largest(n1, n2, n3)
print(f"The largest number is: {res}")


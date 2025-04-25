'''

Write a program to print True if the number is divisible by 5. If not, print False.

Get an integer input from the user.
Check if the input is divisible by 5.
If it's divisible by 5, print True.
If not, print False.

'''

# Get integer input
number = int(input("Enter an integer: "))

# Write your code below
result = number % 5
print(result)

if result != 0:
    print("False")
else:
    print("True")

# if result == "True":
#     print("True")
# else:
#     print("False")
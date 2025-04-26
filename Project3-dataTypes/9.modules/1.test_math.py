import math

number = 25.123

result = math.sqrt(number)
print(result)

result1 = math.floor(number)
print(result1)


# import the math module
import math

# get two integer inputs
n1 = int(input("enter n1: "))
n2 = int(input("enter n2: "))

# compute gcd
# call the gcd() function defined in the math module
# use n1 and n2 as arguments
result = math.gcd(n1, n2)

# print the result
print(result)
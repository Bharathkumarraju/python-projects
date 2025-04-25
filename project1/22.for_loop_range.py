for i in range(1,10):
    print(f"Item: {i}")


n = int(input("Enter a number to print sum of natural numbers until to it!"))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)



n = int(input("Enter a number to print sum of natural numbers until to it!"))
fact = 1

for i in range(1, n+1):
    fact = fact * i
print("fact is: ", fact)

n = int(input("Enter a number!"))
for i in range(1, n+1):
    if i %2 != 0:
        print(i)
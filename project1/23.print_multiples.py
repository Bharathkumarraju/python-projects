# Get integer input
n = int(input("Enter a positive integer: "))

for i in range(1, n+1):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)

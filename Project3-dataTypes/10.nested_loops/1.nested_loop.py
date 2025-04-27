attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for i in attributes:
    for j in cars:
        print(i, j)
    print("-------")


# get integer input
n = int(input("enrer a number: "))

# iterate the outer loop n times
for i in range(n+1):
    # iterate the inner loop 2 times
    for j in range(i):
        print("*", end=' ')
    print("")

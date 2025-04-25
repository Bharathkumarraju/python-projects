numbers = [10, 15, 20, -5, 30, -40]

for i in numbers:
    if i < 0:
        break
    print(i)


while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    print(n)
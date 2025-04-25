n=int(input("Enter a number: "))

for i in range(1, 11):
    product = n * i
    print(f"{n} * {i} = {product}")


while True:
    n = int(input("Enter an integer: "))
    # Terminate the loop if it's not between 1 and 100
    if n < 1 or n > 100:
        break
    print(n)
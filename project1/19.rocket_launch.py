countdown = int(input("Enter starting countdown number: "))
elapsed = 0

while countdown >= 0:
    print(f"Time left: {countdown} seconds")
    print(f"Elapsed: {elapsed} seconds")
    print("---")
    countdown = countdown - 1
    elapsed = elapsed + 1
print("Liftoff!")
# Take integer input
countdown = int(input("Enter starting countdown number: "))
elapsed = 0

while (elapsed < countdown) or (countdown != 0):
    print(f"Time left: {countdown} seconds")
    print(f"Elapsed: {elapsed} seconds")
    print("---")
    countdown = countdown - 1
    elapsed = elapsed + 1


# Print the "Liftoff!" message
if (countdown == 0):
    print(f"Time left: {countdown} seconds")
    print(f"Elapsed: {elapsed} seconds")
    print("---")
    print("Liftoff!")
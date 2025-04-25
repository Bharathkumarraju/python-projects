numbers = [10, -3, 5, -1, 0, 7, -8, 2]

# Initialize total
total = 0

for number in numbers:

    # Skip negative numbers
    if number < 0:
        continue

    # Terminate the loop if the number is 0
    if number == 0:
        break

        # Add positive numbers to the total
    total = total + number

# Display the total
print("Total of positive numbers:", total)
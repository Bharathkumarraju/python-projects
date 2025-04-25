total = float(input("Total? "))
discount_percent = 10

if total > 100:
    excess = total - 100
    discount = (discount_percent / 100) * excess
    total = total - discount

print(f"The final amount to pay is: ${total}")
def calculate_total_after_discount(total, discount_percent):
    if total > 100:
        extra = total - 100
        discount = (discount_percent/100) * extra
        total -= discount
    return total

# 1st customer
total = float(input("enter the billed amount is: "))
discount_percent = float(input("Discount Percentage?"))
actual=calculate_total_after_discount(total, discount_percent)
print("THe total amount payable is", actual)

# 2nd customer
total = float(input("enter the billed amount is: "))
discount_percent = float(input("Discount Percentage?"))
actual=calculate_total_after_discount(total, discount_percent)
print("THe total amount payable is", actual)

# total = float(input("enter the billed amount is: "))
# actual=calculate_total_after_discount(total)
# print("THe total amount payable is", actual)
#
# total = float(input("enter the billed amount is: "))
# actual=calculate_total_after_discount(total)
# print("THe total amount payable is", actual)
#
# total = float(input("enter the billed amount is: "))
# actual=calculate_total_after_discount(total)
# print("THe total amount payable is", actual)
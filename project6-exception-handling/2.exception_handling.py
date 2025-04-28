try:
    numerator = int(input("Enter Numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator/denominator

    print(result)
except Exception as e:
    print("the error message is: ", e)
    print("Denominator can not be zero, Try again!")

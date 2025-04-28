try:
    numbers = [10, 20, 30]
    index = int(input("enter a number!"))
    print(numbers[index])
except Exception as e:
    print("the error is: ", e)
    print("index is not found!")
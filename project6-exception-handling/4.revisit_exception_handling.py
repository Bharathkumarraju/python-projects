try:
    list1 = [10, 20, 30, 40, 50]
    for i in list1:
        print(i)
    n = int(input("enter the index number: "))
    print(f"{list1[n]}")
except Exception as e:
    print("the error is: ",e)
    print("index is not in the range")
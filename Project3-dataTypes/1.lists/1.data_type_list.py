
list1 = ["mouse", "cat",[1,2,3],[4],[7,8,9],{1:2},{2:4},{},[]]
for i in list1:
    print(i)

list_length = len(list1)
print("the length of the list is",list_length)

print(list1[0])
print(list1[1])
print(list1[6])

try:
    print(list1[10])
except Exception as e:
    print(e)

try:
    print(list1[-7])
except Exception as e:
    print(e)

print("slicing a list")
new_list = list1[2: 5]
print(new_list)

new_list1 = list1[2: ]
print(new_list1)

new_list2 = list1[: 5]
print(new_list2)

new_list3 = list1[:]
print(new_list3)


list1[1] = "Gorilla"
print(list1)

list1[-1] = "test"
print(list1)

try:
    del list1[12]
except Exception as e:
    print(e)

list1.append('rabbit')
print(list1)

# print(dir(list1))

for i in dir(list1):
    if not i.startswith("__"):
        print(i)

animals = ["dog", "cat"]
animals1 = ["rabbit", "pig"]
animals.extend(animals1)
print(animals)


list3 = ["mouse", "cat", "dog", "rabbit"]
list4 = []

for item in list3:
    list4 = [item] + list4
print(list4)



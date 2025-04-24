user = input("Please enter username: ")
print("Entered username is:", user)

x="code"
for i in x:
    print(i)

print("")
List = ["cat", "dog", "fox"]
for i in List:
    print(i)
print()
for i in range(1,6):
    print(i, end='')
print()

for i in range(6):
    print(i, end="")
print()

for i in "abacdegh":
    print(i, end="$")
print()
print("print the pattern please")

for i in range(6):
    for j in range(i):
        print(j, end='')
    print()

for i in range(5):
    for j in range(i):
        print('#', end='')
    print()

print("learn about break")

for i in range(10):
    print(i)
    if i == 5:
      break

print("learn about continue!")
for i in range(10):
    if i == 5:
        continue
    print(i)

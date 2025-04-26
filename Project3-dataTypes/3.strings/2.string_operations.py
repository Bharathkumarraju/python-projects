first_name = "Jack"
last_name = "Sparrow"

name = first_name + " " + last_name
print(name)

print("hey bro what\'s \nup!")

print(name[0])

for i in name:
    print(i)

'''
Strings are immutable; we cannot change characters of a string.

Let's see what will happen if we try to change the characters of a string.
'''
print("")
movie = "the Big short"
print(movie)
print(movie[0])
print(movie[5])
# movie[5] = 'e'
movie = "the Beg short"
print(movie)

print("\n"*3)

movie = "Avengers: Endgame"

# characters from index 0 to 7
print(movie[0: 8])   # Avengers

# characters from index 0 to 7
print(movie[: 8])   # Avengers

# characters from index 10 to 16
print(movie[10: 17])   # Endgame

# characters from index 10 to last
print(movie[10: ])   # Endgame

# characters from first to last
print(movie[:])   # Avengers: Endgame


animal = "Rat Master"

new_animal = "C" + animal[1: ]
print(new_animal)
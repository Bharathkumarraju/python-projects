squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

for key in squares:
    print(key)
    value = squares[key]
    print(f"{key} ---> {value}")

scores = {'physics': 99, 'maths': 100, 'science': 99}
print(scores.get('physics'))


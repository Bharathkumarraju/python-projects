numbers = {'one': 1, 'two': 2 , 'three': 3}

if 'two' in numbers:
    print(numbers['two'])

frontend_developers = ['Rob', 'Jane', 'Mary', 'Anne']
backend_developers = ['Jane', 'Jack', 'Lily']

# convert lists to sets and perform set intersection
both_developers = set(frontend_developers) & set(backend_developers)

# convert to list and print it
print(list(both_developers))
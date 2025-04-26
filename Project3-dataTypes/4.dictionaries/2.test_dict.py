numbers = {10: 'ten', 20: 'twenty', }

length = len(numbers)
print(length)

person_info = {}
print(len(person_info))

student_info = {
    'name': 'Gabriel',
    'major': 'Computer Science',
    'age': 20
}

print(student_info['name'], student_info['major'])

student_info['name'] = 'Amit'
student_info['major'] = 'Chemistry'
print(student_info)
student_info['City'] = 'London'
print(student_info)

del student_info['age']
print(student_info)



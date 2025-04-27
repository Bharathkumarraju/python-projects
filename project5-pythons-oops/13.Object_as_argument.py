class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_persons_attributes(self, person):
        print(self.name)
        print(self.age)
        print(person.name)
        print(person.age)


person1 = Person("raju", 40)
person2 = Person("hundu", 5)

# calling print_persons_attributes() using person1 object
# person2 is used as an argument
person1.print_persons_attributes(person2)
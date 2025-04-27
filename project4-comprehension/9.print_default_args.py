print("hello","there!", sep='######')


def greet(message, message1):
    print(message)

greet("hi", "hello")


def greet1(*messages):
    print(messages)

greet1("hi")
greet1("hi", "hello")
greet1("hi", "hello", "how are you?")
greet1()

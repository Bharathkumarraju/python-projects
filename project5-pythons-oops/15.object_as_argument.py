class Test:
    def __init__(self, name):
        self.attr = name

    def print_value(self, obj):
        print(self.attr)
        print(obj.attr)


t1 = Test('Mira')
t2 = Test('Daniel')

t2.print_value(t1)
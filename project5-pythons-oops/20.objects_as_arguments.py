# creating the Test class
class Test:

   def __init__(self, a):
       self.attr1 = a

   def call_me(self, obj):
       print(self.attr1)   # 1
       print(obj.attr1)   # 100

# object t1 of the Test class
t1 = Test(1)
t2 = Test(100)

t1.call_me(t2)
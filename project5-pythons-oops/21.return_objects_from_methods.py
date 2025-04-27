# creating the Test class
class Test:

   def __init__(self, a):
       self.attr1 = a

   def call_me(self):
       # creating a new object
       t2 = Test(1000)
       return t2

# object t1 of the Test class
t1 = Test(1)

result = t1.call_me()
print(result.attr1)   # 1000
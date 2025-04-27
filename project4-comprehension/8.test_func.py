# define the call_me() function with arguments a and b
def call_me(a = 5, b = 10):
    print(a)
    print(b)

# take integer input
n = int(input("enter N value: "))

# call call_me() with n as an argument
call_me(n)
def sum(x,y):
   return x + y

print(sum(10, 5))
print(sum(16,4))
"""
def student_names(names="Beeyond_meanings"):
    print("Hello " +  names)


student_names()
student_names("John")
student_names("Jane")


def more_num(a, b=7, c=10):
    print("a is ", a, "and b is ", b, "while c is ", c)

more_num(3, 7)
more_num(23, c=17)
more_num(c=40, a=80)


def greeting():
    def say_hello():
        return "Hello"
    return say_hello
hello = greeting()

print(hello())


def mynum(x):
    return x + 1
num = mynum

print(num(7))
print(mynum(8))

#Anonymous function (Lambda)

a = lambda b: b + 4
print(a(4))

c = lambda d, e, : d + e
print(c(7,8))

def ghost_number(n):
    return lambda f : f * n

double_num = ghost_number(2)

print(double_num(20))

#DocString function

def add_numbers(d, e):
    ''' Adding two numbers.

    The values must be intergers'''

    print(d + e)



add_numbers(8, 4)

print(add_numbers.__doc__)

#DECORATOR FUNCTION:
def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper
@my_decorator
def say_hello():
    return "hello world"
#decorate = my_decorator(say_hello)
print(say_hello())

def greet(name, age=-1):
    print(f"Hello {name} how are you?")
    if age >= 0:
     print(f"I know your age = {age}")

greet("Maduabuchi", 35)
greet("Alex", 4)


def is_adult(age):
    if age >= 16:
        return True
    else:
        return False
result = is_adult(35)
print(result)
"""

def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"

print(convertGender("F"))
print(convertGender("f"))
print(convertGender("M"))
print(convertGender("m"))
print(convertGender("hello"))

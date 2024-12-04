# Functions
# is a block of code which only run when it is called


# Creating a Function

# In Python a function is defined using the def keyword:

def my_code():
    print("I love python")


# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_code()


# Argument
# Information can be passed into functions as arguments.


# Arguments are specified after the function name, inside the parentheses.
def name(fname):
    print(fname + " that name")


name("John")


# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print(kids)


# return value
# To let a function return a value, use the return Statement
print("Return a value")


def add(x):
    return x * 2


print(add(5))

# Python Lambda

# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression


def x(a): return a + 10


print(x(3))


# Lambda functions can take any number of arguments:

(lambda w: w * 3)(2)

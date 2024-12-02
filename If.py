# If ... Else statement

# An "if statement" is written by using the if keyword.

a = 50
b = 20

if a > b:
    print(a)


# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 330
b = 2
print("A") if a > b else print("B")


# And
# The and keyword is a logical operator, and is used to combine conditional statements:

c = 500
if a > b and c > a:
    print("Both conditions are true")
else:
    print("No")

# or
if a > b or a > c:
    print("At least one of the conditions is True")

# not
if not a > b:
    print("a is NOT greater than b")

print("    ")
# Nested if
x = 40
if x > 10:
    print("above 10")
    if x == 20:
        print("it equal too")
    else:
        print("It not equal")


age = int(input("Enter your age: ")) 
if age >= 18: print("You are eligible to vote!")
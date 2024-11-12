# Boolean Value

# When you compare two values, the expression
# is evaluated and Python returns the Boolean answer


# > greater than sign
# < less than sign

print(10 > 20)
print(10 > 5)
print(5 < 4)
print(15 < 60)

print(10 == 5)


a = 30
b = 50
if b > a:
    print("b is greater than a")
else:
    print("b is less than a")

# Any string is TRUE, expect empty string
y = "JOHN"
x = ""
print(bool(y))
print(bool(x))


# Any number is True, except 0.

num1 = 30
num2 = 0
print("for 30:", bool(num1))
print("for 0:", bool(num2))

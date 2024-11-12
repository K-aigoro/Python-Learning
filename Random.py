
# To make random number
import random

a = random.randrange(5, 20)
print(a)

b = random.randrange(20, 50)
print(b)

c = b + a
print("The sum of the random numbers generated of", a, "and", b, "=", c)

# F-Strings - for combine string and Number
age = 18
txt = f"My name is John, I am {age*2}"
print(txt)

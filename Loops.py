

# while loops and for loops

# While loop- Execute a set of statements as long as condition is true.

i = 1
print("This is a while loop")
while i < 5:
    print(i)
    i += 1

# Note: remember to increment i, or else the loop will continue forever.

# z = int(input("enter y "))

# print(z)

# break Statement
# With the break statement we can stop the loop even if the while condition is true:

x = 1
print("Break Statment")
while x < 10:
    print(x)
    if x == 7:
        break
    x += 1


# For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry", "pineapple"]
print("For Loop")
for x in fruits:
    print(x)

# loop through a string
print("loop through a string ")
for y in "pineapple":
    print(y)

print("Break statement in for loop ")

for x in fruits:
    print(x)
    if x == "banana":
        break

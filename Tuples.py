
# Tuples are used to store multiple items in a single variable.
mytuple = ("apple", "banana", "cherry")
print(mytuple)


# Unchangeable - it means that items can not be change, add or
# removed after tuples has been created

# Access a tuple
second = mytuple[1]
print(second)

# Length of a tuple
print(len(mytuple))

# Tuples can be any datatype
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple_all = ("abc", 10, True, "apple")
print(tuple_all)


# check if item exist

if "banana" in tuple1:
    print("yes")


x = list(tuple1)
x[1] = 5
print(x)
tuple1 = tuple(x)
print(tuple1)


# unpacking in tuple

fruit = ("Pineapple", "orange", "Apple", "Carrot")
(green, yellow, *red) = fruit
print(green)
print(red)
print(yellow)


# Loop through a tuple

# using for Loop
print("This is a loop")

for x in fruit:
    print(x)


print(" join tuple")

tuple1 = + tuple2
print(tuple1)

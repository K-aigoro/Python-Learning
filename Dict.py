# Dictionaries are used to store data values in key:value pairs.
dict = {
    "name": "Kazeem",
    "Job": "Software Engineer",
    "Passion": "Love to solve problem"
}


print(dict)
print(type(dict))
print(len(dict))

this_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# Accessing Item -You can access the items of a dictionary by referring to its key name, inside square brackets:
print("Acessing Item in the dict")

x = this_dict["brand"]
print(x)

# Key() method - Return a list of all the keys in the dict

y = this_dict.keys()
print(y)

w = this_dict.values()
print(w)

# Change Value - by referring to it value

# You can change the value of a specific item by referring to its key name:
this_dict["year"] = 2005

print(this_dict)


# Adding items - is done by using new index key to assign a value

this_dict["Course"] = "Comp Sci"

print(this_dict)

# Remove item
# pop() method- specified key name:

this_dict.pop("year")
print(this_dict)

# The popitem() method removes the last inserted item

this_dict.popitem()
print(this_dict)
# The clear() method empties the dictionary:


# Loop in Dict - using for loop
# When looping through a dictionary, the return value are the keys of the dictionary
for x in dict:
    print(x)
    # to print value
    print(dict[x])


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.


myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)
# Access Items
print(myfamily["child2"]["name"])

# loop
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

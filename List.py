

# List are used to Store Mutiple items in asingle variable
this_list = ["apple", "orange", "fruits"]
print(this_list)

# list length - len

print(len(this_list))

# list can be any data type or mix datatype
this_number = [1, 3, 5, 7, 4]

differnt_type = ["joe", 40, True, "Male"]
print(differnt_type)

# Access a list item
print(differnt_type[0])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

if "apple" in this_list:
    print("yes it exist")

# change list item

this_list[2] = "pineapple"
print(this_list)

# remove List Items
this_list1 = ["apple", "banana", "cheey", "pineapple"]
print(this_list1)
this_list1.remove("banana")
# Remove specified index
this_list1.pop(2)

print(this_list1)


# LOOP list - using for loop

thislist3 = ["apple", "banana", "cherry"]
for x in thislist3:
    print(x)

thislist3.sort()
print(thislist3)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# join list 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
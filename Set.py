
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.

my_Set = {"Python", "Java", "C+", "Go", "cloud"}

print(my_Set)

# Set cannot have items with same value

# Access item
# item cannot be access using index in set

# but it can be loop through or check specific item

print("Java" in my_Set)

# ADD item
my_Set.add("SQL")
print(my_Set)


# Remove set items

my_Set.remove("Java")

print(my_Set)

# join sets


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# The union() and update() methods joins all items from both sets.
set3 = set1.union(set2)
print(set3)

# The intersection() method keeps ONLY the duplicates.
set3 = set1 | set2
print(set3)

# The difference() method keeps the items from the first set that are not in the other set(s).


# The symmetric_difference() method keeps all items EXCEPT the duplicates.

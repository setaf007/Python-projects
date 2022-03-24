values = input("Input comma seperated values: ")
#list is container (items need not be same data type, can be changed)
list = values.split(",")
#tuple is immutable container (cannot be changed after being set)
tuple = tuple(list)

print("List: ", list)
print("Tuple: ", tuple)
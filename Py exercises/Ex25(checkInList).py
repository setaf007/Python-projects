def searcher(group, value):
    return value in group


group = [1,3,4,5,6,9]
value = int(input("Enter value to search for: "))
if searcher(group, value) == True:
    print("Value is in group")
else:
    print("Value is not in group")
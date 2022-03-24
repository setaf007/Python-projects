numbers = input("Enter 3 numbers seperated by space: ")
splits = numbers.split()
#convert string list to int list
intsplits = [int(i) for i in splits]
print(sum(intsplits))
filename = input("Input filename with extension: ")
#split with delimitter .
extension = filename.split(".")
#take out last element in extension array with split elements
print("File extension is: " + extension[-1])
word = input("Enter word: ")
n = int(input("Enter number of times to copy: "))

if (len(word) < 2):
    print("Repeated string: ", word * n)
else:
    s = word[:2]
    print("Repeated string: ", s*n)
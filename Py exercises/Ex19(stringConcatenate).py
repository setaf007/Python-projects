def concat(x):
    if len(x) >=2 and x[:2] == "Is":
        return x

    return "Is" + x

x = input("Input string: ")
print("New string is: ", concat(x))
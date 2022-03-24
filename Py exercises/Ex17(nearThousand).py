#check if number within 100 of 1000 or 2000
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

x = int(input("Input number: "))
print("Is number 100 near 1000 or 2000? ",near_thousand(x))
def counter(numbers):
    count = 0
    for num in numbers:
        if (num == 4):
            count = count + 1
    return count

numbers = input("Enter numbers seperated by space: ")
numsplits = numbers.split()
numsplits2 = [int(i) for i in numsplits]
count = counter(numsplits2)
print("Number of times 4 has been entered: ", count)

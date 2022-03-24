def histogram(hist):
    for n in hist:
        output = ''
        times = n
        while(times > 0):
            output += '@'
            times = times - 1
        print(output)


hist = input("Enter histogram values seperated by space: ")
hist = hist.split()
hist2 = [int(i) for i in hist]
histogram(hist2)
import datetime

time = datetime.datetime.now()
format = time.strftime("%d-%m-%Y %H:%M:%S")
print("Current Date and Time: " + format)
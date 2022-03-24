from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2021, 10, 22)

diff = date2 - date1

print(diff.days)
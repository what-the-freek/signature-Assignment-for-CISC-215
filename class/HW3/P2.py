years = int(input())
total = 0
months = years*12
for i in range(1, years+1):
    for a in range(1, 12+1):
        rain = int(input())
        total = total + rain
ave = total/months
print("amount of months:", months, "total rain:", total, "inches. average per month", ave)
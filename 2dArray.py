#15/09/25
import random

cust = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
    ]
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
hours = ["6am","7am","8am","9am","10am","11am","12pm"]

for i in range(0,7):
    for j in range(0,7):
        cust[i][j] = 60+random.randint(-40,40)

for i in range(0,7):
    print(cust[i])
print("")

for i in range(0,7):
    for j in range(0,7):
        print(cust[i][j], end=" ")
        if cust[i][j]<10:
            print(" ",end="")
    print()

maxV = cust[0][0]
maxD = 0
maxT = 0
for day in range(0,7):
    for hour in range(0,7):
        if cust[day][hour] > maxV:
            maxV = cust[day][hour]
            maxD = day
            maxT = hour

maxWV = 0
maxW = 0
for day in range(0,7):
    overall = 0
    for hour in range(0,7):
        overall += cust[day][hour]
    if overall > maxWV:
        maxWV = overall
        maxW = day

overallDay = 0
overallEnd = 0

for day in range(0,7):
    for hour in range(0,7):
        if day == 0 or day == 6:
            overallEnd += cust[day][hour]
        else:
            overallDay += cust[day][hour]


print("")
print("The busiest time was on",days[maxD],"at",hours[maxT],"with",maxV,"customers")
print("")
print("The busiest day of the week was",days[maxW],"with",maxWV,"customers")
print("")
print("The average number of customers on a weekday was",overallDay//5,"customers")
print("")
print("The average number of customers on a weekend was",overallEnd//2,"customers")
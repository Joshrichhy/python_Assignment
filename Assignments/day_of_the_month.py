day = int(input("Enter today's day in number: "))
future_day = int(input("Enter the number of days elapsed since today: "))
future = (future_day + day) % 7

if day == 0:
    print("Today is Sunday")
if day == 1:
    print("Today is monday")
if day == 2:
    print("Today is Tuesday")
if day == 3:
    print("Today is Wednesday")
if day == 4:
    print("Today is Thursday")
if day == 5:
    print("Today is Friday")
if day == 6:
    print("Today is Saturday")


if future == 0:
    print("future day is Sunday")
if future == 1:
    print("future day is monday")
if future == 2:
    print("future day is Tuesday")
if future == 3:
    print("future day is Wednesday")
if future == 4:
    print("future day is Thursday")
if future == 5:
    print("future day is Friday")
if future == 6:
    print("future day is Saturday")


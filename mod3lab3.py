year = int(input("Enter a year: "))
if year<1582:
    print("Not within the Gregorian calendar period")

if year%4!=0:
    print(year,"is a common year")
elif year%100!=100:
    print(year,"is a leap year")
elif year%400!=0:
    print(year,"is a common year")
else:
    print(year,"is a leap year")

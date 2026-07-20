year = int(input("Enter the year to check: "))
if year%4==0 and (year%100 != 0 or year%400==0):
    print("Leap year!!")
else: 
    print("Not leap year!!")

#built in calendar module
import calendar
print(calendar.isleap(year))
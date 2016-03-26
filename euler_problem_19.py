'''
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

startYear = 1900
endYear = 2000
monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
totalDays = 0
totalSundaysOnFirst = 0
# listz = [1900]
# for year in listz:
for year in range(startYear,endYear+1):
	monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
		monthDays = [31,29,31,30,31,30,31,31,30,31,30,31]
	for num in monthDays:
		if (totalDays + 1) % 7 == 0:
			totalSundaysOnFirst += 1
		totalDays += num

print totalSundaysOnFirst - 2
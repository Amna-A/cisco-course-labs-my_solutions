#Your task is to write and test a function which takes two arguments (a year and a month) 
# and returns the number of days for the given month/year pair 
# (while only February is sensitive to the year value, 
# your function should be universal).
# The initial part of the function is ready. 
# Now, convince the function to return None if its arguments don't make sense.

#-----------leap year function---------------------------
def isYearLeap(year):
    if year % 4 != 0:
        return True
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return True
    else:
	    return False
#---------------------------------------------
def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

#---------------------------------------------------------------------------
def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		# ...
		# if statement
			# ...
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		# ...
	else:
		# ...


#--------------------testing--------------------------------------------------

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
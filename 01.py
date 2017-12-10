from enum import Enum

Day_Of_The_Week = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday') 
print 'Days of the week: '
for i in Day_Of_The_Week:
	print i
try:
	pick_favourite_day_of_week = input('Pick your favourite day of the week')
	if pick_favourite_day_of_week == 1:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[0])
	elif pick_favourite_day_of_week == 2:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[1])
	elif pick_favourite_day_of_week == 3:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[2])
	elif pick_favourite_day_of_week == 4:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[3])
	elif pick_favourite_day_of_week == 5:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[4])
	elif pick_favourite_day_of_week == 6:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[5])
	elif pick_favourite_day_of_week == 7:
		print 'Your favourite day of the week is ' + str(Day_Of_The_Week[6])
except:
	print 'Please enter a number between 1-7'

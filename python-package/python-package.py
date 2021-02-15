#!/usr/bin/env python

"""
A package that determines the current day of the week.
"""

from datetime import date 
import calendar

# Set the first day of the week as Sunday.

calendar.firstday(calendar.SUNDAY)

def day_of_the_week(arg):

	"""
	Returns the current day of the week.
	"""
    
    if arg == "day":
        day_of_the_week = calendar.day_name[date.today().weekday()]
        print("Today is " + day_of_the_week + ".")	


    #Raise exception for invalid argument
    else:
    	raise Exception ("Invalid argument for day of the week")	


 def info():
    
    """
    Returns information about the package.
	"""

	 info = "This package determines the day of the week."
	 print(info)

if __name__ == "__main__"
	day("today")
	info()

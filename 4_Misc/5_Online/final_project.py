import datetime as dt
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    correctDate = None
    try:
        newDate = dt.datetime(year, month, day)
        correctDate = True
        return True
    except ValueError:
        correctDate = False
        return False
    #return correctDate

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if (year2 >= year1 and month2 >= month1 and day2 >= day1) or (year2 >= year1 and month2 >= month1) or (year2 >= year1):
        d1 = dt.date(year1, month1, day1)
        d2 = dt.date(year2, month2, day2)
        #delta = (dt.date(year2, month2, day2) - dt.date(year1, month1, day1))
        delta = d2 - d1
        #print("Its okay diff")
        return delta.days
    elif (year2 < year1) or (year2 < year1 and month2 < month1) or (year2 < year1 and month2 < month1 and day2 < day1):
        #print("Wrong diff 1")
        return 0
    else:
        #print("Wrong diff 0")
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    year_now = dt.date.today().year
    month_now = dt.date.today().month
    day_now = dt.date.today().day
    print(str(year_now) + " _ " + str(month_now) + " _ " + str(day_now))

    if is_valid_date(year, month, day):
        #print("Date is valid")
        return days_between(year, month, day, year_now, month_now, day_now)
    else:
        return 0

#print(age_in_days(2016, 12, 31))
#print(days_between(2017, 12, 31, 2018, 1, 1))
#print(is_valid_date(2017, 2, 28))
#print(days_in_month(2005, 2))
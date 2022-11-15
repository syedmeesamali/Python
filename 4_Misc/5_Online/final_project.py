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
    newDate = None
    if (year >= 1 and year <= 9999):
        if (month > 0 and month <= 12):
            if (day > 0 and day <= 31):
                try:
                    newDate = dt.date(year, month, day)
                    #date_now = dt.date.today()
                    return True
                except:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

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
    
    #Check date validity before carrying out delta
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        d1 = dt.date(year1, month1, day1)
        d2 = dt.date(year2, month2, day2)
        delta = d2 - d1
        if delta.days > 0:
            return delta.days
        else:
            return 0
    else:
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
    #print(str(year_now) + " _ " + str(month_now) + " _ " + str(day_now))
    if is_valid_date(year, month, day):
        days_Val = days_between(year, month, day, year_now, month_now, day_now)
        if days_Val > 0:
            return days_Val
        else:
            return 0
    else:
        return 0

#print(days_between(2022, 11, 10, 2022, 11, 15))
#print(days_between(2017, 12, 31, 2018, 1, 1))
#print(days_between(1973, 8, 14, 1973, 8, 13))
#print(age_in_days(2022, 11, 10))
#print(age_in_days(0, 1, 21))
#print(days_between(20000, 1, 1, 2047, 8, 2))
#print(is_valid_date(9998, 12, 31))
#print(age_in_days(1, 1, 1))
#print(days_between(2032, 2, 31, 1322, 9, 16))
#print(is_valid_date(0, 1, 1))
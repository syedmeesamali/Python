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
    if year <= dt.MAXYEAR and year >= dt.MINYEAR:
        if month > 0 and month <= 12:
            if day > 0 and day <= 31:
                return True
    else:
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
    if year2 >= year1 or (year2 >= year1 and month2 >= month1) or (year2 >= year1 and month2 >= month1 and day2 >= day1):
        delta = dt.date(year2, month2, day2) - dt.date(year1, month1, day1)
        return delta.days
    elif year1 > year2:
        return 0
    elif year1 < year2 and month1 > month2:
        return 0
    elif year1 < year2 and month1 < month2 and day1 > day2:
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
    print(str(year_now) + " _ " + str(month_now) + " _ " + str(day_now))

    if is_valid_date(year, month, day):
        print("Date is valid")
        return days_between(year, month, day, year_now, month_now, day_now)
    else:
        return 0

print(age_in_days(2016, 12, 31))
print(days_between(1973, 8, 14, 1973, 8, 13))
print(is_valid_date(0, 1, 1))
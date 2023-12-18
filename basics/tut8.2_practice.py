# number of days per month. First value placeholder for indexing purposes.
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    '''Returns True for leap years and False for non-leap years.'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month of the year."""

    if not 1 <=month<=12:
        return "invalid month"
    
    if month ==2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017))
print (days_in_month(2020, 2))
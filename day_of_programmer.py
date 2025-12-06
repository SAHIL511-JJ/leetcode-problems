#!/usr/bin/env python3
"""
HackerRank: Day of the Programmer
https://www.hackerrank.com/challenges/day-of-the-programmer

The Day of the Programmer is the 256th day of the year.
Given a year, find the date of the Day of the Programmer in dd.mm.yyyy format.

Note: Russia switched from Julian to Gregorian calendar in 1918.
In the Julian calendar, leap years are divisible by 4.
In the Gregorian calendar, leap years are divisible by 400 or by 4 but not 100.
"""

def day_of_programmer(year):
    """
    Find the date of Day of the Programmer (256th day).
    
    Args:
        year: the year to check
    
    Returns:
        Date string in dd.mm.yyyy format
    """
    # Special case: Transition year 1918
    # Russia skipped Feb 14 to Feb 28 (13 days)
    if year == 1918:
        return '26.09.1918'
    
    # Determine if leap year
    if year < 1918:
        # Julian calendar: leap year if divisible by 4
        is_leap = (year % 4 == 0)
    else:
        # Gregorian calendar
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    # Days in each month Jan-Aug
    if is_leap:
        days_before_sep = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31  # 244 days
    else:
        days_before_sep = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31  # 243 days
    
    day_in_september = 256 - days_before_sep
    
    return f'{day_in_september:02d}.09.{year}'


if __name__ == '__main__':
    year = int(input())
    result = day_of_programmer(year)
    print(result)

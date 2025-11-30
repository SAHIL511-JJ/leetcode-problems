#!/bin/python3

import os

def timeConversion(s):
    """
    Convert 12-hour time format to 24-hour time format.
    
    Args:
        s: Time string in 12-hour format (e.g., '07:05:45PM')
    
    Returns:
        Time string in 24-hour format (e.g., '19:05:45')
    """
    period = s[-2:]  # AM or PM
    time_parts = s[:-2].split(':')
    hour = int(time_parts[0])
    
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}:{time_parts[1]}:{time_parts[2]}"

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()

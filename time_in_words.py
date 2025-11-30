#!/bin/python3

import os

def timeInWords(h, m):
    """
    Convert time from numeric to word format.
    
    Args:
        h: Hour (1-12)
        m: Minutes (0-59)
    
    Returns:
        Time in words
    """
    numbers = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
        26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'
    }
    
    if m == 0:
        return f"{numbers[h]} o' clock"
    elif m == 15:
        return f"quarter past {numbers[h]}"
    elif m == 30:
        return f"half past {numbers[h]}"
    elif m == 45:
        return f"quarter to {numbers[h % 12 + 1]}"
    elif m == 1:
        return f"one minute past {numbers[h]}"
    elif m < 30:
        return f"{numbers[m]} minutes past {numbers[h]}"
    elif m == 59:
        return f"one minute to {numbers[h % 12 + 1]}"
    else:
        return f"{numbers[60 - m]} minutes to {numbers[h % 12 + 1]}"

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    fptr.write(result + '\n')
    fptr.close()

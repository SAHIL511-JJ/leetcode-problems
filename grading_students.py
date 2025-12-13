#!/usr/bin/env python3
"""
HackerRank: Grading Students
https://www.hackerrank.com/challenges/grading

Round grades according to rules:
- If grade < 38, no rounding (failing)
- If difference between grade and next multiple of 5 is < 3, round up
"""

def grading_students(grades):
    """
    Round grades according to university rules.
    
    Args:
        grades: list of student grades
    
    Returns:
        List of rounded grades
    """
    result = []
    
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            # Find next multiple of 5
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    
    return result


if __name__ == '__main__':
    n = int(input())
    grades = [int(input()) for _ in range(n)]
    result = grading_students(grades)
    for grade in result:
        print(grade)

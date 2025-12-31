#!/usr/bin/env python3
"""
HackerRank: Fraudulent Activity Notifications
https://www.hackerrank.com/challenges/fraudulent-activity-notifications

Given expenditure data for n days and lookback period d,
find notifications triggered when spending >= 2x median of last d days.
"""

def activity_notifications(expenditure, d):
    """
    Count fraud notifications using counting sort for median.
    
    Args:
        expenditure: list of daily expenditures
        d: lookback period
    
    Returns:
        Number of notifications
    """
    notifications = 0
    count = [0] * 201  # Values are 0-200
    
    # Initialize count for first d days
    for i in range(d):
        count[expenditure[i]] += 1
    
    def get_median():
        """Get median from count array."""
        total = 0
        if d % 2 == 1:
            for i in range(201):
                total += count[i]
                if total > d // 2:
                    return i
        else:
            m1, m2 = None, None
            for i in range(201):
                total += count[i]
                if m1 is None and total > d // 2 - 1:
                    m1 = i
                if total > d // 2:
                    m2 = i
                    break
            return (m1 + m2) / 2
    
    for i in range(d, len(expenditure)):
        median = get_median()
        if expenditure[i] >= 2 * median:
            notifications += 1
        
        # Slide the window
        count[expenditure[i]] += 1
        count[expenditure[i - d]] -= 1
    
    return notifications


if __name__ == '__main__':
    n, d = map(int, input().split())
    expenditure = list(map(int, input().split()))
    result = activity_notifications(expenditure, d)
    print(result)

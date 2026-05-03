"""
LeetCode #70: Climbing Stairs
You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps.
Return the number of distinct ways to climb to the top.
This is essentially the Fibonacci sequence.
"""


def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


def climb_stairs_with_memo(n):
    """Alternative solution using memoization."""
    memo = {}

    def helper(steps):
        if steps <= 2:
            return steps
        if steps not in memo:
            memo[steps] = helper(steps - 1) + helper(steps - 2)
        return memo[steps]

    return helper(n)


if __name__ == "__main__":
    for n in range(1, 11):
        print(f"Steps: {n}, Ways: {climb_stairs(n)}")

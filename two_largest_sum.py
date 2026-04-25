# Two Largest Sum
# Given an integer array nums, return the sum of the two largest integers in the array.
#
# Example:
#   Input: nums = [1, 2, 3, 4, 5]
#   Output: 9 (because 4+5=9)
#
# Constraints:
#   2 <= nums.length <= 10^4
#   -10^4 <= nums[i] <= 10^4
#
# Approach:
#   We can find the two largest by iterating through the array and keeping track of the two largest numbers.
#   Alternatively, we can sort the array and take the last two elements.
#   Sorting approach: O(n log n) time, O(1) space (if we sort in place) or O(n) space (if we create a copy).
#   However, we can do it in O(n) time with O(1) space by scanning.
#
#   We initialize two variables, first and second, to negative infinity.
#   For each number in the array:
#     If the number is greater than first, then update second to be first, and first to be the number.
#     Else if the number is greater than second (and not equal to first, to handle duplicates), update second.
#   Then return first + second.
#
#   Edge case: if there are duplicates, we want to make sure we capture the two largest distinct values?
#   But note: the problem says 'two largest integers', so if the array is [5,5,5,5], then the two largest are 5 and 5, so sum=10.
#   Our algorithm above will work for duplicates because when we see a duplicate of the current first, we won't update first (since it's not greater) but we will update second if it's greater than second (which it is, because second might be less than first).
#   However, let's test with [5,5,5,5]:
#     Start: first=-inf, second=-inf
#     See 5: 5 > -inf -> second=-inf, first=5
#     See 5: 5 is not > first (5) -> check if 5 > second (-inf) -> yes, so second=5
#     See 5: 5 is not > first (5) -> 5 is not > second (5) -> no change
#     See 5: same as above.
#     Result: first=5, second=5 -> sum=10.
#   So it works.
#
#   Alternatively, we can use sorting: sorted_nums = sorted(nums); return sorted_nums[-1] + sorted_nums[-2]
#   But the problem might be looking for an efficient solution, so we'll implement the O(n) solution.

def two_largest_sum(nums):
    if len(nums) < 2:
        # According to constraints, this shouldn't happen, but we handle it.
        return None
    
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    
    return first + second

# Example usage:
if __name__ == \
__main__\:
    example1 = [1, 2, 3, 4, 5]
    print(f\Input:
example1
\)
    print(f\Output:
two_largest_sum(example1)
\)  # Expected: 9
    
    example2 = [5, 5, 5, 5]
    print(f\Input:
example2
\)
    print(f\Output:
two_largest_sum(example2)
\)  # Expected: 10
    
    example3 = [10, -5, 8, 3]
    print(f\Input:
example3
\)
    print(f\Output:
two_largest_sum(example3)
\)  # Expected: 18 (10+8)


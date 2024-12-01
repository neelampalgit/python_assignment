# Maximum Subarray Sum:
#     Problem: Given an array of integers, find the contiguous subarray
#     (containing at least one number) which has the largest sum.
#     Example: max_subarray_sum([1, 2, 3, -2, 5]) should return 9

def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
print(max_subarray_sum([1, 2, 3, -2, 5]))  # Output: 9

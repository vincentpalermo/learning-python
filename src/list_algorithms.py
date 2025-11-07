def unique_keep_order(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return result

def reverse_list(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

def find_min_max(nums):
    min, max = nums[0], nums[0]
    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max

def count_occurrences(nums):
    result = {}
    for i in nums:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
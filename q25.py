def has_dup(nums):
    return len(set(nums)) != len(nums)
nums = [5,7,8,9,9]
print(has_dup(nums))
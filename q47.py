def is_sorted(nums):
    for i in range(len(nums)- 1):
        if nums[i] > nums[i+1]:
            return False
    return True
nums = [1,2,2,4]
print(is_sorted(nums))
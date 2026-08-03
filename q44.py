def max(nums):
    result = []
    m = nums[0]
    for i in nums:
        if i > m:
            m = i
            result.append(m)
    return result
nums = [3,3,1,5,4]
print(max(nums))

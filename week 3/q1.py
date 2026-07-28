def total(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
    return s
nums = [10,20,30,40,50]
result = total(nums)
print("Total = " ,result)

    
def two_sum(nums,target):
    for i in range(len(nums)):
     for j in range(i+1,len(nums)):
        if nums[i]+ nums[j] == target:
           return (i,j)
    return None
nums = [2,8,7,6]
target = 20
print(two_sum(nums,target))

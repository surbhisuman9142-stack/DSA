def adjacent_pair_sums(nums):
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] + nums[i  + 1])
    return result
nums = [2,4,6,8]
print(adjacent_pair_sums(nums))
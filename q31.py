def two_sum(nums,target):
    seen = {}
    for i,x in enumerate(nums):
        need = target - x
        if need in seen:
            return(seen[need], i)
        seen[x]  = i
    return None
nums = [4,5,6,7]
target = 9
print(two_sum(nums,target)) 
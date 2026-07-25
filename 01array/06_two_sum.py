def two_sum_using_map(nums,target):
    hashmap = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i

    return []

def two_sum_using_binary(nums,target):
    nums.sort()

    l = 0
    r = len(nums) - 1

    while l<r:

        sum = nums[l] + nums[r]

        if target == sum:
            return [nums[l],nums[r]]

        elif sum < target:
            l += 1

        else:
            r -= 1

    return []


nums = [2, 7, 11, 15]
target = 13

print(two_sum_using_map(nums, target))
print(two_sum_using_binary(nums, target))

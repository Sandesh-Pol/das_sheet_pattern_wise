def lower_bound(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
                r = mid - 1
        else:
                l = mid + 1

    return l

print(lower_bound([1,3,4],2))

def rotated_array(nums, target, l, r):

    if l > r:
        return -1

    mid = l + (r - l) // 2

    if nums[mid] == target:
        return mid

    # Left half is sorted
    if nums[l] <= nums[mid]:

        if nums[l] <= target < nums[mid]:
            return rotated_array(nums, target, l, mid - 1)
        else:
            return rotated_array(nums, target, mid + 1, r)

    # Right half is sorted
    else:

        if nums[mid] < target <= nums[r]:
            return rotated_array(nums, target, mid + 1, r)
        else:
            return rotated_array(nums, target, l, mid - 1)


nums = [4,5,6,7,0,1,2]
target = 0

print(rotated_array(nums, target, 0, len(nums) - 1))

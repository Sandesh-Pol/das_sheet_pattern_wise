def move_zero_to_end(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums

print(move_zero_to_end([1, 4, 0, 3, 2, 0]))
